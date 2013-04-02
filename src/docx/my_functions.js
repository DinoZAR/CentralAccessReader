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
		var range = window.getSelection()
		var startNode = range.anchorNode;
		var offset = range.anchorOffset;
		
		// Check to see if the start is inside a math equation. If so, adjust selection to
		// only select that node. Otherwise, have it select the first whole word there.
		var equation = GetEquation(startNode);
		alert("Got something!");
		if (equation === null) {
			alert("No equation...");
			var nextIndex = startNode.textContent.substring(offset).search(/\w/) + offset;
			var endIndex = startNode.textContent.substring(nextIndex).search(/\s/) + nextIndex;

			// Create range from all this
			var range = document.createRange();
			range.setStart(startNode, nextIndex);
			range.setEnd(startNode, endIndex);

			alert("Made range!");

			// Replace with highlighting
			highlight = document.createElement("span");
			highlight.setAttribute("id", "npaHighlight");

			var contents = range.extractContents();
			highlight.appendChild(contents);
			
			range.insertNode(highlight);

			// Clear the selection
			window.getSelection().collapseToStart();
		}
		else {
			alert("Got an equation!" + equation.nodeName + equation.textContent);
			startNode = equation;
			offset = 0;

			// Set the highlight right there
			highlight = document.createElement("span");
			highlight.setAttribute("id", "npaHighlight");
			highlight.innerHTML = startNode.outerHTML
		
			// Replace the beginning with my highlight
			startNode.parentNode.replaceChild(highlight, startNode);
		}

		alert("Done!");
	}
}

// Returns the range of equation if node is inside an equation.
function GetEquation(node) {
	
	var myNode = node

	while (myNode.parentNode != null) {
		myNode = myNode.parentNode
		// Check to see if it is an equation by checking its class
		if (myNode.className == "mathmlEquation") {
			return myNode;
		}
	}
	return null;
}

// Clears the highlight of where it was before.
function ClearHighlight() {
	// Get the contents that I am going to replace the node with
	var contents = document.createDocumentFragment();
	contents.innerHTML = highlight.innerHTML;

	alert("Contents: " + contents.toString());

	// Replace the highlight node with mjy contents
	var p = highlight.parentNode;
	alert("Got parent!");
	p.insertBefore(contents, highlight);
	alert("Inserted contents!");
	p.removeChild(highlight);
	alert("Removed highlight!");

	alert("Done!");
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