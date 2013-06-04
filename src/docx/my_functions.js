var highlight = null; // The highlighter element that has the highlighted content.
var highlightLine = null; // The highlighter element that has the whole line that will be highlighted
var lastElement = null;
var beginOffset = 0;
var lastHeadingElement = null;
var startFromHeading = false;
var lastSearchElement = null;
var lastSearchOffset = 0;
var startFromSearch = false;

// ---------------------------------------------------------------------------
// GENERAL FUNCTIONS
// ---------------------------------------------------------------------------

// Have tooltips pop up anytime there is an image with a tooltip
$(function() {
    $( document ).tooltip({
      position: {
        my: "center top+20",
        at: "center bottom",
        using: function( position, feedback ) {
          $( this ).css( position );
          $( "<div>" )
            .addClass( feedback.vertical )
            .addClass( feedback.horizontal )
            .appendTo( this );
        }
      },
      hide: false,
      show: false
    });
  });

// Used in page navigation to move to an anchor point with specific id
function GotoPageAnchor(anchorName) {
	console.debug("GotoPageAnchor()");
	element_to_scroll_to = document.getElementById(anchorName);
	startFromHeading = true;
	lastHeadingElement = element_to_scroll_to;
	$.scrollTo(element_to_scroll_to, {duration: 200});
}

// Scrolls the view to where the highlight is
function ScrollToHighlight(isInstant) {
	isInstant = typeof isInstant !== 'undefined' ? isInstant : false;
	
	var myDuration = 800;
	if (isInstant) {
		myDuration = 0;
	}
	if (highlightLine != null) {
		$.scrollTo(highlightLine.parentNode, {duration: myDuration, offset: {top: -120}});
	}
	else {
		$.scrollTo(highlight.parentNode, {duration: myDuration, offset: {top: -120}});
	}
}

// Finds the next search term, highlights it, and moves the view to it, if any.
// If after is true, it will find word after current. Otherwise, search for text before.
// Returns true if it found something, false if it didn't
function SearchForText(myText, after) {
	console.debug('SearchForText()');
	if (after) {
		return SearchTextForward(myText);
	}
	else {
		return SearchTextBackward(myText);
	}
}

function SearchTextBackward(myText) {
	var currentNode = null;
	if (!(highlight === null)) {
		currentNode = PreviousElement(highlight);
	}
	else {
		currentNode = document.body.lastChild;
	}
	
	while (true) {
		if (currentNode.nodeType == 3) {
			var lastIndex = -1;
			var first = true;
			var index = 1000;
			currentSearch = currentNode.data.toLowerCase();
			while (index >= 0) {
				index = currentSearch.indexOf(myText);
				if (index >= 0) {
					if (first) {
						lastIndex = index;
						first = false;
					}
					else {
						lastIndex += index + myText.length;
					}
					currentSearch = currentSearch.substring(index + myText.length);
				}
			}
			if (lastIndex >= 0) {
				// Get the highlight to surround what I found
				var range = document.createRange();
				lastSearchElement = currentNode;
				lastSearchOffset = lastIndex;
				startFromSearch = true;
				range.setStart(currentNode, lastIndex);
				range.setEnd(currentNode, lastIndex + myText.length);
				SetHighlight(range, false);
				ScrollToHighlight(true);
				return true;
			}
		}
		currentNode = PreviousElement(currentNode);
		if (currentNode === null) {
			return false;
		}
	}
}

