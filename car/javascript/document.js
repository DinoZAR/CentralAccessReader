/*
 * Document-related Functions
 * 
 * @author Spencer Graffe
 */

// States for refreshing the math equations
var lastRefreshedEquation = null;

/**
 * Detect when MathJax is done messing around with the MathML. 
 */
finishedMathTypeset = false;
mathTypeSetProgress = 0;
MathJax.Hub.Queue(function () {
	SetHighlightToBeginning();
	ClearUserSelection();
	finishedMathTypeset = true;
});

/**
 * This function is run at startup. Do whatever one needs to do to setup
 * for things to come.
 */
$(document).ready( function() {
	
	// Have tooltips pop up anytime there is an image with a tooltip. 
    $( document ).tooltip({
      position: {
        my: "center top+20",
        at: "center bottom",
        using: function( position, feedback ) {
          $( this ).css( position );
          $( "<div>" )
            .addClass( feedback.vertical )
            .addClass( feedback.horizontal )
            .appendTo( this );
        }
      },
      hide: false,
      show: false
    });
    
});

/**
 * Every time the user clicks on the document somewhere, it will set the
 * highlight to the element under the cursor. If its text, it will select the
 * closest word.
 */
document.onclick = function (ev) {
	if (!isHighlighting) {
		
		var myR = window.getSelection();
		if (myR.isCollapsed) {

			// Get the range of where my caret is
		    var r = document.caretRangeFromPoint(ev.clientX, ev.clientY);
		    var elem = document.elementFromPoint(ev.clientX, ev.clientY);
		    
		    // Check if it is an equation or an image first
		    if (!IsInsideHighlight(elem)) {	    	
		    	if (elem.nodeName == "IMG") {
		    		r.selectNode(elem);
		    		SetHighlight(false, r, true);
		    		AlmightyGod._emitNavigationBarUpdate();
		    		return;
		    	}
		    	
		    	var eq = GetEquation(elem);
		    	if (eq !== null) {
		    		r.selectNode(eq);
		    		SetHighlight(false, r, true);
		    		AlmightyGod._emitNavigationBarUpdate();
		    		return;
		    	}
		    }
		    
		    // Now check for text
		    if (!IsInsideHighlight(r.startContainer)) {
			    if (r.startContainer.nodeType === Node.TEXT_NODE) {
			    	var word = GetWordRange(r.startContainer.data, r.startOffset);
			    	if (word.start != word.end) {
			    		r.setStart(r.startContainer, word.start);
			    		r.setEnd(r.startContainer, word.end);
			    		
			    		// Set the highlight around it
			    		SetHighlight(false, r, true);
			    		AlmightyGod._emitNavigationBarUpdate();
			    		return;
			    	}
			    	else {
			    		// Try getting the deepest element and seeing if I get an
			    		// image or math equation from that
			    		elem = DeepestChild(elem);
			    		
			    		if (!IsInsideHighlight(elem)) {	    	
			    	    	if (elem.nodeName == "IMG") {
			    	    		r.selectNode(elem);
			    	    		SetHighlight(false, r, true);
			    	    		AlmightyGod._emitNavigationBarUpdate();
			    	    		return;
			    	    	}
			    	    	
			    	    	var eq = GetEquation(elem);
			    	    	if (eq !== null) {
			    	    		r.selectNode(eq);
			    	    		SetHighlight(false, r, true);
			    	    		AlmightyGod._emitNavigationBarUpdate();
			    	    		return;
			    	    	}
			    	    }
			    	}
			    }
			    else {
			    	var myOffset = r.startOffset;
			    	if (myOffset >= r.startContainer.children.length) {
			    		myOffset = r.startContainer.children.length - 1;
			    	}
			    	
			    	var elem = r.startContainer.children[myOffset];
			    	r.selectNode(elem);
			    	
		    		// Set the highlight around it
		    		SetHighlight(false, r, true);
		    		AlmightyGod._emitNavigationBarUpdate();
		    		return;
			    }
		    }
		}
	}
}

/**
 * Returns true when the document has been completely loaded, except MathJax.
 */
function IsPageLoaded() {
    //console.debug("IsPageLoaded()");
	if (document.readyState === 'interactive') {
		return true;
	}
	return false;
}

/**
 * Returns true when MathJax is done typesetting the math equations. 
 */
function IsMathTypeset() {
    //console.debug("IsMathTypeset()");
	return finishedMathTypeset;
}

MathJax.Hub.processMessage = function (state, type) {
	mathTypeSetProgress = Math.floor((state.i/state.scripts.length) * 50);
}
/**
 * Returns the typeset progress from MathJax. Returns an integer from 0-100.
 */
