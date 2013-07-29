var beginOffset = 0;
var lastHeadingElement = null;
var startFromHeading = false;
var lastSearchElement = null;
var lastSearchOffset = 0;
var startFromSearch = false;

// ---------------------------------------------------------------------------
// HIGHLIGHTING FUNCTIONS
// ---------------------------------------------------------------------------

// Returns a range that has the range of selection, whether that is the user or
// automatic
function GetSelectionRange() {
	console.debug('GetSelectionRange()');
	var range = window.getSelection();
    
	if (!range.isCollapsed) {
		range = window.getSelection();
		
		if (range.anchorNode.compareDocumentPosition(range.focusNode) && Node.DOCUMENT_POSITION_PRECEDING) {
			var newRange = document.createRange();
			
			var startNode = range.focusNode;
			var startOffset = range.focusOffset;
			var endNode = range.anchorNode;
			var endOffset = range.anchorOffset;
			
			// If the parent of the end node is the start node,
			// get the last child of the start and swap it with
			// the end node. Yea, it is that weird.
			if (startNode == range.anchorNode.parentNode) {
                console.debug('Swapping last child of start with end node.');
				swapNode = endNode;
				swapOffset = endOffset;
				endNode = DeepestChild(startNode, true);
				endOffset = endNode.length;
				startNode = swapNode;
				startOffset = swapOffset;
			}
			
			newRange.setStart(startNode, startOffset);
			newRange.setEnd(endNode, endOffset);
			range = newRange;
		}
		else {
			console.debug('Switching around the start and end nodes.');
			if (range.anchorNode === range.focusNode) {
				// Switch around the offsets if needed
				var newRange = document.createRange()
				if (range.anchorOffset > range.focusOffset) {
					newRange.setStart(range.anchorNode, range.focusOffset);
					newRange.setEnd(range.focusNode, range.anchorOffset);
				}
				else {
					newRange.setStart(range.anchorNode, range.anchorOffset);
					newRange.setEnd(range.focusNode, range.focusOffset);
				}
				range = newRange;
				//console.debug('Range here: ' + GetHTMLSource(range) + ' [start node: ' + range.startContainer.toString() + '] [end node: ' + range.endContainer.toString() + ']');
			}
			else {
				var newRange = document.createRange();
				newRange.setStart(range.anchorNode, range.anchorOffset);
				newRange.setEnd(range.focusNode, range.focusOffset);
				range = newRange;
				//console.debug('Range here: ' + GetHTMLSource(range) + ' [start node: ' + range.startContainer.toString() + '] [end node: ' + range.endContainer.toString() + ']');
			}
		}
		
		//console.debug('Range here: ' + GetHTMLSource(range) + ' [start node: ' + range.startContainer.toString() + '] [end node: ' + range.endContainer.toString() + ']');
		
		// Move start forward so that it removes the whitespace
		if ((range.startContainer.nodeName == '#text')) {
			console.debug('Checking #text node if it only has whitespace...');
			var whitespaceRegex = /\s+/g;
			var sub = range.startContainer.data;
			console.debug('Substring is: ' + sub);
			sub = sub.substring(range.startOffset);
			console.debug('Substring is: ' + sub);
			var result = whitespaceRegex.exec(sub);
			if (result != null) {
				console.debug('Skipping #text node with whitespace...');
				if (result.index == 0) {
					range.setStart(range.startContainer, whitespaceRegex.lastIndex + range.startOffset);
				}
			}
		}
		
		// If the start turns out to be the body, alter the start so that it points at the
		// deepest node in child that's referred to by the offset
		if (range.startContainer.nodeName == 'BODY') {
			console.debug('Moving start to deepest element in offset of body');
			myNode = DeepestChild(document.body.childNodes[range.startOffset], false);
			range.setStart(myNode, 0);
		}
		
		// If my range is inside of a math equation on both sides, then make the range
		// surround the math equation
		var startEq = GetEquation(range.startContainer);
		var endEq = GetEquation(range.endContainer);
		if ($(startEq).is($(endEq)) && (startEq != null)) {
			console.debug('Equation: ' + startEq.nodeName + ', class name: ' + startEq.className);
			range.selectNode(startEq);
			range.setStart(startEq, 0);
		}
		
		// If I am starting at a paragraph with absolutely nothing in it, move to the
		// next element
		if ((range.startContainer.nodeName == 'P') && !(range.startContainer.hasChildNodes())) {
			console.debug('Moving off of a completely empty paragraph');
			range.setStart(NextElement(range.startContainer), 0);
		}
		
		//console.debug('Range here: ' + GetHTMLSource(range));
	}
	else {
		// Start from the heading, if applicable
		if (startFromHeading == true) {
			console.debug('Starting from heading...');
			range = document.createRange();
			range.selectNodeContents(DeepestChild(lastHeadingElement))
			range.startOffset = 0;
		}
		else {
			// Get the first deepest child in the document and go from there
			range = window.getSelection();
			range.selectAllChildren(document.body);
			var newRange = document.createRange();
			newRange.setStart(range.focusNode, range.focusOffset);
			newRange.setEnd(range.anchorNode, range.anchorOffset);
			range = newRange;
		}
		beginOffset = lastSearchOffset;
		var lastElement = DeepestChild(document.body.lastChild, true);
		
		range.setEnd(lastElement, lastElement.length);
		
		console.debug('My last element: ' + lastElement.toString() + ', ' + $(lastElement).text());
		//console.debug('My selection range: ' + range.toString());
	}
	
	// Clear the highlighting in it, if any.
	// There would be if we did a search.
	ClearAllHighlights();
	
	// Reset the user selection around the range we constructed
	var sel = window.getSelection();
	sel.removeAllRanges();
	sel.addRange(range);
	
	return range;
}