function SearchTextForward(myText) {
	// Determing the starting point
	var currentNode = null;
	if (!(highlight === null)) {
		currentNode = NextElement(highlight);
	}
	else {
		currentNode = document.body.firstChild;
	}
	
	while (true) {
		if (currentNode.nodeType == 3) {
			var index = currentNode.data.toLowerCase().indexOf(myText);
			if (index >= 0) {
				// Get the highlight to surround what I found
				var range = document.createRange();
				lastSearchElement = DeepestChild(currentNode);
				lastSearchOffset = index;
				startFromSearch = true;
				range.setStart(currentNode, index);
				range.setEnd(currentNode, index + myText.length);
				SetHighlight(range, false);
				ScrollToHighlight(true);
				return true;
			}
		}
		currentNode = NextElement(currentNode);
		if (currentNode === null) {
			return false;
		}
	}
}

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
		
		if (range.anchorNode.compareDocumentPosition(range.focusNode) & Node.DOCUMENT_POSITION_PRECEDING) {
			var newRange = document.createRange();
			newRange.setStart(range.focusNode, range.focusOffset);
			newRange.setEnd(range.anchorNode, range.anchorOffset);
			range = newRange;
		}
		else {
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
			}
			else {
				var newRange = document.createRange();
				newRange.setStart(range.anchorNode, range.anchorOffset);
				newRange.setEnd(range.focusNode, range.focusOffset);
				range = newRange;
			}
		}
		
		// If I have a paragraph with no text, move the range to the next element
		if ((range.startContainer.nodeName == 'P') && ($(range.startContainer).text() == '')) {
			range.setStart(NextElement(range.startContainer), 0);
		}
	}
	else {
		// Start from the heading, if applicable
		if (startFromHeading == true) {
			console.debug('Starting from heading...');
			range = document.createRange();
			range.selectNodeContents(DeepestChild(lastHeadingElement))
			range.startOffset = 0;
		}
		// Start from highlight, if it was a search or something
		// Just a little too buggy right now
		//else if (startFromSearch == true) {
		//	console.debug('Start from last search...');
		//	ClearAllHighlights();
		//	range = document.createRange();
		//	console.debug('- The text from search: ' + lastSearchElement.data.toString());
		//	console.debug('- Parent: ' + lastSearchElement.parentNode.nodeName);
		//	range.setStart(lastSearchElement, lastSearchOffset);
		//}
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
		range.setEnd(document.body.lastChild, document.body.lastChild.length);
	}
	
	return range;
}

// Gets the HTML content of my selection and returns it
function GetSelectionHTML() {
	console.debug("GetSelectionHTML()");
	var range = GetSelectionRange();
	return GetHTMLSource(range);
}

