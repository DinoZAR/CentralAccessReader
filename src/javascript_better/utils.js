/**
 * General Utility Functions
 * 
 * @author Spencer Graffe
 */

/*******************************************************************************
Selection Functions
 *******************************************************************************/

/**
 * Gets the selection range. 
 */
function GetSelectionRange() {
	range = ConvertUserSelectionToRange();

	// Check if I don't have a user selection or not
	if (range.collapsed) {
		// Start from beginning or last navigated heading
		if (startFromHeading) {
			range.selectNodeContents(DeepestChild(lastHeadingElement));
			range.startOffset = 0;
		}
		else {
			range = GetRangeToEntireDocument();
			//console.debug('Range here: ' + GetHTMLSource(range));
		}
	}
	else {
		// Start from the user selection. Do some random fixes for it
		console.debug(' > Stage 0: ' + GetHTMLSource(range));
		MoveRangeAfterWhitespace(range);
		console.debug(' > Stage 1: ' + GetHTMLSource(range));
		MoveRangeStartToDeepestInBody(range);
		console.debug(' > Stage 2: ' + GetHTMLSource(range));
		SurroundMathEquation(range);
		console.debug(' > Stage 3: ' + GetHTMLSource(range));
		MoveRangeOverEmptyParagraph(range);
		console.debug(' > Stage 4: ' + GetHTMLSource(range));
	}

	ClearAllHighlights();
	SetUserSelection(range);

	//console.debug('GetSelectionRange() ' + GetHTMLSource(range));

	return range;
}

/**
 * Gets the HTML content of my selection and returns it. 
 */
function GetSelectionHTML() {
	console.debug("GetSelectionHTML()");
	var range = GetSelectionRange();
	return GetHTMLSource(range);
}

/**
 * Takes a Range object and extracts the HTML content as text.
 * 
 * @param range 
 */
function GetHTMLSource(range) {
	//console.debug("GetHTMLSource()");
	var clonedSelection = range.cloneContents();
	div = document.createElement('div');
	div.appendChild(clonedSelection);
	return div.innerHTML;
}

/**
 * Moves the start of the range after any beginning whitespace.
 * 
 * @param range 
 */
function MoveRangeAfterWhitespace(range) {
	if (range.startContainer.nodeName == '#text') {
		var whitespaceRegex = /\s+/g;
		var sub = range.startContainer.data;
		console.debug('Substring is: ' + sub);
		sub = sub.substring(range.startOffset);
		console.debug('Substring is: ' + sub);
		var result = whitespaceRegex.exec(sub);
		if (result !== null) {
			console.debug('Skipping #text node with whitespace...');
			if (result.index === 0) {
				range.setStart(range.startContainer, whitespaceRegex.lastIndex + range.startOffset);
			}
		}
	}
}

/**
 * If the start node is a body element, it will be altered to deepest child of 
 * the element referred to by the offset in the body.
 * 
 * @param range
 */
function MoveRangeStartToDeepestInBody(range) {
	if (range.startContainer.nodeName == 'BODY') {
		console.debug('Moving start to deepest element in offset of body');
		myNode = DeepestChild(document.body.childNodes[range.startOffset], false);
		range.setStart(myNode, 0);
	}
}

/**
 * If the start and end of the range are inside of the same equation, move the 
 * start and end out to surround that equation.
 * 
 * @param range
 */
function SurroundMathEquation(range) {
	startEq = GetEquation(range.startContainer);
	endEq = GetEquation(range.endContainer);
	if ($(startEq).is($(endEq)) && (startEq !== null)) {
		console.debug('Equation: ' + startEq.nodeName + ', class name: ' + startEq.className);
		range.selectNode(startEq);
		range.setStart(startEq, 0);
	}
}

/**
 * If the start is a paragraph with nothing it, move to the next element.
 * 
 * @param range 
 */
function MoveRangeOverEmptyParagraph(range) {
	if ((range.startContainer.nodeName == 'P') && !(range.startContainer.hasChildNodes())) {
		console.debug('Moving off of a completely empty paragraph');
		range.setStart(NextElement(range.startContainer), 0);
	}
}

