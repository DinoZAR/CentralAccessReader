/*
 * Document-related Functions
 * 
 * @author Spencer Graffe
 */
var startFromHeading = false;
var lastHeadingElement = null;

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
	
	// Highlight the first element in the document. This will act as the cursor.
	var r = GetRangeToEntireDocument();
	var start = DeepestChild(r.startContainer);
	var offset = 0;
	
	// Get the first word, of that is the case
	if (start.nodeType == Node.TEXT_NODE) {
		var regex = /\b\w+\b/g;
		var m = start.data.match(regex);
		if (m !== null) {
			r.setStart(start, regex.lastIndex);
			r.setEnd(start, regex.lastIndex + m[0].length);
			SetHighlight(false, r);
		}
		else {
			r.selectNode(start);
			SetHighlight(false, r);
		}
	}
	else {
		r.selectNode(start);
		SetHighlight(false, r);
	}
	
	ClearUserSelection();
});

/**
 * Detect when MathJax is done messing around with the MathML. 
 */
finishedMathTypeset = false;
mathTypeSetProgress = 0;
MathJax.Hub.Queue(function () {
	finishedMathTypeset = true;
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
	
	// Get the next element, whatever that happens to be
	var elem = NextElement(highlight);
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
 * This moves the cursor up, jumping to the beginning of the previous paragraph.
 */
function MoveCursorUp() {
	var elem = highlight.parentNode.previousSibling;
	
	if (elem.nodeName === 'BODY') {
		elem = highlight;
	}
	
	if (elem !== null) {
		elem = DeepestChild(elem);
	}
	
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
		
		console.debug('Element that is up: ' + elem.nodeName);
		
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
 * This moves the cursor down, jumping to the beginning of the next paragraph.
 */
function MoveCursorDown() {
	var elem = NextElement(highlight.parentNode);
	
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