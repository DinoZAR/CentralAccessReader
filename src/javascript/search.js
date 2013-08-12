/*
 * Search Functions
 * 
 * @author Spencer Graffe
 */
lastSearchElement = null;
lastSearchOffset = 0;

/**
 * Finds the next search term, highlights it, and moves the view to it, if any. 
 * If after is true, it will find word after current. Otherwise, search for text 
 * before. Returns true if it found something, false if it didn't.
 * @param myText
 * @param after
 * @param wholeWord
 * @param matchCase
 * @returns
 *  
 */
function SearchForText(myText, after, wholeWord, matchCase) {
	//console.debug('SearchForText()');
	if (after) {
		return SearchTextForward(myText, wholeWord, matchCase, false);
	}
	else {
		return SearchTextBackward(myText, wholeWord, matchCase, false);
	}
}

/**
 * Resets the states that are used by the search feature. 
 */
function ResetSearchStates() {
    lastSearchElement = null;
    lastSearchOffset = 0;
}

/**
 * Searches for text backwards.
 * @param myText
 * @param wholeWord
 * @param matchCase
 * @param alreadyWrapped
 * @returns
 */
function SearchTextBackward(myText, wholeWord, matchCase, alreadyWrapped) {
    //console.debug('SearchTextBackward()');
	var currentNode = null;
	if (!(highlight === null)) {
		currentNode = PreviousElement(highlight);
	}
	else {
		currentNode = document.body.lastChild;
	}
	
	while (true) {
		if (currentNode.nodeType == 3) {
			var lastIndex = -1;
			var first = true;
			var index = 1000;
			currentSearch = '';
			if (matchCase == true) {
				currentSearch = currentNode.data;
			}
			else {
				currentSearch = currentNode.data.toLowerCase();
			}
			
			// Create the regular expression I need based on settings
			re = '';
			if (matchCase == true) {
				re = new RegExp('\\b' + myText + '\\b', 'g');
			}
			else {
				re = new RegExp('\\b' + myText.toLowerCase() + '\\b', 'g');
			}
			
			while (index >= 0) {
				index = currentSearch.search(re);
				if (index >= 0) {
					if (first) {
						lastIndex = index;
						first = false;
					}
					else {
						lastIndex += index + myText.length;
					}
					currentSearch = currentSearch.substring(index + myText.length);
				}
			}
			if (lastIndex >= 0) {
				// Get the highlight to surround what I found
				var range = document.createRange();
				lastSearchElement = currentNode;
				lastSearchOffset = lastIndex;
				startFromSearch = true;
				range.setStart(currentNode, lastIndex);
				range.setEnd(currentNode, lastIndex + myText.length);
				SetHighlight(range, false);
				ScrollToHighlight(true);
				return true;
			}
		}
		currentNode = PreviousElement(currentNode);
		if (currentNode === null) {
			// Start over from the back if I haven't already
			if ((alreadyWrapped == false)) {
				ClearAllHighlights();
				return SearchTextBackward(myText, wholeWord, matchCase, true);
			}
			return false;
		}
	}
}

/**
 * Searches for text forward.
 * @param myText
 * @param wholeWord
 * @param matchCase
 * @param alreadyWrapped
 * @returns
 */
function SearchTextForward(myText, wholeWord, matchCase, alreadyWrapped) {
    //console.debug('SearchTextForward()');
	// Determing the starting point
	var currentNode = null;
	if (!(highlight === null)) {
		currentNode = NextElement(highlight);
	}
	else {
		currentNode = document.body.firstChild;
	}
	
	// Create the regular expression I need based on settings
	re = '';
	if (matchCase == true) {
		re = new RegExp('\\b' + myText + '\\b', 'g');
	}
	else {
		re = new RegExp('\\b' + myText.toLowerCase() + '\\b', 'g');
	}
	
	while (true) {
		if (currentNode.nodeType == TEXT_NODE) {
			var index = -1;
			if (matchCase == true) {
				index = currentNode.data.search(re);
			}
			else {
				index = currentNode.data.toLowerCase().search(re);
			}
			if (index >= 0) {
				// Get the highlight to surround what I found
				var range = document.createRange();
				lastSearchElement = DeepestChild(currentNode);
				lastSearchOffset = index;
				startFromSearch = true;
				range.setStart(currentNode, index);
				range.setEnd(currentNode, index + myText.length);
				SetHighlight(range, false);
				ScrollToHighlight(true);
				return true;
			}
		}
		currentNode = NextElement(currentNode);
		if (currentNode === null) {
			// Start over from the back if I haven't already
			if ((alreadyWrapped == false)) {
				ClearAllHighlights();
				return SearchTextForward(myText, wholeWord, matchCase, true);
			}
			return false;
		}
	}
}