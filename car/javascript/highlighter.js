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

var mySelectionRange = null;

/**
 * Flags that the highlighter can start.
 */
function StartHighlighting() {
	if (isHighlighting) {
		StopHighlighting();
	}
	
	//console.debug('StartHighlighting()');
	content = SetStreamBeginning();
	
	isHighlighting = true;
	isFirstHighlight = true;
	
	return content
}

/**
 * Flags that the highlighter should not be highlighting anymore.
 */
function StopHighlighting() {
	
	if (isHighlighting) {
		//console.debug('StopHighlighting()');
		isHighlighting = false;
		isFirstHighlight = false;
		
		// If there isn't a highlight present, make sure to create one
		if (highlight === null) {
			
			//console.debug('Trying to create highlight...');
			
			var range = GetSelectionRange();
			var startElem = range.startContainer;
			
			// Modify it to select the first word if I'm in a text node
			if (startElem.nodeType === Node.TEXT_NODE) {
		    	var regex = /\w+/g;
				var m = regex.exec(startElem.data.substring(range.startOffset));
				var start = -1;
				var offset = -1;
				if (m !== null) {
					start = regex.lastIndex - m[0].length;
					offset = regex.lastIndex;
				}
		    	
				if (start >= 0) {
					var myRangeStart = range.startOffset;
					range.setStart(startElem, start + myRangeStart);
					range.setEnd(startElem, offset + myRangeStart);
				}
				else {
					range.selectNode(startElem);
				}
			}
			
			else {
				startElem = DeepestChild(startElem.children[range.startOffset]);
				
				// Check if I get a math equation. If I do, select that instead
				var eq = GetEquation(startElem);
				if (eq !== null) {
					range.selectNode(eq);
				}
				else{
					range.selectNode(startElem);
				}
			}
			
			SetHighlight(false, range, true, false);
		}
		
		ClearLineHighlight();
		ClearUserSelection();
	}
	
	else {
		
		isFirstHighlight = false;
		
		// Check if we have a highlight somewhere. If we don't, get the
		// highlight set
		if (highlight === null) {
			var range = GetSelectionRange();
		    var startElem = range.startContainer;
		    var myRange = document.createRange();
		    
		    var eq = GetEquation(startElem);
		    if (eq !== null) {
		    	startElem = eq;
		    	myRange.setStart(startElem, range.startOffset);
			    myRange.setEndAfter(startElem);
		    }
		    else if (startElem.nodeType === Node.TEXT_NODE) {
		    	// See if I can't get the first word from the text. If I can't, I'll
		    	// just select all of the text.
		    	var regex = /\w+/g;
				var m = regex.exec(startElem.data.substring(range.startOffset));
				var start = -1;
				var offset = -1;
				if (m !== null) {
					start = regex.lastIndex - m[0].length;
					offset = regex.lastIndex;
				}
		    	
				if (start >= 0) {
					var myRangeStart = range.startOffset;
					myRange.setStart(startElem, start + myRangeStart);
					myRange.setEnd(startElem, offset + myRangeStart);
				}
				else {
					myRange.selectNode(startElem);
				}
		    }
		    else {
		    	myRange.selectNode(startElem);
		    }
		    
		    SetHighlight(false, myRange, true, false);
		    //ScrollToHighlight(true);
		}
	}
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
function HighlightNextWord(doLine, word, wordOffset, wordLength, shouldFollow, doWord) {
	
	shouldFollow = typeof shouldFollow !== 'undefined' ? shouldFollow : false;
	doWord = typeof doWord !== 'undefined' ? doWord : true;
	
	if (isHighlighting) {
		//console.debug('HighlightNextWord()');
		
		var reference = GetReferencePoint();
		var elem = reference.element;
		var startOffset = reference.offset;
		var needScroll = false;
		
		
		// Search for a text node that has the word I want.
		while (true) {
			
			// Stop if I don't have anymore
			if (elem === null) {
				break;
			}
			
			if (elem.nodeType === Node.TEXT_NODE) {
				if ((wordOffset + highlightBeginOffset) >= (startOffset - wordLength)) {
					var sub = elem.data.substring(wordOffset + highlightBeginOffset, 
							wordOffset + wordLength + highlightBeginOffset);
					if (sub === word) {
						break;
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
		if (elem !== null) {
			var r = document.createRange();
			r.setStart(elem, wordOffset + highlightBeginOffset);
			r.setEnd(elem, wordOffset + wordLength + highlightBeginOffset);
			SetHighlight(doLine, r, true, doWord);
		}
		
		// Clear the user selection
		window.getSelection().empty()
		
		// Scroll to highlight if necessary
		if ((needScroll === true) || isFirstHighlight) {
			ScrollToHighlight();
		}
		else {
			if (shouldFollow) {
				// If the highlight is not in view, move the view to the highlight
				// itself (previously, it was the parent of the highlight)
				if (!ElementInViewport(highlight)) {
					ScrollToElement(highlight, true);
				}
			}
		}
		
		isFirstHighlight = false;
	}
}

/**
 * Highlights the next image.
 * 
 * @param doLine
 * @param lastElementType
 */
function HighlightNextImage(doLine, doWord) {
    doWord = typeof doWord !== 'undefined' ? doWord : true;

	if (isHighlighting) {
		//console.debug('HighlightNextImage()');
		var reference = GetReferencePoint();
		var elem = DeepestChild(reference.element);
		
		if ((reference.element.nodeType !== Node.TEXT_NODE) && (reference.element.children.length > 0)) {
			elem = $(reference.element).contents()[reference.offset];
		}
		
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
		if (elem !== null) {
			var r = document.createRange();
			r.selectNode(elem);
			
			SetHighlight(doLine, r, true, doWord);
		}
		
		// Clear the user selection
		window.getSelection().empty()
		
		// Scroll to highlight
		ScrollToElement(highlight);
		
		highlightBeginOffset = 0;
		isFirstHighlight = false;
	}
}

/**
 * Highlights the next math equation.
 * 
 * @param doLine
 * @param lastElementType
 */
function HighlightNextMath(doLine, doWord) {
    doWord = typeof doWord !== 'undefined' ? doWord : true;

	if (isHighlighting) {
		//console.debug('HighlightNextMath()');
		
		var reference = GetReferencePoint();
		var elem = reference.element;
		
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
		if (elem !== null) {
			var r = document.createRange();
			var eq = GetEquation(elem);
			r.selectNode(eq);
			SetHighlight(doLine, r, true, doWord);
		}
		
		// Clear the user selection
		window.getSelection().empty()
		
		ScrollToHighlight();
		
		highlightBeginOffset = 0;
		isFirstHighlight = false;
	}
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
function SetHighlight(doLine, range, isSelection, doWord) {
    doWord = typeof doWord !== 'undefined' ? doWord : false;

    //console.debug("SetHighlight()");
	if (highlight != null) {
		ClearHighlight();
	}

	if (highlightLine != null) {
		ClearLineHighlight();
	}

	highlight = document.createElement("span");
	
	if (doWord == true) {
		highlight.setAttribute("id", "npaHighlightSelection");
	}
	else {
		highlight.setAttribute("id", "npaHighlight");
	}

	var contents = range.extractContents();
	highlight.appendChild(contents);
	
	// Check if the highlight is surrounding an image. If so, increase the
	// padding size so that we can see the border
	if (highlight.firstChild !== null) {
		if (highlight.firstChild.nodeName === 'IMG') {
			highlight.style.padding = '0.2em';
		}
	}

	range.insertNode(highlight);
	
	SetMathColors(highlight);

	if (doLine == true) {
		SetLineHighlight();
	}
}

function SetHighlightToBeginning() {
	
	// Get the first word, image, or math equation, whichever comes first
	var done = false;
	var elem = DeepestChild(document.body);
	var range = document.createRange();
	
	while (!done) {
		
		// Calculate whether the element is visible
		var s = window.getComputedStyle(elem);
		var isVisible = false;
		if (s === null) {
			isVisible = true;
		}
		else {
			isVisible = s.getPropertyValue('visible')
			if (isVisible === null) {
				isVisible = true;
			}
			else {
				if (isVisible.find('hidden') >= 0) {
					isVisible = false;
				}
				else {
					isVisible = true;
				}
			}
		}
		
		// Only consider it if it is visible
		if (isVisible) {
			
			// Check if math equation
			var eq = GetEquation(elem);
			if (eq !== null) {
				range.selectNode(eq);
				done = true;
			}
			
			// Check if an image
			else if (elem.nodeName == 'IMG') {
				range.selectNode(elem);
				done = true;
			}
			
			// Check if a text element
			if (elem.nodeType == Node.TEXT_NODE) {
				
				// Get first word, if found. Otherwise, move on.
				var regex = /\b\w+\b/g;
				var m = elem.data.match(regex);
				if (m !== null) {
					range.setStart(elem, regex.lastIndex);
					range.setEnd(elem, regex.lastIndex + m[0].length);		
					done = true;
				}
			}
		}
		
		elem = NextElement(elem);
		
		if (elem === null) {
			done = true
		}
	}
	
	SetHighlight(false, range, true, false);
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
				var endSentenceRegex = /[!?.][\s]/g;
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
				var endSentenceRegex = /[!?.][\s]/g;
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
	
	var contents = range.extractContents();
	highlightLine.appendChild(contents);
	range.insertNode(highlightLine);
	SetMathColors(highlightLine);
}

/**
 * Clears both the line highlight and the individual element highlight. 
 */
function ClearAllHighlights() {
    //console.debug("ClearAllHighlights()");
	if (highlightLine !== null) {
		ClearLineHighlight();
	}

	if (highlight !== null) {
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
	
	SetMathColors(p);
}

/**
 * Clears the line highlight. 
 */
function ClearLineHighlight() {
	//console.debug("ClearLineHighlight()");
	if (highlightLine != null) {
		var p = highlightLine.parentNode;

		InsertAllChildNodes(p, highlightLine);

		p.removeChild(highlightLine);
		p.normalize();
		highlightLine = null;
		
		SetMathColors(p);
	}
	
	// Recapture my highlight element reference while changing its style to that
	// of a selection.
	highlight = document.getElementById("npaHighlight");
	if (highlight !== null) {
		highlight.id = "npaHighlightSelection";
	}
	else {
		highlight = document.getElementById('npaHighlightSelection');
	}
}

/**
 * Scrolls the view to where the highlight is.
 * @param isInstant
 */
function ScrollToHighlight(isInstant) {
    //console.debug("ScrollToHighlight()");
	isInstant = typeof isInstant !== 'undefined' ? isInstant : false;
	ScrollToElement(highlight.parentNode, isInstant);
}

/**
 * Scrolls the view to show the element. If isInstant is false, the view will
 * smoothly scroll to show the element. Otherwise, the view will jump to it.
 */
function ScrollToElement(elem, isInstant) {
	isInstant = typeof isInstant !== 'undefined' ? isInstant : false;
	
	// Calculate the top offset making it the top 1/6 of the document viewport.
    // This will scale correctly for different zoom sizes
    var myVerticalOffset = window.innerHeight * (1.0 / 6.0);
    
    // Calculate the horizontal offset, which should be the first 1/3 of the
    // document viewport
    var myHorizOffset = window.innerWidth * (1.0 / 3.0);
    
	var myDuration = 800;
	if (isInstant) {
		myDuration = 0;
	}
	if (highlightLine != null) {
		$.scrollTo(elem, {duration: myDuration, offset: {top: -myVerticalOffset, left: -myHorizOffset}});
	}
	else {
		$.scrollTo(elem, {duration: myDuration, offset: {top: -myVerticalOffset, left: -myHorizOffset}});
	}
}

/**
 * Sets the colors of the math to the color as defined in the style of the
 * parent element.
 */
function SetMathColors(parentElem) {
	
//	for (var i = 0; i < parentElem.children.length; i++) {
//		var myElem = parentElem.children[i];
//		myStyle = window.getComputedStyle(myElem);
//		if (myElem.hasAttribute('stroke')) {
//			myElem.setAttribute('stroke', myStyle.getPropertyValue('color'));
//		}
//		if (myElem.hasAttribute('fill')) {
//			myElem.setAttribute('fill', myStyle.getPropertyValue('color'));
//		}
//		
//		SetMathColors(parentElem.children[i]);
//	}
	
	$(parentElem).find('*[stroke]').each(function (index, element) {
		var myStyle = window.getComputedStyle(element);
		element.setAttribute('stroke', myStyle.getPropertyValue('color'));
	});
	
	// Set the fills
	$(parentElem).find('*[fill]').each(function (index, element) {
		var myStyle = window.getComputedStyle(element);
		element.setAttribute('fill', myStyle.getPropertyValue('color'));
	});
}