function GetMathTypesetProgress() {
    //console.debug("GetMathTypesetProgress()");
	return mathTypeSetProgress * 2;
}

/**
 * Used in page navigation to move to an anchor point with specific id.
 * @param anchorName
 */
function GotoPageAnchor(anchorName) {
	//console.debug("GotoPageAnchor()");
	element_to_scroll_to = document.getElementById(anchorName);
	
	// Set the highlight to the beginning of that anchor
	MoveCursorToBeginningOfNode(DeepestChild(element_to_scroll_to), true);
}

/**
 * Clears the user's selection.
 */
function ClearUserSelection() {
	sel = window.getSelection();
	sel.collapse();
}

/**
 * Refreshes the document to update the styles. This should cause the document
 * to change colors, not to reload everything.
 */
function RefreshDocument() {
	var links = document.getElementsByTagName("link");

	for (var x in links) {
	    var link = links[x];
	    
	    if (link.getAttribute) {
		    if (link.getAttribute("type").indexOf("css") > -1) {
		        link.href = link.href + "?id=" + new Date().getMilliseconds();
		    }
	    }
	}
	
	// Also set the colors of all the math equations to their correct colors
	lastRefreshedEquation = $('.MathJax_SVG').first()[0];
	setTimeout(RefreshMathEquation, 70);
}

/**
 * Refreshes the math equation, then refreshes the next one after it. If there
 * are no more math equations, this function stops calling itself. This function
 * is set up this way so that it gives some of the control to the UI thread.
 */
function RefreshMathEquation() {
	SetMathColors(lastRefreshedEquation);
	lastRefreshedEquation = GetNext(lastRefreshedEquation, '.MathJax_SVG');
	
	if (lastRefreshedEquation !== null) {
		setTimeout(RefreshMathEquation, 70);
	}
}

/*******************************************************************************
Heading Functions
*******************************************************************************/

/**
 * Gets the current heading that the highlight is under.
 * @returns {String}
 */
function GetCurrentHeading() {
	
	var elemSel = $(highlight);
	var headingSel = $("h1, h2, h3, h4, h5, h6");
	var elem = GetPreviousOccurrence(elemSel, headingSel);
	
	if (elem !== null) {
		return elem.id;
	}
	
	return '';
}

/**
 * Gets the current page that the highlight is under.
 * @returns {String}
 */
function GetCurrentPage() {
	var elemSel = $(highlight);
	var headingSel = $("p.pageNumber");
	var elem = GetPreviousOccurrence(elemSel, headingSel);
	
	if (elem !== null) {
		return elem.id;
	}
	
	return ''
}

/*******************************************************************************
Cursor functions
*******************************************************************************/

/**
 * Moves the cursor to the left. It will go to the previous word or element,
 * whichever is there.
 */
function MoveCursorLeft() {
	
	// Get the previous element, whatever that happens to be.
	var elem = PreviousElement(highlight);
	var start = -1;
	var offset = -1;
	while (elem !== null) {
		var equation = GetEquation(elem);
		
		// If it is an equation, select the top element
		if (equation !== null) {
			elem = equation;
			break;
		}
		
		// If it is a text node, try to see if I can get a word
		else if (elem.nodeType == Node.TEXT_NODE) {
			var regex = /\w+/g;
			var m;
			while ((m = regex.exec(elem.data)) !== null) {
				start = regex.lastIndex - m[0].length;
				offset = regex.lastIndex;
			}
			if (start >= 0) {
				break;
			}
		}
		
		// If an image, get the image
		else if (elem.nodeName === 'IMG') {
			break;
		}
		
		elem = PreviousElement(elem);
	}
	
	// If I got something, get that next element highlighted
	if (elem !== null) {
		if (start >= 0) {
			var r = document.createRange();
			r.setStart(elem, start);
			r.setEnd(elem, offset);
			SetHighlight(false, r, true);
		}
		else {
			var r = document.createRange();
			r.selectNode(elem);
			SetHighlight(false, r, true);
		}
		
		// Scroll to the highlight
		ScrollToHighlight(true);
	}
}

/**
 * Moves the cursor to the right. It will get the next word or element,
 * whichever is there.
 */
function MoveCursorRight() {
	var elem = NextElement(highlight);
	MoveCursorToBeginningOfNode(elem);
}

/**
 * This moves the cursor up, jumping to the beginning of the previous paragraph.
 */
function MoveCursorUp() {
	var elem = PreviousElementFirstChild(highlight.parentNode);
	MoveCursorToEndOfNode(elem);
	MoveCursorToStart();
}

/**
 * This moves the cursor down, jumping to the beginning of the next paragraph.
 */
