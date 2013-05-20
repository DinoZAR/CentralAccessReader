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
	element_to_scroll_to = document.getElementById(anchorName);
	$.scrollTo(element_to_scroll_to, {duration: 200});
}

function ScrollToHighlight() {
	if (highlightLine != null) {
		$.scrollTo(highlightLine.parentNode, {duration: 1000, offset: {top: -120}});
	}
	else {
		$.scrollTo(highlight.parentNode, {duration: 1000, offset: {top: -120}});
	}
}

// ---------------------------------------------------------------------------
// HIGHLIGHTING FUNCTIONS
// ---------------------------------------------------------------------------
var highlight; // The highlighter element that has the highlighted content.
var highlightLine; // The highlighter element that has the whole line that will be highlighted
var lastElement;
var beginOffset;

// Sets the beginning to start the speech. It will start at beginning if no selection was made.
function SetBeginning(doLine, elementType) {
	console.debug("SetBeginning()");
	var range = window.getSelection();
	if (!(range === null)) {
		
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
	}
	else {
		// Get the first deepest child in the document and go from there
		range = document.createRange();
		range.selectNode(DeepestChild(document.body.firstChild));
		range.startOffset = 0;
		range.endOffset = 1;
	}
	
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
		console.debug("Highlight node: " + highlight.toString());
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
function GetNextWord(node, offset, type) {
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
	else if (node.nodeName == "#text"){
		range = document.createRange();
		
		console.debug("Content: <start>" + node.data + "<end><offset>" + offset.toString() + "<length>" + node.data.length.toString());
		
		// Adjust end if they exceed the length of the data
		if ((offset + 1) >= node.data.length) {
			range.setStart(node, node.data.length - 1);
			range.setEnd(node, node.data.length);
			needToGoToNext = true;
		}
		else {
			range.setStart(node, offset);
			range.setEnd(node, offset + 1);
		}
		
		return [range, needToGoToNext, false];
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

function DeepestChild(parent) {
	if (parent.childNodes.length == 0) {
		return parent;
	}
	else {
		var child = parent.firstChild;
		return DeepestChild(child);
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