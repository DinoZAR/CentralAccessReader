/**
 * Document-related Functions
 * 
 * @author Spencer Graffe
 */
var startFromHeading = false;
var lastHeadingElement = null;

/**
 * Have tooltips pop up anytime there is an image with a tooltip. 
 */
$(function() {
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