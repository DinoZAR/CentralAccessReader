/*
 * Stream functions (so far, just for TTS)
 * 
 * @author Spencer Graffe
 */

var nextStreamElement = null;

/**
 * Gives me a beginning to work with.
 */
function SetStreamBeginning() {
    //console.debug('SetStreamBeginning()');
    
    var range = GetSelectionRange();
    nextStreamElement = range.startContainer;
    
    var eq = GetEquation(nextStreamElement);
    if (eq !== null) {
    	nextStreamElement = eq;
    }
    
    var myRange = document.createRange();
    myRange.setStart(nextStreamElement, range.startOffset);
    myRange.setEndAfter(nextStreamElement);
    highlightBeginOffset = range.startOffset;
    
    nextStreamElement = NextElement(nextStreamElement)
    
    return GetHTMLSource(myRange);
}

/**
 * Gets the next element content to read. Returns a string representing the
 * HTML content. 
 */
function StreamNextElement() {
    //console.debug('StreamNextElement()');
    
    var eq = null;
    if (nextStreamElement != null) {
        eq = GetEquation(nextStreamElement);
    }
    
    if (eq !== null) {
        nextStreamElement = eq;
    }
    
    if (nextStreamElement === null) {
        return '';
    }
    else {
        var myRange = document.createRange();
        myRange.selectNode(nextStreamElement);
        nextStreamElement = NextElement(nextStreamElement);
        return GetHTMLSource(myRange);
    }
}

/**
 * Returns whether there are more elements to stream.
 * @returns {Boolean}
 */
function HasMoreElements() {
    //console.debug('HasMoreElements()');
    if (nextStreamElement == null) {
        return false;
    }
    return true;
}