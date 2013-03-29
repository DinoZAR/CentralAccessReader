// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Insert my CSS first
chrome.tabs.insertCSS(null, { file: "npa-toolbar.css" }, function () {
    if (chrome.extension.lastError) {
        message.innerText = 'Could not inject CSS into this page.';
    }
    else {
        message.innerText = 'Inserted style!';
    }
});

// Then, insert my Javascript that handles the toolbar


// Then, insert my HTML constituting my toolbar
//var toolbarHTML = chrome.extension.getURL("toolbar.html");

//var request = new XMLHttpRequest();
//request.open("GET", toolbarHTML, false);
//request.send(null);

//var toolbar = document.createElement('div');
//toolbar.innerHTML = request.responseText;

//// Add all children of the toolbar into the document
//for (var i = 0; i < toolbar.childNodes.length; i++) {
//    document.body.appendChild(toolbar.childNodes[i]);
//}