// Used in page navigation to move to an anchor point with specific id
function GotoPageAnchor(anchorName) {
	element_to_scroll_tasdo = document.getElementById(anchorName);
	element_to_scroll_to.scrollIntoView();
}

// Variables for storing exactly where the highlighter is
var highlight; // The highlighter element that has the highlighted content.
var hasHighlight = false;

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
		var range = window.getSelection();
		var startNode = range.anchorNode.parentNode.nodeName;
		
		// Set the highlight right there
		var mySpan = document.createElement("span");
		mySpan.setAttribute("id", "npaHighlight");
		mySpan.appendChild(myContents);

		range.deleteContents();
		range.insertNodes(mySpan);
	}
}

// Sets the highlight right on the selection. It will make sure to select the
// entire word on the beginning and end of the selection.
function SetHighlight() {
	if (window.getSelection()) {
		var range = window.getSelection().getRangeAt(0);
		
		var debugString = "The Range!\n";
		debugString += "Starting char: " + range.startContainer.nodeValue.toString()[range.startOffset] + "\n";
		debugString += "Ending char: " + range.endContainer.nodeValue.toString()[range.endOffset] + "\n";
		//alert(debugString);
		
		// Get a clone of my contents to insert into my highlight span
		var myContents = range.cloneContents();
		
		// Insert my custom span object at the beginning with my cloned content
		// inserted.
		var mySpan = document.createElement("span");
		mySpan.setAttribute("id", "npaHighlight");
		mySpan.appendChild(myContents);
		
		// Delete what is inside of my range
		range.deleteContents();
		
		// Insert my new highlighted region
		range.insertNode(mySpan);
	}
}