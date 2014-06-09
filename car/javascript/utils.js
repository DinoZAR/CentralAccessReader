/*
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
	//console.debug('GetSelectionRange()');
	var range = ConvertUserSelectionToRange();

	// Check if I have don't have a user selection.
	if (range.collapsed) {
		
		if (highlight !== null) {
			
			// Make a range that starts from the highlighter/cursor
			var parent = highlight.parentNode;
			
			if (highlight.previousSibling !== null) {
			
				if (highlight.previousSibling.nodeType === Node.TEXT_NODE) {
					var elem = highlight.previousSibling;
					var startOffset = elem.length;
					var startIndex = GetChildIndex(elem);
					
					ClearHighlight();
					
					elem = $(parent).contents()[startIndex];
					range.setStart(elem, startOffset);
					range.setEndAfter(parent.lastChild);
				}
				else {
					var index = GetChildIndex(highlight);
					ClearHighlight();
					range.selectNode($(parent).contents()[index]);
				}
			}
			else {
				ClearHighlight();
				range.selectNode(DeepestChild(parent));
			}
		}
		
		else {
			
			if (mySelectionRange !== null) {
				range = mySelectionRange;
			}
			else {
				// Select the entire document and start at beginning
				range = GetRangeToEntireDocument();
			}
		}
	}
	else {		
		// Start from the user selection. Do some random fixes to it
		ClearAllHighlights();
		MoveRangeAfterWhitespace(range);
		MoveRangeStartToDeepestInBody(range);
		SurroundMathEquation(range);
		MoveRangeOverEmptyParagraph(range);
	}

	ClearAllHighlights();
	
	mySelectionRange = range;

	return range;
}

/**
 * Gets the HTML content of my selection and returns it. 
 */
function GetSelectionHTML() {
	//console.debug("GetSelectionHTML()");
	var range = GetSelectionRange();
	return GetHTMLSource(range);
}

/**
 * Gets the HTML content of the body.
 * @returns
 */
function GetBodyHTML() {
	var range = document.createRange();
	range.selectNode(document.body);
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
	var div = document.createElement('div');
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
		sub = sub.substring(range.startOffset);
		var result = whitespaceRegex.exec(sub);
		if (result !== null) {
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
		myNode = DeepestChild(document.body.childNodes[range.startOffset], false);
		range.setStart(myNode, 0);
	}
}

/**
 * If the start or end of the range is inside of an equation, adjust them to the
 * start or end of the equation span respectively.
 * 
 * @param range
 */
function SurroundMathEquation(range) {
	
	if (IsInsideEquation(range.startContainer) === true) {
		var startEq = GetEquation(range.startContainer);
		range.setStart(startEq, 0);
	}
	if (IsInsideEquation(range.endContainer) === true) {
		var endEq = GetEquation(range.endContainer);
		range.setEnd(NextElement(endEq), 0);
	}
}

/**
 * If the start is a paragraph with nothing it, move to the next element.
 * 
 * @param range 
 */
function MoveRangeOverEmptyParagraph(range) {
	if ((range.startContainer.nodeName == 'P') && !(range.startContainer.hasChildNodes())) {
		range.setStart(NextElement(range.startContainer), 0);
	}
}

/**
 * Sets the user selection to the range given.
 * 
 * @param range 
 */
function SetUserSelection(newRange) {
	//console.debug('SetUserSelection()');
	newRange.startOffset = 0;
	
	var sel = window.getSelection();
	sel.removeAllRanges();
	sel.addRange(newRange);
}

/**
 * Converts a user selection to a Range object. This is NOT a SelectionRange 
 * object.
 */
function ConvertUserSelectionToRange() {
	var range = window.getSelection();
	var newRange = document.createRange();
	if (range.isCollapsed !== true) {
		var newRange = range.getRangeAt(0);
	}
	ClearUserSelection();
	return newRange;
}

/**
 * Gets the range of the entire document.
 * 
 * @param range 
 */
function GetRangeToEntireDocument() {
	//console.debug('GetRangeToEntireDocument()');
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
	//console.debug("InsertAllChildNodes()");
	var contents = node.cloneNode(true);

	var currentNode = contents.firstChild;

	while(currentNode !== null) {
		var nodeCopy = currentNode.cloneNode(true);
		parent.insertBefore(nodeCopy, node);
		currentNode = currentNode.nextSibling;
	}

	r = document.createRange();
	r.selectNode(parent);
}

/**
 * Gets the previous element, whether that is a text element or a normal 
 * element.
 * 
 * @param elem
 */
function PreviousElement(elem) {
	//console.debug("PreviousElement()");
	var prev = elem.previousSibling;
	if (prev === null) {
		if (elem.parentNode === null) {
			return null;
		}
		else {
			if (elem.parentNode.nodeName === 'BODY') {
				return null;
			}
			else {
				//elem = PreviousElement(elem.parentNode);
				//return elem;
				return elem.parentNode;
			}
		}
	}
	else {
		return DeepestChild(prev, true);
	}
}

