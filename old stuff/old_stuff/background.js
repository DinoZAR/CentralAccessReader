// Register my browser action listener
chrome.browserAction.onClicked.addListener(injectContents);
chrome.extension.onMessage.addListener();


// This will be called when the extension button is pressed
function injectContents(tab) {

    // Insert my CSS first (now handled by the manifest)
//    chrome.tabs.insertCSS(null, { file: "npa-toolbar.css" }, function () {
//        if (chrome.extension.lastError) {
//            console.error('Could not inject CSS into this page.');
//        }
//        else {
//            console.log('CSS injection successful!');
//        }
//    });
    // Insert my Javascript that handles the toolbar (a content script)
    chrome.tabs.executeScript(null, { file: "toolbar.js" }, function () {
        if (chrome.extension.lastError) {
            console.error('Could not inject Javascript into this page.');
        }
        else {
            console.log("Javascript injection successful!");
        }
    });
}


function toolbarListener(message, sender) {

    console.log("Message received!");
    console.log(message);

}