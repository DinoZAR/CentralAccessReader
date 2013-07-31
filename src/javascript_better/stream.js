/**
 * Stream functions (so far, just for TTS)
 * 
 * @author Spencer Graffe
 */

var lastStreamElement = null;

/**
 * Gives me a beginning to work with.
 */
function SetStreamBeginning() {
    console.debug('SetStreamBeginning()');
    range = GetSelectionRange();
    lastStreamElement = range.startContainer;
    myRange = document.createRange();
    myRange.setStart(lastStreamElement, range.startOffset);
    myRange.setEndAfter(lastStreamElement);
    //myRange.selectNode(DeepestChild(lastStreamElement));
    console.debug('SetStreamBeginning() ' + GetHTMLSource(myRange));
    return GetHTMLSource(myRange);
}

/**
 * Gets the next element content to read. Returns a string representing the
 * HTML content. 
 */
function StreamNextElement() {
    //console.debug('StreamNextElement()');
    lastStreamElement = NextElement(lastStreamElement);
    
    eq = null;
    if (lastStreamElement != null) {
        eq = GetEquation(lastStreamElement);
    }
    
    if (eq != null) {
        lastStreamElement = eq;
    }
    
    if (lastStreamElement == null) {
        return '';
    }
    else {
        myRange = document.createRange();
        myRange.selectNode(lastStreamElement);
        return GetHTMLSource(myRange);
    }
}

/**
 * Returns whether there are more elements to stream.
 * @returns {Boolean}
 */
function HasMoreElements() {
    //console.debug('HasMoreElements()');
    if (lastStreamElement == null) {
        return false;
    }
    return true;
}