/**
 * Sets the user selection to the range given.
 * 
 * @param range 
 */
function SetUserSelection(range) {
	var sel = window.getSelection();
	sel.removeAllRanges();
	sel.addRange(range);
}

/**
 * Converts a user selection to a Range object. This is NOT a SelectionRange 
 * object.
 */
function ConvertUserSelectionToRange() {
	var range = window.getSelection();
	var newRange = document.createRange();
	if (!range.isCollapsed) {
		newRange.setStart(range.anchorNode, range.anchorOffset);
		newRange.setEnd(range.focusNode, range.focusOffset);

		// Switch the two ends around if it is reversed
		if (newRange.startContainer.compareDocumentPosition(newRange.endContainer) && Node.DOCUMENT_POSITION_PRECEDING) {
			var temp = newRange.startContainer;
			var tempOffset = newRange.startOffset;
			newRange.setStart(newRange.endContainer, newRange.endOffset);
			newRange.setEnd(temp, tempOffset);
		}

		// Also, switch around the offsets if the ends refer to the same node, 
		// but the offsets are in the wrong order
		if (newRange.startContainer === newRange.endContainer) {
			if (newRange.startOffset > newRange.endOffset) {
				var temp = newRange.startOffset;
				newRange.setStart(newRange.startContainer, newRange.endOffset);
				newRange.setEnd(newRange.endContainer, temp);
			}
		}
	}
	return newRange;
}

/**
 * Gets the range of the entire document.
 * 
 * @param range 
 */
function GetRangeToEntireDocument() {
	r = window.getSelection();
	r.selectAllChildren(document.body);
	range = document.createRange();
	range.setStart(r.anchorNode, r.anchorOffset);
	range.setEnd(r.focusNode, r.focusOffset);
	return range;
}

/*******************************************************************************
Element Navigation Functions
 *******************************************************************************/

/**
 * Copies all of the children in node and puts them in parent.
 * 
 * @param parent
 * @param node
 */
function InsertAllChildNodes(parent, node) {
	console.debug("InsertAllChildNodes()");
	var contents = node.cloneNode(true);

	var currentNode = contents.firstChild;

	while(currentNode !== null) {
		var nodeCopy = currentNode.cloneNode(true);
		parent.insertBefore(nodeCopy, node);
		currentNode = currentNode.nextSibling;
	}

	r = document.createRange();
	r.selectNode(parent);
	//console.debug('Contents inside parent: ' + GetHTMLSource(r));
}

/**
 * Gets the previous element, whether that is a text element or a normal 
 * element.
 * 
 * @param elem
 */
function PreviousElement(elem) {
	console.debug("PreviousElement()");
	var prev = elem.previousSibling;
	if (prev === null) {
		if (elem.parentNode === null) {
			return null;
		}
		else {
			elem = PreviousElement(elem.parentNode);
			return elem;
		}
	}
	else {
		return DeepestChild(prev, true);
	}
}

/**
 * Gets the next element, whether that is a text element or a normal element.
 * 
 * @param elem 
 */
function NextElement(elem) {
	//console.debug("NextElement()");
	var next = elem.nextSibling;
	if (next === null) {
		if (elem.parentNode === null) {
			return null;
		}
		else {
			elem = NextElement(elem.parentNode);
			return elem;
		}
	}
	else {
		return DeepestChild(next);
	}
}

/**
 * Gets the deepest child of the parent. Will get the first child by default, 
 * the last child if isLast is true.
 * 
 * @param parent
 * @param isLast
 */
function DeepestChild(parent, isLast) {
	//console.debug("DeepestChild()");
	isLast = typeof isLast !== 'undefined' ? isLast : false;

	if (parent.childNodes.length === 0) {
		return parent;
	}
	else {
		if (isLast) {
			var child = parent.lastChild;
			return DeepestChild(child, true);
		}
		else {
			var child = parent.firstChild;
			return DeepestChild(child);
		}
	}
}

/**
 * Gets the child index of the element in its parent.
 * 
 * @param elem
 */
