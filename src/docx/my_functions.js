// Used in page navigation to move to an anchor point with specific id
function GotoPageAnchor(anchorName) {
	element_to_scroll_tasdo = document.getElementById(anchorName);
	element_to_scroll_to.scrollIntoView();
}

// ---------------------------------------------------------------------------
// HIGHLIGHTING FUNCTIONS
// ---------------------------------------------------------------------------

var highlight; // The highlighter element that has the highlighted content.

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
	if (window.getSelection()) {
		var range = window.getSelection()
		var startNode = range.anchorNode;
		var offset = range.anchorOffset;
		
		// Check to see if the start is inside a math equation. If so, adjust selection to
		// only select that node. Otherwise, have it select the first whole word there.
		var equation = GetEquation(startNode);
		if (equation === null) {
			range = GetNextWord(startNode, offset);
			
			// If I can't get another word, get another element.
			if (range == null) {
				var nElem = NextElement(startNode);
				range = document.createRange();
			}
			SetHighlight(range);

			// Clear the user selection
			window.getSelection().collapseToStart();
		}
		else {
			range = document.createRange();
			range.selectNode(equation);
			SetHighlight(range);
		}
	}
}

// Move the highlight to the next element that should be highlighted 
function HighlightNextElement() {
	
	var s = highlight.nextSibling;
	
	if (s != null) {
		
		var range = GetNextWord(s, 0);
		if (range == null) {
			alert("I got no more words!");
			
			// I had to do this twice because the first is an empty #text element
			s = highlight.nextSibling;
			s = s.nextSibling;
			alert("New sibling: " + s.nodeName + " " + s.textContent);
		} 
		else {
			SetHighlight(range);
		}
	}
	else {
		alert("No sibling...");
	}
}

// Returns the range of equation if node is inside an equation.
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
	
	// Check to see if I can find the start of the next word. Otherwise, return null.
	var nextIndex = node.textContent.substring(offset).search(/\w/);
	if (nextIndex == -1) {
		return null;
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

// Clears the highlight of where it was before.
function ClearHighlight() {
	// Get the contents that I am going to replace the node with
	var contents = highlight.cloneNode(true);

	// Replace the highlight node with my contents
	var p = highlight.parentNode;
	
	// Insert everything in the contents before the highlight position
	for  (i = 0; i < contents.childNodes.length; i++) {
		p.insertBefore(contents.childNodes[i], highlight);
	}
	
	// Cleanup the highlight and its reference
	p.removeChild(highlight);
	highlight = null;
}

// Given a Range object, this will clean up any previous highlight and create a highlight
// over the new range
function SetHighlight(range) {
	
	if (highlight != null) {
		ClearHighlight();
	}
	
	highlight = document.createElement("span");
	highlight.setAttribute("id", "npaHighlight");

	var contents = range.extractContents();
	highlight.appendChild(contents);
	
	range.insertNode(highlight);
}

// --------------------------------------------------------------------------------------------------
// GENERAL UTILITY FUNCTIONS
// --------------------------------------------------------------------------------------------------

function NextElement(elem) {
	var next = elem.nextSibling;
	while (next && next.nodeType != 1) {
		next = next.nextSibling;
	}
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
		return next;
	}
}

function GetChildIndex(elem) {
	var i = 0;
	while ((elem = elem.previousSibling) != null) {
		i++;
	}
	return i;
}