/**
 * Get the previous element, except that it will take the first child of the
 * previous parent instead of the last.
 * 
 * @param elem
 */
function PreviousElementFirstChild(elem) {
	//console.debug("PreviousElementFirstChild()");
	var prev = elem.previousSibling;
	if (prev === null) {
		if (elem.parentNode === null) {
			return null;
		}
		else {
			if (elem.parentNode.nodeName === 'BODY') {
				return null;
			}
			else {
				//elem = PreviousElement(elem.parentNode);
				//return elem;
				return elem.parentNode;
			}
		}
	}
	else {
		return DeepestChild(prev);
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
 * Gets the previous occurrence of $sel from $elemSel. Both parameters are
 * JQuery objects. Returns an Element object.
 * @param $elemSel
 * @param $sel
 * @returns
 */
function GetPreviousOccurrence($elemSel, $sel) {
	var elem = $elemSel[0];
	var prev = PreviousElement(elem);
	
	// Keep getting the previous until I get something that matches selector
	while (prev !== null) {
		if ($(prev).is($sel)) {
			break;
		}
		prev = PreviousElement(prev);
	}
	
	return prev;
}

/**
 * Gets the next occurrence of $sel from $elemSel. Both parameters are JQuery
 * objects. Returns an Element object.
 * @param $elemSel
 * @param $sel
 * @returns
 */
function GetNextOccurrence($elemSel, $sel) {
	var elem = $($elemSel)[0];
	var next = NextElement(elem.parentNode);
	
	// Keep getting the next until I get something that matches selector
	while (next !== null) {
		if ($(next).is($sel)) {
			break;
		}
		
		if (next.parentNode !== null) {
			if ($(next.parentNode).is($sel)) {
				next = next.parentNode;
				break;
			}
		}
		
		next = NextElement(next);
	}
	
	return next;
}

/**
 * Gets the next element after the current that matches the JQuery selector.
 * @param elem
 * @param nextSel
 * @returns
 */
function GetNext(elem, nextSel) {
	
	// Make this an iterative process so that it doesn't overflow the stack
	while (elem !== null) {
		
		// Change the current element. If it has a child, go to the
		// child. If it has a sibling, go to the sibling. If it has
		// a parent, go up and get the sibling of that parent. If
		// that sibling does not have a sibling, keep going up until
		// the parent doesn't exist.
		
		if (elem.firstChild !== null) {
			// First child
			elem = elem.firstChild;
		}
		else {
			// Next sibling
			if (elem.nextSibling !== null) {
				elem = elem.nextSibling;
			}
			else {
				// Sibling of parent
				var done = false;
				while (!done) {
					if (elem.parentNode === null) {
                        elem = null;
						done = true;
					}
					else {
						if (elem.parentNode.nextSibling !== null) {
							elem = elem.parentNode.nextSibling;
							done = true;	
						}
						else {
							elem = elem.parentNode;
						}
					}
				}
			}
		}
		
		// Now test the element to see if it matches
		if ($(elem).is(nextSel)) {
			return elem;
		}
	}
	
	// If I'm down here, it means I didn't find it
	return elem;
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
	//console.debug('GetChildIndex()');
	var i = 0;
	var myElem = el.previousSibling;
	while (myElem !== null) {
		myElem = myElem.previousSibling;
		i++;
	}
	return i;
}

/**
 * Returns whether an element is completely in the client viewport. 
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
 * Returns whether the element is or is inside the highlight node.
 * 
 * @param elem
 * @returns {Boolean}
 */
function IsInsideHighlight(elem) {
	var myNode = elem;

	// Check to see if this node is an equation
	if (myNode.id == "npaHighlightSelection") {
		return true;
	}

	while (myNode.parentNode !== null) {
		myNode = myNode.parentNode;

		// Check to see if it is an equation by checking its class
		if (myNode.id == "npaHighlightSelection") {
			return true;
		}
	}
	return false;
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
				index = index - 1;
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

/**
 * Retrieves the closest whole word in a string to the index. By default, a
 * word that wraps around the index is the closest. If there are no words in
 * the string, then it returns a range with equal start and end points.
 * 
 * The returned object is as follows:
 * {'word' : the word it found,
 *  'start' : start index of word in string,
 *  'end' : end index of word in string}
 * 
 * @param myString
 * @param startIndex
 * @returns {object}
 */
function GetWordRange(myString, startIndex) {

    var regex = /\b\w+\b/g;
    var m = null;
    
    // Pick the range that either intersects with the start index
    // or is the closest in distance.
    var start = 0,
        end = 0;
    
    while ((m = regex.exec(myString)) !== null) {
        start = regex.lastIndex - m[0].length;
        end = regex.lastIndex;
        if (regex.lastIndex > startIndex) {
            break;
        }
    }
    
    return {'word' : myString.substring(start, end),
            'start' : start,
            'end' : end};
}