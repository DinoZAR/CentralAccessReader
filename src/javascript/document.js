/*
 * Document-related Functions
 * 
 * @author Spencer Graffe
 */
var startFromHeading = false;
var lastHeadingElement = null;

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
	startFromHeading = true;
	lastHeadingElement = element_to_scroll_to;
	$.scrollTo(element_to_scroll_to, {duration: 200});
}

/**
 * Clears the user's selection.
 */
function ClearUserSelection() {
	sel = window.getSelection();
	sel.collapse();
}

/*******************************************************************************
Heading Functions
*******************************************************************************/

/**
 * Resets the states relating to the heading selection and playback.
 */
function ResetHeadingStates() {
    startFromHeading = false;
    lastHeadingElement = null;
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
			SetHighlight(false, r);
		}
		else {
			var r = document.createRange();
			r.selectNode(elem);
			SetHighlight(false, r);
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
function MoveCursorToBeginningOfNode(elem) {
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
		if (start >= 0) {
			var r = document.createRange();
			r.setStart(elem, start);
			r.setEnd(elem, offset);
			SetHighlight(false, r);
		}
		else {
			var r = document.createRange();
			r.selectNode(elem);
			SetHighlight(false, r);
		}
		
		// Scroll to the highlight
		ScrollToHighlight(true);
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
			SetHighlight(false, r);
		}
		else {
			var r = document.createRange();
			r.selectNode(elem);
			SetHighlight(false, r);
		}
		
		// Scroll to the highlight
		ScrollToHighlight(true);
	}
}