function GetChildIndex(el) {
	console.debug('GetChildIndex()');
	var i = 0;
	var myElem = el.previousSibling;
	while (myElem !== null) {
		myElem = myElem.previousSibling;
		i++;
	}
	return i;
}

/**
 * Returns whether an element is in the client viewport. 
 * 
 * @param el
 */
function ElementInViewport(el) {
	//console.debug('ElementInViewport()');
	var top = el.offsetTop;
	var left = el.offsetLeft;
	var width = el.offsetWidth;
	var height = el.offsetHeight;

	while(el.offsetParent) {
		el = el.offsetParent;
		top += el.offsetTop;
		left += el.offsetLeft;
	}

	return (
			top >= window.pageYOffset &&
			left >= window.pageXOffset &&
			(top + height) <= (window.pageYOffset + window.innerHeight) &&
			(left + width) <= (window.pageXOffset + window.innerWidth)
	);
}

/**
 * Returns the equation node if node is inside an equation.
 * 
 * @param node 
 */
function GetEquation(node) {	
	//console.debug("GetEquation()");
	var myNode = node;

	// Check to see if this node is an equation
	if (myNode.className == "mathmlEquation") {
		return myNode;
	}

	while (myNode.parentNode !== null) {
		myNode = myNode.parentNode;

		// Check to see if it is an equation by checking its class
		if (myNode.className == "mathmlEquation") {
			return myNode;
		}
	}
	return null;
}

/**
 * Returns true or false depending on whether the node is inside of a math
 * equation or not.
 * 
 * @param node
 * @returns {Boolean}
 */
function IsInsideEquation(node) {
	var myNode = GetEquation(node);
	return myNode !== null;
}

/**
 * Gets the index and offset of the contents directly after the element that is 
 * going to be removed and replaced by its children.
 * 
 * @param elemRemove
 * @returns
 */
function CalculateIndexOffsetAfterRemoval(elemRemove) {
	var index = 0;
	var offset = 0;

	// This will depend on whether the element before the element to remove
	// is a text type or element type. It also depends on whether there was
	// anything at all.

	var elemLastChildIndex = 0;
	var elemLastChildOffset = 0;

	if (elemRemove.previousSibling === null) {
		// No previous sibling? Just get index and length of last child
		index = GetChildIndex(elemRemove.lastChild) + 1;
		offset = 0;
		if (elemRemove.lastChild.nodeType == Node.TEXT_NODE) {
			offset = elemRemove.lastChild.length;
			index = index - 1;
		}
		return {index: index, offset: offset};
	}
	else {
		// If it is a normal element, no node combining will be done. If it is
		// a text node, node combining may happen
		if (elemRemove.previousSibling.nodeType === Node.TEXT_NODE) {
			if (elemRemove.firstChild.nodeType === Node.TEXT_NODE) {
				index = GetChildIndex(elemRemove.previousSibling) + 1;
				offset = elemRemove.previousSibling.data.length + elemRemove.firstChild.data.length;
				if (IsChildrenJustText(elemRemove) === true) {
					index = index - 1;
				}
			}
			else {
				index = GetChildIndex(elemRemove.previousSibling) + GetChildIndex(elemRemove.lastChild) + 2;
				offset = 0;
				if (elemRemove.lastChild.nodeType === Node.TEXT_NODE) {
					offset = elemRemove.lastChild.data.length;
				}
			}
		}
		else {
			// Just a normal node, so no combining necessary at beginning
			index = GetChildIndex(elemRemove.previousSibling) + GetChildIndex(elemRemove.lastChild) + 2;
			offset = 0;
			if (elemRemove.lastChild.nodeType === Node.TEXT_NODE) {
				offset = elemRemove.lastChild.data.length;
			}
		}
	}

	return {index: index, offset: offset};
}

/**
 * Returns whether the elem only has 1 text child node.
 * 
 * @param elem
 * @returns {Boolean}
 */
function IsChildrenJustText(elem) {
	if ($(elem).contents().length === 1) {
		if (elem.firstChild.nodeType == Node.TEXT_NODE) {
			return true;
		}
	}
	return false;
}