function MoveCursorDown() {
	var elem = NextElement(highlight.parentNode);
	MoveCursorToBeginningOfNode(elem);
}

/**
 * Moves the cursor to the start of the line.
 */
function MoveCursorToStart() {
	var p = highlight.parentNode;
	ClearAllHighlights();
	var elem = p.firstChild;
	MoveCursorToBeginningOfNode(elem);
}

/**
 * Moves the cursor to the end of the line.
 */
function MoveCursorToEnd() {
	var p = highlight.parentNode;
	ClearAllHighlights();
	var elem = p.lastChild;
	MoveCursorToEndOfNode(elem);
}

/**
 * Moves the cursor to the previous bookmark, whether that is a heading or a
 * page number.
 */
function MoveCursorToPreviousBookmark() {
	var elemSel = $(highlight.parentNode);
	var headingSel = $("p.pageNumber, h1, h2, h3, h4, h5, h6");
	var elem = GetPreviousOccurrence(elemSel, headingSel);
	
	if (elem !== null) {
		elem = DeepestChild(elem);
		MoveCursorToBeginningOfNode(elem);
	}
}

/**
 * Moves the cursor to the next bookmark, whether that is a heading or a page
 * number.
 */
function MoveCursorToNextBookmark() {
	var elemSel = $(highlight);
	var headingSel = $("p.pageNumber, h1, h2, h3, h4, h5, h6");
	var elem = GetNextOccurrence(elemSel, headingSel);
	
	if (elem !== null) {
		elem = DeepestChild(elem);
		MoveCursorToBeginningOfNode(elem);
	}
}

/**
 * Moves to the beginning of whatever the node is.
 * @param elem
 */
function MoveCursorToBeginningOfNode(elem, isGradual) {
	isGradual = typeof isGradual !== 'undefined' ? isGradual : false;
	
	var start = -1;
	var offset = -1;
	while (elem !== null) {
		var equation = GetEquation(elem);
		
		// If it is an equation, select the top element
		if (equation !== null) {
			elem = equation;
			break;
		}
		
		// If it is a text node, try to see if I can get a word
		else if (elem.nodeType == Node.TEXT_NODE) {
			// Check if I got a word I can highlight
			var regex = /\w+/g;
			var m = regex.exec(elem.data);
			if (m !== null) {
				start = regex.lastIndex - m[0].length;
				offset = regex.lastIndex;
				break;
			}
		}
		
		// If an image, get the image
		else if (elem.nodeName === 'IMG') {
			break;
		}
		
		elem = NextElement(elem);
	}
	
	// If there is something next, get that next element highlighted
	if (elem !== null) {
		if (!IsInsideHighlight(elem)) {
			if (start >= 0) {
				var r = document.createRange();
				r.setStart(elem, start);
				r.setEnd(elem, offset);
				SetHighlight(false, r, true);
			}
			else {
				var r = document.createRange();
				r.selectNode(elem);
				SetHighlight(false, r, true);
			}
			
			// Scroll to the highlight
			if (isGradual) {
				var myVerticalOffset = window.innerHeight * (1.0 / 6.0);
			    var myHorizOffset = window.innerWidth * (1.0 / 3.0);
			    $.scrollTo(highlight, {duration: 200, offset: {top: -myVerticalOffset, left: -myHorizOffset}});
			}
			else {
				ScrollToHighlight(true);
			}
		}
	}
}

/**
 * Moves to the end of whatever the node is.
 * @param elem
 */
function MoveCursorToEndOfNode(elem) {
	var start = -1;
	var offset = -1;
	while (elem !== null) {
		var equation = GetEquation(elem);
		
		// If it is an equation, select the top element
		if (equation !== null) {
			elem = equation;
			break;
		}
		
		// If it is a text node, try to see if I can get a word
		else if (elem.nodeType == Node.TEXT_NODE) {
			var regex = /\w+/g;
			var m;
			while ((m = regex.exec(elem.data)) !== null) {
				start = regex.lastIndex - m[0].length;
				offset = regex.lastIndex;
			}
			if (start >= 0) {
				break;
			}
		}
		
		// If an image, get the image
		else if (elem.nodeName === 'IMG') {
			break;
		}
		
		elem = PreviousElement(elem);
	}
	
	// If I got something, get that next element highlighted
	if (elem !== null) {
		if (start >= 0) {
			var r = document.createRange();
			r.setStart(elem, start);
			r.setEnd(elem, offset);
			SetHighlight(false, r, true);
		}
		else {
			var r = document.createRange();
			r.selectNode(elem);
			SetHighlight(false, r, true);
		}
		
		// Scroll to the highlight
		ScrollToHighlight(true);
	}
}