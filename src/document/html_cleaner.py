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
import re

def clean(htmlElem, progressHook=None, cancelHook=None):
    '''
    Receives an HTML element and cleans it up, returning the cleaned HTML
    element in return
    '''
    if progressHook is not None:
        progressHook(0, 'Cleaning up styling...')
    _deleteStyles(htmlElem)
    if cancelHook is not None:
        if cancelHook():
            return htmlElem
        
    if progressHook is not None:
        progressHook(20, 'Cleaning up empty images...')
    _delete1x1Images(htmlElem)
    if cancelHook is not None:
        if cancelHook():
            return htmlElem
    
    if progressHook is not None:
        progressHook(40, 'Cleaning up buttons and text fields...')    
    _deleteInputControls(htmlElem)
    if cancelHook is not None:
        if cancelHook():
            return htmlElem
    
    if progressHook is not None:
        progressHook(60, 'Cleaning up spans...')    
    htmlElem = _deleteSpans(htmlElem)
    if cancelHook is not None:
        if cancelHook():
            return htmlElem
    
    if progressHook is not None:
        progressHook(80, 'Cleaning up line breaks...')
    htmlElem = _deleteLineBreaks(htmlElem)
    if cancelHook is not None:
        if cancelHook():
            return htmlElem
    
    if progressHook is not None:
        progressHook(95, 'Cleaning up image attributes...')    
    _stripImageAttributes(htmlElem)
    
    return htmlElem

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
    content = html.tostring(elem)
    p = re.compile('<span[^>]*>')
    p.sub('', content)
    content = content.replace('</span>', '')
    return html.fromstring(content)

def _deleteLineBreaks(elem):
    '''
    Removes all line break elements, also known as <br> and </br>. The
    content providers should have used paragraph styles.
    '''
    content = html.tostring(elem)
    content = content.replace('<br>', '').replace('</br>', '')
    return html.fromstring(content)

def _stripImageAttributes(elem):
    '''
    For all of the images, strip all of its attributes besides its src.
    '''
    for img in elem.xpath('//img'):
        for k in img.attrib.keys():
            if k.lower() != 'src':
                img.attrib.pop(k)