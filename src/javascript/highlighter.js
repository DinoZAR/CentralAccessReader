/*
 * Highlighter Functions
 * 
 * @author Spencer Graffe
 */

var highlight = null;
var highlightLine = null;
var isHighlighting = false;
var highlightBeginOffset = 0;
var isFirstHighlight = false;

/**
 * Flags that the highlighter can start.
 */
function StartHighlighting() {
	//console.debug('StartHighlighting()');
	isHighlighting = true;
	isFirstHighlight = true;
}

/**
 * Flags that the highlighter should not be highlighting anymore.
 */
function StopHighlighting() {
	//console.debug('StopHighlighting()');
	isHighlighting = false;
	isFirstHighlight = false;
	ClearAllHighlights();
}

/**
 * Highlights the next word.
 * 
 * @param doLine
 * @param lastElementType
 * @param word
 * @param wordOffset
 * @param wordLength
 */
function HighlightNextWord(doLine, word, wordOffset, wordLength) {
	//console.debug('HighlightNextWord()');
	var reference = GetReferencePoint();
	var elem = reference.element;
	var startOffset = reference.offset;
	var needScroll = false;
	
	ResetHeadingStates();
	
	// Search for a text node that has the word I want.
	while (true) {
		
		// Stop if I don't have anymore
		if (elem === null) {
			break;
		}
		
		// Check that my word offset is at or ahead of the start offset.
		// Otherwise, this may mean a different word in a different place.
		if ((wordOffset + highlightBeginOffset) >= (startOffset - word.length)) {
			// Check the node's properties
			if (elem.nodeType === Node.TEXT_NODE) {
				// Check if my proposed offset and length are within my text 
				// element
				if ((wordOffset + wordLength) <= elem.data.length) {
					// See if the word is even in there
					if (elem.data.indexOf(word) >= 0) {
						// Check if it is not inside an equation
						if (IsInsideEquation(elem) !== true) {
							break;
						}
					}
				}
			}
		}
		
		startOffset = 0;
		needScroll = true;
		
		highlightBeginOffset = 0;
		
		// If element fails test, try the next one
		elem = NextElement(elem);
	}
	
	// If I actually got an element, set the highlight
	if ((elem !== null) && (isHighlighting === true)) {
		var r = document.createRange();
		r.setStart(elem, wordOffset + highlightBeginOffset);
		r.setEnd(elem, wordOffset + wordLength + highlightBeginOffset);
		SetHighlight(doLine, r);
	}
	
	// Clear the user selection
	window.getSelection().empty()
	
	// Scroll to highlight if necessary
	if ((needScroll === true) || (isFirstHighlight === true)) {
		ScrollToHighlight();
	}
	
	isFirstHighlight = false;
}

/**
 * Highlights the next image.
 * 
 * @param doLine
 * @param lastElementType
 */
function HighlightNextImage(doLine) {
	//console.debug('HighlightNextImage()');
	var reference = GetReferencePoint();
	var elem = DeepestChild(reference.element);
	
	ResetHeadingStates();
	
	// Search until I get an image
	while (true) {
		
		if (elem === null) {
			break;
		}
		
		// See if it an image
		if (elem.nodeName === 'IMG') {
			break;
		}
		
		// If element fails test, try the next one
		elem = NextElement(elem);
	}
	
	// If I actually got an element, set the highlighter
	if ((elem !== null) && (isHighlighting === true)) {
		var r = document.createRange();
		r.selectNode(elem);
		
		SetHighlight(doLine, r);
	}
	
	// Clear the user selection
	window.getSelection().empty()
	
	ScrollToHighlight();
	
	highlightBeginOffset = 0;
	
	isFirstHighlight = true;
}

/**
 * Highlights the next math equation.
 * 
 * @param doLine
 * @param lastElementType
 */
function HighlightNextMath(doLine) {
	//console.debug('HighlightNextMath()');
	
	var reference = GetReferencePoint();
	var elem = reference.element;
	
	ResetHeadingStates();
	
	// Search until I get a math equation
	while (true) {
		
		if (elem === null) {
			break;
		}
		
		// Check if the element is inside a math equation
		if (IsInsideEquation(elem)) {
			break;
		}
		
		// If element fails test, try the next one
		elem = NextElement(elem);
	}
	
	// If I actually got an element, set the highlighter
	if ((elem !== null) && (isHighlighting === true)) {
		var r = document.createRange();
		var eq = GetEquation(elem);
		r.selectNode(eq);
		SetHighlight(doLine, r);
	}
	
	// Clear the user selection
	window.getSelection().empty()
	
	ScrollToHighlight();
	
	highlightBeginOffset = 0;
	
	isFirstHighlight = true;
	
}

/**
 * Returns the element that provides the reference point from which the next
 * thing to highlight should come after.
 * 
 * @returns {element, offset}
 */
function GetReferencePoint() {
	//console.debug('GetReferencePoint()');
	
	if (NoHighlights()) {
		var r = GetSelectionRange();
		return {element: r.startContainer, offset: r.startOffset};
	}
	else {
		// Now that we are dealing with a highlight, we have to remove it and
		// figure out its node position.
		ClearLineHighlight();
		
		// Calculate the index and offset of the element that is directly after 
		// the highlight after we have replaced it with all of its children
		var results = CalculateIndexOffsetAfterRemoval(highlight);
		var p = GetHighlightParent();
		ClearHighlight();
		var myElem = $(p).contents()[results.index];
		
		// If the index is larger than my children count, get the next element
		// after the parent.
		if (results.index >= $(p).contents().length) {
			myElem = NextElement(p);
		}
		
		if (myElem.nodeType === Node.TEXT_NODE) {
			return {element: myElem, offset: results.offset}
		}
		else {
			return {element: myElem, offset: results.offset}
		}
	}
}

/**
 * Checks to see if there are no highlights.
 * 
 * @returns {Boolean}
 */
function NoHighlights() {
	return (highlight === null) && (highlightLine === null);
}

/**
 * Gets the parent node of the highlight in whatever form it may be.
 * 
 *  @returns {Element}
 */
function GetHighlightParent() {
    //console.debug("GetHighlightParent()");
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
 * 
 * @returns {Integer}
 */
function GetHighlightChildIndex() {
    //console.debug("GetHighlightChildIndex()");
	if (highlightLine !== null) {
		return GetChildIndex(highlightLine);
	}
	else {
		return GetChildIndex(highlight);
	}
}

/**
 * Given a Range object, this will clean up any previous highlight and create a
 * highlight over the new range.
 * 
 * @param range
 * @param doLine
 */
function SetHighlight(doLine, range) {
    //console.debug("SetHighlight()");
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
    //console.debug("SetLineHighlight()");
	highlightLine = document.createElement("span");
	highlightLine.setAttribute("id", "npaHighlightLine");

	// Start my range where my highlight is
	var range = document.createRange()
	range.selectNode(highlight);
	
	// If I have text in text highlight, do shifting. Otherwise, don't do 
	// anything
	if (highlight.firstChild.nodeType === Node.TEXT_NODE) {
		if (!(highlight.previousSibling === null)) {
			if (highlight.previousSibling.nodeType === Node.TEXT_NODE) {
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
			if (highlight.nextSibling.nodeType === Node.TEXT_NODE) {
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
 * Clears both the line highlight and the individual element highlight. 
 */
function ClearAllHighlights() {
    //console.debug("ClearAllHighlights()");
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
	//console.debug("ClearHighlight()");
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
	//console.debug("ClearLineHighlight()");
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