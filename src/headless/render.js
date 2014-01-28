var page = require('webpage').create();

page.settings.javascriptEnabled = true;
page.settings.loadImages = true;
page.settings.localToRemoteUrlAccessEnabled = true;
page.settings.webSecurityEnabled = false;

var system = require('system')
var url;

if (system.args.length === 1) {
	console.log('Usage: render.js <some URL>');
	phantom.exit();
}

url = system.args[1];

page.onConsoleMessage = function(msg) {
	console.log('<{' + msg);
};

function waitFor(testFx, onReady, timeOutMillis) {
    var maxtimeOutMillis = timeOutMillis ? timeOutMillis : 3000,
        start = new Date().getTime(),
        condition = false,
        interval = setInterval(function() {
            if ( (new Date().getTime() - start < maxtimeOutMillis) && !condition ) {
                condition = (typeof(testFx) === "string" ? eval(testFx) : testFx());
            } else {
                if(!condition) {
                    phantom.exit(1);
                } else {
                    typeof(onReady) === "string" ? eval(onReady) : onReady();
                    clearInterval(interval);
                }
            }
        }, 100);
};

page.open(url, function (status) {
	
    // Check for page load success
    if (status !== "success") {
        console.log("Unable to access URL");
    } else {
        
		// Wait for the math typesetting to complete
        waitFor(function() {
            // Check in the page if a specific element is now visible
            return page.evaluate(function() {
            	console.log('[The Math Typeset Progress Is:' + GetMathTypesetProgress());
                return IsMathTypeset();
            });
        }, function() {
			var myHtml = page.evaluate(function() {
				return document.documentElement.innerHTML;
			});
			console.log('[Exporting the document to HTML]');
			console.log(myHtml);
			phantom.exit();
        },
        30000000);
    }
});