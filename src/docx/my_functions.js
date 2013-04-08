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
	
	// Get the sibling of the highlight node. It will either be more text or an actual element.
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
	console.debug("Next node: " + node.nodeName + " " + node.data);

	// See if it is an equation
	var equation = GetEquation(node);
	if (equation != null) {
		var range = document.createRange();
		range.selectNode(equation);
		return range;
	}

	// See if it is an image
	if (node.nodeName == "IMG") {
		console.debug("Got an image!");
		var range = document.createRange();
		range.selectNode(node);
		return range;
	}

	// See if it is anything else, like text
	else {
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