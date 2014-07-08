'''
Created on Dec 16, 2013

This module will help me cleanup the junk from the HTML. It will get rid of
styles that we don't need, destroy any conflicting CSS, and other things.

To use it, do the following:
import html_cleaner
html_cleaner.clean(myHtmlElem)

@author: Spencer Graffe
'''
from lxml import html

def clean(htmlElem, progressHook=None, cancelHook=None):
    '''
    Receives an HTML element and cleans it up, returning the cleaned HTML
    element in return.
    '''

    # Do some preprocessing first
    myHtml = _removeLineEndingsInsideText(htmlElem)

    tasks = [
        (_deleteStyles, 'Cleaning up styling...'),
        (_delete1x1Images, 'Deleting empty images...'),
        (_deleteInputControls, 'Deleting buttons and text fields...'),
        (_deleteSpans, 'Deleting spans...'),
        (_deleteLineBreaks, 'Deleting line breaks...'),
        (_deleteEmptyParagraphs, 'Deleting empty paragraphs...'),
        (_stripImageAttributes, 'Cleaning up image attributes...'),
        (_stripAnchorAttributes, 'Cleaning up anchor attributes...')]

    for i in range(len(tasks)):
        if cancelHook is not None:
            if cancelHook():
                break
        if progressHook is not None:
            progressHook(int(float(i) / len(tasks) * 100), tasks[i][1])
        tasks[i][0](myHtml)
    
    return myHtml

def _removeLineEndingsInsideText(htmlElem):
    '''
    Deletes line endings inside of the text elements in HTML. These characters
    have no purpose in layout and display while hampering the TTS engine's
    ability to read it correctly.
    '''
    htmlString = html.tostring(htmlElem, pretty_print=False)
    htmlString = htmlString.replace('\r', '')
    htmlString = htmlString.replace('\n', ' ')
    return html.fromstring(htmlString)

def _deleteStyles(elem):
    '''
    Deletes all of the style information in this element and all elements
    underneath it.
    '''
    for bad in elem.xpath("//*[@style]"):
        bad.attrib.pop('style')
            
def _delete1x1Images(elem):
    '''
    Deletes all 1x1 images in the document. Nobody is going to see them.
    '''
    for bad in elem.xpath("//img[@width='1']"):
        bad.getparent().remove(bad)

def _deleteInputControls(elem):
    '''
    Deletes all input and form-like controls in the HTML, like textboxes and
    buttons.
    '''
    for bad in elem.xpath('//input | //textarea | //button'):
        bad.getparent().remove(bad)
        
def _deleteSpans(elem):
    '''
    Removes all spans from the element and its children. The content of the
    spans will be preserved, but the span tags themselves will not be.
    '''
    
    spans = elem.xpath('.//span')
    for s in spans:
        # If it has text, add to tail of previous element or to text of parent
        if s.text is not None:
            if s.getprevious() is not None:
                if s.getprevious().tail is not None:
                    s.getprevious().tail += s.text
                else:
                    s.getprevious().tail = s.text
            else:
                if s.getparent().text is not None:
                    s.getparent().text += s.text
                else:
                    s.getparent().text = s.text
        
        # Get all child elements out
        for child in s:
            s.addprevious(child)

        # Make sure that I get the tail too!
        previousElem = s.getprevious()
        if s.tail is not None:
            if previousElem is not None:
                if child.tail is not None:
                    child.tail += s.tail
                else:
                    child.tail = s.tail
            else:
                if s.getparent() is not None:
                    if s.getparent().text is not None:
                        s.getparent().text += s.tail
                    else:
                        s.getparent().text = s.tail
        
        # Remove the span
        s.getparent().remove(s)
    
def _deleteLineBreaks(elem):
    '''
    Removes all line break elements, also known as <br> and </br>. The
    content providers should have used paragraph styles.
    '''
    content = html.tostring(elem)
    content = content.replace('<br>', '').replace('</br>', '')
    return html.fromstring(content)

def _deleteEmptyParagraphs(elem):
    '''
    Removes all empty <p>'s
    '''
    paras = elem.xpath('.//p')
    for p in paras:
        shouldDelete = (len(p) == 0) and (p.text is None)
        
        if shouldDelete:
            
            # Check for tail and adjust it appropriately
            if p.tail is not None:
                if p.getprevious() is not None:
                    if p.getprevious().tail is not None:
                        p.getprevious().tail += p.tail
                    else:
                        p.getprevious().tail = p.tail
                else:
                    if p.getparent().text is not None:
                        p.getparent().text += p.tail
                    else:
                        p.getparent().text = p.tail
            
            # Now remove the paragraph
            p.getparent().remove(p)
        
        else:
            
            # Might as well do some cleanup, like classes and styles
            if 'class' in p.attrib:
                p.attrib.pop('class')
            
            if 'style' in p.attrib:
                p.attrib.pop('style')
            

def _stripImageAttributes(elem):
    '''
    For all of the images, strip all of its attributes besides its car.
    '''
    VALID_ATTRIBUTES = ['src', 'alt', 'title']

    for img in elem.xpath('//img'):
        for k in img.attrib.keys():
            if k not in VALID_ATTRIBUTES:
                img.attrib.pop(k)

def _stripAnchorAttributes(elem):
    '''
    Strips attributes from a <a> tag that are not directly related to its
    purpose.
    '''
    VALID_ATTRIBUTES = ['href', 'download', 'media', 'name', 'rel', 'target', 'type']

    for anchor in elem.xpath('//a'):
        for k in anchor.attrib.keys():
            if k not in VALID_ATTRIBUTES:
                anchor.attrib.pop(k)