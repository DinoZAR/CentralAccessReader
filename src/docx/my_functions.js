// Have tooltips pop up anytime there is an image with a tooltip
$(function() {
    $( document ).tooltip({
      position: {
        my: "center top+20",
        at: "center bottom",
        using: function( position, feedback ) {
          $( this ).css( position );
          $( "<div>" )
            .addClass( "arrow" )
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
// -----------------------------------------------------------------------------
// HIGHLIGHTING FUNCTIONS AND STATE DATA
// -----------------------------------------------------------------------------

var highlight; // The highlighter element that has the highlighted content.
var highlightLine; // The highlighter element that has the whole line that will be highlighted
var beginOffset;
var atBeginning = false;

// -----------------------------------------------------------------------------
// END STATE DATA
// -----------------------------------------------------------------------------
// Sets the beginning to start the speech. It will start at beginning if no selection was made.
function SetBeginning(doLine) {
	console.debug("SetBeginning");	
	// Get a range of the selection first
	var range = window.getSelection();
	if (!(range === null)) {		
		console.debug("Something got selected! Range: " + range.toString());
		
		range = window.getSelection();
		
		if (range.anchorNode.compareDocumentPosition(range.focusNode) & Node.DOCUMENT_POSITION_PRECEDING) {
			var newRange = document.createRange();
			newRange.setStart(range.focusNode, range.focusOffset);
			newRange.setEnd(range.anchorNode, range.anchorOffset);
			console.debug("New range being modified!" + newRange.toString());
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
		console.debug("Nothing was selected!");
		// Get the first deepest child in the document and go from there
		range = document.createRange();
		range.selectNode(DeepestChild(document.body.firstChild));
	}
	
	// Set some of my states
	beginOffset = range.startOffset;
	atBeginning = true;
	
	// Check to see if the start is inside a math equation. If so, adjust selection to
	// only select that node. Otherwise, have it select the first whole word there.
	range = SelectWord(range.startContainer, range.startOffset, 1);
	// If I can't get another word, get another element.
	if (range == null) {
		var nElem = NextElement(startNode);
		range = document.createRange();
	}
	
	// Set the highlight there
	SetHighlight(range, doLine);
	
	// Clear the user selection, if any
	window.getSelection().empty();
}

// Highlight a word in the current element. The JavaScript keeps track of the
// beginning offset, since it doesn't expect the TTS calling this to know that.
function HighlightWord(doLine, offset, length) {
	var start = offset;
	if (atBeginning == True) {
		start += beginOffset;
	}
	var end = start + length;
}

// Move the highlight to the next element that should be highlighted 
function HighlightNextElement(doLine) {
	console.debug("HighlightNextElement");
	// Get the sibling of the highlight node. It will either be more text or an actual element.
	ClearLineHighlight();
	var next = NextElement(highlight);
	var range = GetNextWord(next, 0);
	// Check to see if I actually have something coming up. Otherwise, just
	// clear all the highlights
	if (range == null) {
		ClearAllHighlights();
	}
	else {
		SetHighlight(range, doLine);
	}
	
	// Scroll to the element containing the highlight
	if (ElementInViewport(highlight) != true) {
		$(this).scrollTo(highlight.parentNode, {duration: 1000, offset: {top: -120}});
	}
}
// Returns the equation node if node is inside an equation.
function GetEquation(node) {	
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
// Returns a range that has the next word (or element if not word)
function SelectWord(node, offset, length) {
	console.debug("SelectWord");
	// See if it is an equation
	var equation = GetEquation(node);
	if (equation != null) {
		console.debug("It is an equation!");
		var range = document.createRange();
		range.selectNode(equation);
		atBeginning = false;
		return range;
	}
	// See if it is an image
	if (node.nodeName == "IMG") {
		console.debug("It is an image!");
		var range = document.createRange();
		range.selectNode(node);
		atBeginning = false;
		return range;
	}
	// If it is anything else, it is probably text
	else {
		
		var nextIndex = offset;
		if (atBeginning == true) {
			nextIndex += beginOffset
		}
		var endIndex = offset + length;
		
		range = document.createRange();
		range.setStart(node, nextIndex);
		range.setEnd(node, endIndex);
		
		return range;
	}
}
// Clears the highlight of where it was before.
function ClearHighlight() {
	console.debug("ClearHighlight");
	// Replace the highlight node with my contents
	var p = highlight.parentNode;
	InsertAllChildNodes(p, highlight);
	// Cleanup the highlight and its reference
	p.removeChild(highlight);
	p.normalize();
	highlight = null;
}
// Clears the line highlight
function ClearLineHighlight() {
	console.debug("ClearLineHighlight");
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
	console.debug("ClearAllHighlights");
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
	// Adjust beginning of range so that it arrives at the end of previous sentence, or just 
	// the beginning of the first child node.
	var startNode = highlight;
	var startOffset = 0;
	var done = false;
	while (!done) {
		if (startNode.nodeName == "#text") {
			console.debug("Searching inside text node...");
			var lastEnd = -1;
			var patt = /[.!\?]\s/g;
			while (patt.test(startNode.textContent) == true) {
				lastEnd = patt.lastIndex;
			}
			if (lastEnd == -1) {
				console.debug("Couldn't find end of last sentence!");
				// Check if there are more nodes before this
				var prev = startNode.previousSibling;
				if (prev != null) {
					startNode = prev;
					startOffset = 0;
				}
				else {
					done = true;
				}
			}
			else {
				console.debug("Got an end of last sentence! " + lastEnd.toString());
				startOffset = lastEnd - 1;  // Subtracting 1 to ignore the space
				done = true;
			}
		}
		else {
			var prev = startNode.previousSibling;
			if (prev != null) {
				startNode = prev;
				startOffset = 0;
			}
			else {
				done = true;
			}
		}
	}
	console.debug("Start Node: " + startNode.nodeName + " Start Offset: " + startOffset.toString());
	// Set the end index
	// Adjust beginning of range so that it arrives at the end of previous sentence, or just 
	// the beginning of the first child node.
	var endNode = highlight;
	var endOffset = 0;
	done = false;
	while (!done) {
		if (endNode.nodeName == "#text") {
			console.debug("Searching inside text node...");
			var lastEnd = -1;
			var patt = /[.!\?]\s/g;
			if (patt.test(endNode.textContent) == true) {
				lastEnd = patt.lastIndex;
			}
			if (lastEnd == -1) {
				console.debug("Couldn't find end of next sentence!");
				// Check if there are more nodes before this
				var next = endNode.nextSibling;
				if (next != null) {
					endNode = next;
					endOffset = 0;
				}
				else {
					endOffset = endNode.textContent.length;
					done = true;
				}
			}
			else {
				console.debug("Got an end of next sentence! " + lastEnd.toString());
				endOffset = lastEnd;
				done = true;
			}
		}
		else if ((endNode.nodeName == "SPAN") && (endNode.getAttribute("id") == "npaHighlight")) {
			// Check if there is some punctuation mark at the end inside of the node
			// and there is another sibling after this node. If so, make the highlight
			// stop at the beginning of the next sibling.
			var punctPatt = /[.!\?]/g;
			if ((endNode.lastChild.nodeName == "#text") && (endNode.nextSibling != null)){
				var lastPunct = -1;
				while (punctPatt.test(endNode.lastChild.nodeValue) == true) {
					lastPunct = punctPatt.lastIndex;
				}
				if (lastPunct == endNode.lastChild.nodeValue.length) {	
					endNode = endNode.nextSibling;
					endOffset = 0;
					done = true;
				}
				else {
					console.debug("Test failed...." + lastPunct.toString() + ' != ' + (endNode.lastChild.nodeValue.length - 1).toString());
					console.debug(endNode.lastChild.nodeValue);
					endNode = endNode.nextSibling;
					endOffset = 0;
				}
			}
			else {
				var next = endNode.nextSibling;
				if (next != null) {
					endNode = next;
					endOffset = 0;
				}
				else {
					endOffset = 0;
					done = true;
				}
			}
		}
		else {
			var next = endNode.nextSibling;
			if (next != null) {
				endNode = next;
				endOffset = 0;
			}
			else {
				endOffset = 0;
				done = true;
			}
		}
	}
	
	console.debug("End Node: " + endNode.nodeName + " End Offset: " + endOffset.toString());


	// Create the range for my highlighter line thing
	var range = document.createRange();
	range.setStart(startNode, startOffset);
	range.setEnd(endNode, endOffset);
	
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
	return i;
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