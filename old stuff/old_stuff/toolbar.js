// See if I have a toolbar already present
var myToolbar = document.getElementById("nifty-prose-articulator-toolbar");

if (myToolbar === null) {

    // Changing everything on website that has position:absolute and pushing it down
    // These elements I can't just push down with a div tag
    var all = document.getElementsByTagName("*");
    for (var i = 0; i < all.length; i++) {
        if (all[i].style.position == "absolute") {

            console.log("Found an absolute-positioned element!");

            all[i].style.top = "46px";
            //        var before = parseInt(all[i].style.top);
            //        if (before == NaN) {
            //            console.log("Setting default position...");
            //            all[i].style.top = "46px";
            //        }
            //        else {
            //            console.log("Setting position...");
            //            all[i].style.top = (before + 46) + "px";       // May need to be changed depending on stylesheet
            //        }
        }
    }

    console.log("Creating contents of toolbar!");

    // Inject contents of my toolbar.html
    var toolbarHTML = chrome.extension.getURL("toolbar.html");

    var request = new XMLHttpRequest();
    request.open("GET", toolbarHTML, false);
    request.send(null);

    var toolbar = document.createElement('div');
    toolbar.innerHTML = request.responseText;

    // Add all children of the toolbar into the document
    for (var i = 0; i < toolbar.childNodes.length; i++) {
        document.body.appendChild(toolbar.childNodes[i]);
    }

    console.log("Inserting icons into buttons...");

    // Add icons to the buttons while also applying onclick handlers
    addButtonImage("npa-play", "play.png");
    addButtonImage("npa-stop", "stop.png");
    addButtonImage("npa-rewind", "rewind.png");
    addButtonImage("npa-fast-forward", "fast-forward.png");
    addButtonImage("npa-close", "close.png");

    // Finally, add buffer div element to move it down some
    var buffer = document.createElement("div");
    var attr = document.createAttribute("id");
    attr.nodeValue = "nifty-prose-articulator-buffer";
    buffer.setAttributeNode(attr);

    document.body.insertBefore(buffer, document.body.firstChild);

}

else {

    // Find my toolbar root and remove it
    myToolbar.parentNode.removeChild(myToolbar);

    // Find buffer and remove it
    var myBuffer = document.getElementById("nifty-prose-articulator-buffer");
    myBuffer.parentNode.removeChild(myBuffer);

}


function addButtonImage(buttonID, iconURL) {

    var icon = document.createElement("img");
    var iconClass = "npa-button-icon";

    // Create attributes for that image

    // URL
    var attr = document.createAttribute("src");
    attr.nodeValue = chrome.extension.getURL(iconURL);
    icon.setAttributeNode(attr);

    // CSS Button Class
    attr = document.createAttribute("class");
    attr.nodeValue = iconClass
    icon.setAttributeNode(attr);

    // onclick handler (just sends message to background.js containing name of button)
    attr = document.createAttribute("onclick");
    attr.nodeValue = "chrome.extension.sendMessage({message: '" + buttonID + "'})";
    icon.setAttributeNode(attr);

    // Add image to the button
    var parent = document.getElementById(buttonID);
    parent.appendChild(icon);

}