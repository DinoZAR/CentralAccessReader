var lastStreamElement = null;

// DEBUG PURPOSES
// Gives me the beginning to work with
function SetStreamBeginning() {
    range = GetSelectionRange();
    lastStreamElement = DeepestChild(range.startContainer);
    myRange = document.createRange();
    myRange.selectNode(lastStreamElement);
    return GetHTMLSource(myRange);
}

// Gets the next element content to read. Returns a string representing the
// HTML content.
function StreamNextElement() {
    console.debug('StreamNextElement()');
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

function HasMoreElements() {
    if (lastStreamElement == null) {
        return false;
    }
    return true;
}