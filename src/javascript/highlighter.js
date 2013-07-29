/**
 * Highlighter Functions
 * 
 * @author Spencer Graffe
 */
highlight = null;
highlightLine = null;
currentOffset = 0;

/**
 * Sets the beginning for the highlighter and the content streaming.
 * @param doLine
 * @param elementType
 */
function SetBeginning(doLine, elementType) {
    
    range = GetSelectionRange();
    
    // Reset some states
    ResetHeadingStates();
    ResetSearchStates();
    
    SelectFirstElement(range, elementType);
    
    // Set and scroll to highlight
    SetHighlight(range, doLine);
    ScrollToHighlight();
    
    // Clear the user selection
    window.getSelection().empty();
}

/**
 * Selects the first element present in the range. This is useful to set the
 * beginning.
 * @param range
 * @param elementType
 */
function SelectFirstElement(range, elementType) {
	myElem = range.startContainer;
	
	// Keep trying to grab the next element until the element types match up
	while (true) {
		if (myElem === null) {
			break;
		}
		
		if (elementType == 'text') {
			if (myElem.nodeName == '#text') {
				break;
			}
		}
		else if (elementType == 'math') {
			eq = GetEquation(myElem);
			if (eq != null) {
				myElem = eq;
				beginOffset = 0;
				break;
			}
		}
		else if (elementType == 'image') {
			if (myElem.nodeName == 'IMG') {
				beginOffset = 0;
				break;
			}
		}
		
		// If nothing could break the loop, get the next element
		myElem = NextElement(myElem);
	}
	
	range.selectNode(myElem);
}

/**
 * Move the highlight to the next element that should be highlighted.
 * @param doLine
 * @param elementType
 * @param lastElementType
 */
function HighlightNextElement(doLine, elementType, lastElementType) {
	console.debug("HighlightNextElement()");
	ClearLineHighlight();
	
	range = null;
	next = null;
	
	if (elementType == 'text') {
		// pass
	}
	else if (elementType == 'image') {
		
	}
	else if (elementType == 'math') {
		
	}
	else {
		alert('The highlighter does not recognize the element type: ' + elementType + '.');
	}
	
	// See if I actually got anything next. Otherwise, clear all highlighting.
	if (range == null) {
		ClearAllHighlights();
	}
	else {
		SetHighlight(range, doLine);
		ScrollToHighlight();
	}
	
	// Reset beginning offset
	beginOffset = 0;
}

/**
 * Highlights the next text element.
 * @param doLine
 * @param lastElementType
 */
function HighlightNextText(doLine, lastElementType) {
	range = null;
	return range;
}

function HighlightNextImage(doLine, lastElementType) {
	range = null;
	return range;
}

/**
 * Given a Range object, this will clean up any previous highlight and create a
 * highlight over the new range.
 * @param range
 * @param doLine
 */
function SetHighlight(range, doLine) {
    console.debug("SetHighlight()");
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

/**
 * Scrolls the view to where the highlight is.
 * @param isInstant
 */
function ScrollToHighlight(isInstant) {
    //console.debug("ScrollToHighlight()");
	isInstant = typeof isInstant !== 'undefined' ? isInstant : false;
	
    // Calculate the top offset making it the top 1/6 of the document viewport.
    // This will scale correctly for different zoom sizes
    var myOffset = window.innerHeight * (1.0 / 6.0)
    
	var myDuration = 800;
	if (isInstant) {
		myDuration = 0;
	}
	if (highlightLine != null) {
		$.scrollTo(highlightLine.parentNode, {duration: myDuration, offset: {top: -myOffset}});
	}
	else {
		$.scrollTo(highlight.parentNode, {duration: myDuration, offset: {top: -myOffset}});
	}
}


/**
 *  This function will set the line highlight to surround that particular range.
 *  It will highlight all the way to the previous sentence end to the next
 *  sentence end, or just the node if there are no sentences.
 */
function SetLineHighlight() {
    console.debug("SetLineHighlight()");
	highlightLine = document.createElement("span");
	highlightLine.setAttribute("id", "npaHighlightLine");

	// Start my range where my highlight is
	var range = document.createRange()
	range.selectNode(highlight);
	
	// If I have text in text highlight, do shifting. Otherwise, don't do 
	// anything
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


/**
 * Gets the parent node of the highlight in whatever form it may be. 
 */
function GetHighlightParent() {
    console.debug("GetHighlightParent()");
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
	return p;
}

/**
 * Gets the child index of the highlight inside of its parent. 
 */
function GetHighlightChildIndex() {
    console.debug("GetHighlightChildIndex()");
	if (!(highlightLine == null)) {
		return GetChildIndex(highlightLine);
	}
	else {
		return GetChildIndex(highlight);
	}
}


/**
 * Clears both the line highlight and the individual element highlight. 
 */
function ClearAllHighlights() {
    console.debug("ClearAllHighlights()");
	if (highlightLine != null) {
		ClearLineHighlight();
	}

	if (highlight != null) {
		ClearHighlight(); 
	}

}


/**
 * Clears the highlight of where it was before. 
 */
function ClearHighlight() {
	console.debug("ClearHighlight()");
	// Replace the highlight node with my contents
	var p = highlight.parentNode;

	InsertAllChildNodes(p, highlight);

	// Cleanup the highlight and its reference
	p.removeChild(highlight);
	p.normalize();
	highlight = null;
}


/**
 * Clears the line highlight. 
 */
function ClearLineHighlight() {
	console.debug("ClearLineHighlight()");
	if (highlightLine != null) {

		var p = highlightLine.parentNode;

		InsertAllChildNodes(p, highlightLine);

		// Recapture my highlight element reference
		highlight = document.getElementById("npaHighlight");

		p.removeChild(highlightLine);
		p.normalize();
		highlightLine = null;
	}

}