// Used in page navigation to move to an anchor point with specific id
function GotoPageAnchor(anchorName) {
	element_to_scroll_to = document.getElementById(anchorName);
	element_to_scroll_to.scrollIntoView();
}

// ---------------------------------------------------------------------------
// HIGHLIGHTING FUNCTIONS
// ---------------------------------------------------------------------------

var highlight; // The highlighter element that has the highlighted content.
var highlightLine; // The highlighter element that has the whole line that will be highlighted

function PrintSelection() {
	if (window.getSelection()) {
		var range = window.getSelection();
		var buildString = "My Range!\n";
		buildString += "Anchor Node: " + range.anchorNode.parentNode.nodeName + " ";
		buildString += range.anchorOffset.toString() + "\n";
		buildString += "Focus Node: " + range.focusNode.parentNode.nodeName + " ";
		buildString += range.focusOffset.toString() + "\n";
		alert(buildString);
	}
}

// Sets the beginning to start the speech. It will start at beginning if no selection was made.
function SetBeginning() {

	console.debug("SetBeginning");

	if (window.getSelection()) {
		var range = window.getSelection()
		var startNode = range.anchorNode;
		var offset = range.anchorOffset;
		
		// Check to see if the start is inside a math equation. If so, adjust selection to
		// only select that node. Otherwise, have it select the first whole word there.
		range = GetNextWord(startNode, offset);
			
		// If I can't get another word, get another element.
		if (range == null) {
			var nElem = NextElement(startNode);
			range = document.createRange();
		}
		SetHighlight(range);

		window.getSelection().empty();
	}
}

// Move the highlight to the next element that should be highlighted 
function HighlightNextElement() {
	
	console.debug("HighlightNextElement");

	// Get the sibling of the highlight node. It will either be more text or an actual element.
	ClearLineHighlight();
	var next = highlight.nextSibling;
	
	if (next != null) {
		if (next.nodeName == "#text") {

			// Get the next word, if any.
			var range = GetNextWord(next, 0);
			if (range == null) {
				next = NextElement(next);
				range = GetNextWord(next, 0);
				SetHighlight(range);
			}
			else {
				SetHighlight(range);
			}
		}
		else {
			alert("In something else. Weird...");
			alert(next.nodeName);
		}
	}
	else {
		next = NextElement(highlight);
		var range = GetNextWord(next, 0);
		SetHighlight(range);
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

// Returns a range that has the next word
function GetNextWord(node, offset) {
	console.debug("GetNextWord");

	// See if it is an equation
	var equation = GetEquation(node);
	if (equation != null) {
		var range = document.createRange();
		range.selectNode(equation);
		return range;
	}

	// See if it is an image
	if (node.nodeName == "IMG") {
		console.debug("Got next image!");
		var range = document.createRange();
		range.selectNode(node);
		return range;
	}

	// See if it is anything else, like text
	else {
		// Check to see if I can find the start of the next word. Otherwise, return null.
		var nextIndex = node.textContent.substring(offset).search(/\w/);
		if (nextIndex == -1) {
			// If I can't find another word, try to find another element
			var elem = NextElement(node);
			if (elem == null) {
				return null;
			}
			else {
				return GetNextWord(elem, 0);
			}
		}
		nextIndex = nextIndex + offset;
	
		var endIndex = node.textContent.substring(nextIndex).search(/\s/);
		if (endIndex == -1) {
			endIndex = node.length; // Most likely reached the end of whatever element I was in.
		}
		else {
			endIndex = endIndex + nextIndex;
		}

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
	
	var p = highlightLine.parentNode;
	
	InsertAllChildNodes(p, highlightLine);

	p.removeChild(highlightLine);
	p.normalize();
	highlightLine = null;
}

// Given a Range object, this will clean up any previous highlight and create a highlight
// over the new range
function SetHighlight(range) {
	
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

	SetLineHighlight();
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
		else {
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

	for (i = 0; i < contents.childNodes.length; i++) {
		console.debug("Inserting node: " + contents.childNodes[i].nodeName);
		console.debug(contents.childNodes[i].textContent);
		parent.insertBefore(contents.childNodes[i], node);
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