// Gets the HTML content of my selection and returns it
function GetSelectionHTML() {
	console.debug("GetSelectionHTML()");
	var range = GetSelectionRange();
	return GetHTMLSource(range);
}

// Takes a Range object and extracts the HTML content as text
function GetHTMLSource(range) {
    //console.debug("GetHTMLSource()");
    var clonedSelection = range.cloneContents();
	div = document.createElement('div');
    div.appendChild(clonedSelection);
    return div.innerHTML;
}

// Sets the beginning to start the speech. It will start at beginning if no selection was made.
function SetBeginning(doLine, elementType) {
	console.debug("SetBeginning()");
	var range = GetSelectionRange();
	
	// Reset heading states
	startFromHeading = false;
	lastHeadingElement = null;
	
	// Reset search states
	startFromSearch = false;
	lastSearchElement = null;
	lastSearchOffset = 0;
	
	beginOffset = range.startOffset;
	
	//range.setEnd(range.startContainer, range.startOffset);
	
	// Check to see if the start is inside a math equation. If so, adjust selection to
	// only select that node. Otherwise, have it select the first whole word there.
	stuff = GetNextWord(range.startContainer, range.startOffset);
	range = stuff[0];
	var goToNext = stuff[1];
	var clearBeginOffset = stuff[2]
	
	if (clearBeginOffset == true) {
		beginOffset = 0;
	}
	
	SetHighlight(range, doLine);
	window.getSelection().empty();
	
	if (goToNext == true) {
		HighlightNextElement(doLine, elementType, elementType);
	}
	
	ScrollToHighlight();
}

