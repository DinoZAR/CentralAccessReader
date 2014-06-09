/*
 * Functions for converting SVGs to PNGs
 * 
 * NOTE: THIS DOES NOT WORK WITH QWEBVIEW. THIS IS FOR DOCUMENTATION IN CASE
 * A DIFFERENT BROWSER IS USED.
 * 
 * @author Spencer Graffe
 */

// Converts an <svg> to an <img> in-place
/**
 * Converts an <svg> to an <img> in-place. This does NOT block for completion.
 */
function ConvertSVGToPNG(svgElem) {
    var myCanvas = document.createElement('canvas');
    var myImage = document.createElement('img');
    
    var context = myCanvas.getContext('2d');
    var svg_xml = (new XMLSerializer()).serializeToString(svgElem);
    
    var svgImage = document.createElement('img');
    svgImage.src = 'data:image/svg+xml;base64,' + btoa(svg_xml);
    
    svgImage.onload = function() {
        myCanvas.width = svgImage.width;
        myCanvas.height = svgImage.height;
        
        context.drawImage(svgImage, 0, 0);
        myImage.src = myCanvas.toDataURL('image/png');
        
        // Replace the svg with image
        svgElem.parentNode.insertBefore(myImage, svgElem.nextSibling);
        svgElem.parentNode.removeChild(svgElem);
        
        alert('SVG replaced!');
    };
}

/**
 * Starts conversion of all SVGs to PNGs. This does NOT block for completion.
 */
function ConvertAllSVGsToPNGs() {
	console.debug('Converting all of the SVGs awesomely');
	$('svg').each(function (index, elem) {
	    ConvertSVGToPNG(elem);
	});
}

/**
 * Returns true if there are no more SVGs, and thus, all images have been
 * converted.
 * @returns
 */
function AreAllSVGsConverted() {
	return $('svg').length != 0;
} 