// Takes a Range object and extracts the HTML content
function GetHTMLSource(range) {
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
function HighlightWord(doLine, offset, length) {
	console.debug("HighlightWord()");
	
	// Get the parent element from the highlight from which we do these calculations
	var p = null;
	var childNum = 0;
	if (!(highlightLine == null)) {
		p = highlightLine.parentNode;
		childNum = GetChildIndex(highlightLine);
	}
	else {
		p = highlight.parentNode;
		childNum = GetChildIndex(highlight);
	}
	
	// Get rid of highlights
	ClearAllHighlights();
	
	// Get the text content of the child I want
	var t = $(p).contents()[childNum];
	
	// Create range and select that text correctly
	var range = document.createRange();
	range.setStart(t, offset + beginOffset);
	range.setEnd(t, offset + length + beginOffset);
	
	// Create the highlight
	SetHighlight(range, doLine);
}

// Returns the equation node if node is inside an equation.
function GetEquation(node) {	
	console.debug("GetEquation()");
	var myNode = node

	// Check to see if this node is an equation
	if (myNode.className == "mathmlEquation") {
		return myNode;
	}

	while (myNode.parentNode != null) {
		myNode = myNode.parentNode

		// Check to see if it is an equation by checking its class
		if (myNode.className == "mathmlEquation") {
			return myNode;
		}
	}
	return null;
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
	if (node.nodeName == "IMG") {
		var range = document.createRange();
		range.selectNode(node);
		return [range, needToGoToNext, true];
	}

	// See if it is anything else, like text
	if (node.nodeName == "#text"){
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
		range.selectNode(node);
		return [range, needToGoToNext, false]
	}
}

// Clears the highlight of where it was before.
function ClearHighlight() {
	console.debug("ClearHighlight()");
	// Replace the highlight node with my contents
	var p = highlight.parentNode;

	InsertAllChildNodes(p, highlight);

	// Cleanup the highlight and its reference
	p.normalize();
	p.removeChild(highlight);
	p.normalize();
	highlight = null;
}

// Clears the line highlight
function ClearLineHighlight() {
	console.debug("ClearLineHighlight()");
	if (highlightLine != null) {

		var p = highlightLine.parentNode;

		InsertAllChildNodes(p, highlightLine);

		// Recapture my highlight element reference
		highlight = document.getElementById("npaHighlight");

		p.normalize();
		p.removeChild(highlightLine);
		p.normalize();
		highlightLine = null;
	}

}

// Clears both the line highlight and the individual element highlight
function ClearAllHighlights() {

	if (highlightLine != null) {
		ClearLineHighlight();
	}

	if (highlight != null) {
		ClearHighlight(); 
	}

}

// Given a Range object, this will clean up any previous highlight and create a highlight
// over the new range
function SetHighlight(range, doLine) {

	if (highlight != null) {
		ClearHighlight();
	}

	if (highlightLine != null) {
		ClearLineHighlight();
	}

	highlight = document.createElement("span");
	highlight.setAttribute("id", "npaHighlight");

	var contents = range.extractContents();
	highlight.appendChild(contents);

	range.insertNode(highlight);

	if (doLine == true) {
		SetLineHighlight();
	}
}

// This function will set the line highlight to surround that particular range.
// It will highlight all the way to the previous sentence end to the next
// sentence end, or just the node if there are no sentences.
function SetLineHighlight() {

	highlightLine = document.createElement("span");
	highlightLine.setAttribute("id", "npaHighlightLine");

	// Start my range where my highlight is
	var range = document.createRange()
	range.selectNode(highlight);
	
	// If I have text in text highlight, do shifting. Otherwise, don't do anything
	if (highlight.firstChild.nodeName == "#text") {
		if (!(highlight.previousSibling === null)) {
			if (highlight.previousSibling.nodeName == "#text") {
				var endSentenceRegex = /[!?.][\s]/g
				var t = highlight.previousSibling.data;
				var start = -1;
				var m;
				while ((m = endSentenceRegex.exec(t)) != null) {
					start = m.index + 2;
				}
				if (start == -1) {
					start = 0;
				}
				range.setStart(highlight.previousSibling, start);
			}
		}
		if (!(highlight.nextSibling === null)) {
			if (highlight.nextSibling.nodeName == "#text") {
				var endSentenceRegex = /[!?.][\s]/g
				var t = highlight.nextSibling.data;
				var end = -1;
				var m = endSentenceRegex.exec(t);
				if (m != null) {
					end = m.index + 1;
				}
				if (end == -1) {
					end = highlight.nextSibling.data.length;
				}
				range.setEnd(highlight.nextSibling, end);
			}
		}
	}

	// Create the range for my highlighter line thing
	//var range = document.createRange();
	//range.setStart(startNode, startOffset);
	//range.setEnd(endNode, endOffset);
	
	var contents = range.extractContents();
	highlightLine.appendChild(contents);
	range.insertNode(highlightLine);
}

// --------------------------------------------------------------------------------------------------
// GENERAL UTILITY FUNCTIONS
// --------------------------------------------------------------------------------------------------

function InsertAllChildNodes(parent, node) {
	var contents = node.cloneNode(true);
	
	var currentNode = contents.firstChild;
	
	while(currentNode != null) {
		var nodeCopy = currentNode.cloneNode(true);
		parent.insertBefore(nodeCopy, node);
		currentNode = currentNode.nextSibling;
	}
}

// Gets the previous element, whether that is a text element or a normal element.
function PreviousElement(elem) {
	var prev = elem.previousSibling;
	if (prev == null) {
		if (elem.parentNode == null) {
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

// Gets the next element, whether that is a text element or a normal element.
function NextElement(elem) {
	var next = elem.nextSibling;
	if (next == null) {
		if (elem.parentNode == null) {
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

function DeepestChild(parent, isLast) {
	isLast = typeof isLast !== 'undefined' ? isLast : false;
	
	if (parent.childNodes.length == 0) {
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

function GetChildIndex(elem) {
	var i = 0;
	while ((elem = elem.previousSibling) != null) {
		i++;
	}
	return i-1;
}

function ElementInViewport(el) {
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