// Move the highlight to the next element that should be highlighted 
function HighlightNextElement(doLine, elementType, lastElementType) {
	console.debug("HighlightNextElement()");
	// Clear the line highlight first to make this process easier
	ClearLineHighlight();
	
	var range = null;
	var next = null;
	
	if (elementType == "text") {
	
		// Keep getting the next text element until the parent has changed.
		var origParent = highlight.parentNode;
		next = NextElement(highlight);
		var done = false;
		while (done != true) {
			if (elementType == lastElementType) {
				if ((origParent != next.parentNode) && (next.nodeName == "#text")) {
					if ($.trim(next.data) == "") {
						console.debug("Encountered empty text. Skipping...");
						next = NextElement(next);
					}
					else {
						console.debug("Got unique parent and node stuff");
						done = true;
					}
				}
				else {
					next = NextElement(next);
				}
			}
			else if (next.nodeName == "#text") {
				console.debug("Got text!");
				if ($.trim(next.data) == "") {
					console.debug("Encountered empty text. Skipping...");
					next = NextElement(next);
				}
				else {
					done = true;
				}
			}
			else {
				console.debug("Nothing in the stuff...");
				next = NextElement(next);
			}
		}
		range = document.createRange()
		range.setStart(next, 0);
		range.setEnd(next, 1);
		console.debug("New next: " + next.toString());
		if (next.nodeName == "#text") {
			console.debug("Text!" + next.data + ", " + next.data.length.toString());
		}
	}
	else if (elementType == "image") {
		next = NextElement(highlight);
		while (next.nodeName != "IMG") {
			next = NextElement(next);
		}
		range = document.createRange();
		range.selectNode(next);
	}
	else if (elementType == "math") {
		next = NextElement(highlight);
		while (GetEquation(next) === null) {
			next = NextElement(next);
		}
		range = document.createRange();
		range.selectNode(GetEquation(next));
	}
	else {
		alert("The highlighter does not recognize the element type: " + elementType + ". The problem is in TTS driver.");
	}

	// Check to see if I actually have something coming up. Otherwise, just
	// clear all the highlights
	if (range == null) {
		ClearAllHighlights();
	}
	else {
		SetHighlight(range, doLine);
	}
	
	// Set the begin offset back to nothing
	beginOffset = 0;
	
	// Scroll to the element containing the highlight
	ScrollToHighlight();
}

// Highlights a word in the current element based on the offset and length from
// the TTS driver. This function will handle the offsets from the selection.
function HighlightWord(doLine, offset, length, word) {
	console.debug("HighlightWord()");
	
	// Get the parent element from the highlight from which we do these calculations
	var p = GetHighlightParent();
	var childNum = GetHighlightChildIndex();
	
	// Check to see if the text we want is in the parent. Otherwise, keep moving to
	// the next text element until we find it
	ClearAllHighlights();
	var t = $(p).contents()[childNum];
	
	console.debug('t: ' + t.data.toString());
	console.debug('word: ' + word);
	
	while (t.data.indexOf(word) < 0) {
		// Generate a highlight 
		var range = document.createRange();
		range.selectNode($(p).contents()[childNum]);
		SetHighlight(range, doLine);
		
		HighlightNextElement(doLine, 'text', 'text');
		p = GetHighlightParent();
		childNum = GetHighlightChildIndex();
		ClearAllHighlights();
		t = $(p).contents()[childNum];
	}
	
	// Create range and select that text correctly
	var range = document.createRange();
	range.setStart(t, offset + beginOffset);
	range.setEnd(t, offset + length + beginOffset);
	
	// Create the highlight
	SetHighlight(range, doLine);
}

// Returns a range that has the next word or element
function GetNextWord(node, offset) {
	console.debug("GetNextWord()");
	var needToGoToNext = false;
	
	// See if it is an equation
	var equation = GetEquation(node);
	if (equation != null) {
		var range = document.createRange();
		range.selectNode(equation);
		return [range, needToGoToNext, true];
	}

	// See if it is an image
	else if (node.nodeName == "IMG") {
		var range = document.createRange();
		range.selectNode(node);
		return [range, needToGoToNext, true];
	}

	// See if it is anything else, like text
	else if (node.nodeName == "#text"){
		range = document.createRange();
		
		console.debug("Content: <start>" + node.data + "<end><offset>" + offset.toString() + "<length>" + node.data.length.toString());
		
		// Adjust end if they exceed the length of the data
		if ((offset + 1) >= node.data.length) {
			if (node.data.length > 0) {
				range.setStart(node, node.data.length - 1);
			}
			range.setEnd(node, node.data.length);
			needToGoToNext = true;
		}
		else {
			range.setStart(node, offset);
			range.setEnd(node, offset + 1);
		}
		
		return [range, needToGoToNext, false];
	}
	else {
		var range = document.createRange();
		range.selectNode(DeepestChild(node, false));
		return [range, needToGoToNext, false]
	}
}