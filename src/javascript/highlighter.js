/**
 * Highlighter Functions
 * 
 * @author Spencer Graffe
 */
var highlight = null;
var highlightLine = null;
var beginOffset = 0;

/**
 * Sets the beginning for the highlighter and the content streaming.
 * @param doLine
 * @param elementType
 */
function SetBeginning(doLine, elementType) {
	console.debug('SetBeginning()');
    range = GetSelectionRange();
    
    // Reset some states
    ResetHeadingStates();
    ResetSearchStates();
    
    SelectFirstElement(range, elementType);
    
    console.debug('New range: ' + GetHTMLSource(range));
    
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
	console.debug('SelectFirstElement()');
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
	
	range.selectNode(DeepestChild(myElem));
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
	
	var range = null;
	var next = null;
	
	if (elementType == 'text') {
		range = HighlightNextText(lastElementType);
	}
	else if (elementType == 'image') {
		range = HighlightNextImage(lastElementType);
	}
	else if (elementType == 'math') {
		range = HighlightNextMath(lastElementType);
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
		//ScrollToHighlight();
	}
	
	// Reset beginning offset
	beginOffset = 0;
}

/**
 * Highlights the next text element.
 * @param doLine
 * @param lastElementType
 */
function HighlightNextText(lastElementType) {
	console.debug('HighlightNextText()');
	range = null;
	
	// Keep getting the next text element until the parent has changed.
	var origParent = highlight.parentNode;
	next = NextElement(highlight);
	var done = false;
	while (!done) {
		if (lastElementType == 'text') {
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
    range.selectNode(DeepestChild(next))
	//range.setStart(next, 0);
	//range.setEnd(next, 1);
//	console.debug("New next: " + next.toString());
//	if (next.nodeName == "#text") {
//		console.debug("Text!" + next.data + ", " + next.data.length.toString());
//	}
	return range;
}

/**
 * Highlights the next image element.
 * @param lastElementType
 * @returns
 */
function HighlightNextImage(lastElementType) {
	console.debug('HighlightNextImage()');
	range = null;
	next = NextElement(highlight);
	while (next.nodeName != "IMG") {
		next = NextElement(next);
		if (next === null) {
			break;
		}
	}
	if (next != null) {
		range = document.createRange();
		range.selectNode(next);
	}
	return range;
}

/**
 * Highlights the next math element.
 * @param lastElementType
 * @returns
 */
function HighlightNextMath(lastElementType) {
	console.debug('HighlightNextMath()');
	range = null;
	next = NextElement(highlight);
	while (GetEquation(next) === null) {
		next = NextElement(next);
		if (next === null) {
			break;
		}
	}
	if (next != null) {
		range = document.createRange();
		range.selectNode(GetEquation(next));
	}
	return range;
}

/**
 * Highlights a word in the current element based on the offset and length from
 * the TTS driver. This function will handle the offsets from the selection.
 * 
 * @param doLine
 * @param offset
 * @param length
 * @param word
 */
function HighlightWord(doLine, offset, length, word) {
	console.debug("HighlightWord()");
	
	// Get the parent element from the highlight from which we do these 
	// calculations
	var p = GetHighlightParent();
	var childNum = GetHighlightChildIndex();
    
    var r = document.createRange();
    r.selectNode(p)
	console.debug('Child number: ' + childNum.toString());
	console.debug('Parent: ' + GetHTMLSource(r));
	
	// Check to see if the text we want is in the parent. Otherwise, keep moving
	// to the next text element until we find it
	ClearAllHighlights();
    console.debug('Parent: ' + GetHTMLSource(r));
    console.debug('Length of parent: ' + $(p).contents().length.toString());
    if (childNum >= $(p).contents().length) {
        childNum = $(p).contents().length - 1;
    }
	var t = $(p).contents()[childNum];
	
	console.debug('What is t? ' + t.toString());
	console.debug('t: ' + t.data.toString());
	console.debug('word: ' + word);
	
	while (t.data.indexOf(word) < 0) {
		// Generate a highlight 
		var range = document.createRange();
		range.selectNode($(p).contents()[childNum]);
		SetHighlight(range, doLine);
		
		// Highlight the next text element. We are still searching for the text
		// we want.
		HighlightNextElement(doLine, 'text', 'text');
		p = GetHighlightParent();
		childNum = GetHighlightChildIndex();
		ClearAllHighlights();
		t = $(p).contents()[childNum];
	}
	
	// Create range and select that text
	var range = document.createRange();
	range.setStart(t, offset + beginOffset);
	range.setEnd(t, offset + length + beginOffset);
	
	// Create the highlight
	SetHighlight(range, doLine);
}

/**
 * Scrolls the view to where the highlight is.
 * @param isInstant
 */
function ScrollToHighlight(isInstant) {
    console.debug("ScrollToHighlight()");
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
 * This function will set the line highlight to surround that particular range.
 * It will highlight all the way to the previous sentence end to the next
 * sentence end, or just the node if there are no sentences.
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
	if (!(highlightLine == null)) {
		p = highlightLine.parentNode;
	}
	else {
		p = highlight.parentNode;
	}
	return p;
}

/**
 * Gets the child index of the highlight inside of its parent. 
 */
function GetHighlightChildIndex() {
    console.debug("GetHighlightChildIndex()");
	if (highlightLine !== null) {
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
	if (highlightLine !== null) {
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