'''
Created on Mar 3, 2013

@author: Spencer Graffe
'''

def main():
    print 'Starting!'
    
    from headless.renderer import HeadlessRendererThread
    import misc
    import os
    from document.docx.docx_document import DocxDocument
    
    print 'Creating test document...'
    def myProgress(things, stuff):
        pass
    
    def myCancel():
        return False
    
    doc = DocxDocument(misc.program_path('Tutorial.docx'), myProgress, myCancel)    
    
    t = HeadlessRendererThread(doc.getMainPage(mathOutput='svg'))
    t.start()
    
    while t.isRunning():
        pass
    
    with open(os.path.expanduser('~/Desktop/ManyThings.html'), 'w') as f:
        f.write(t.getRenderedHTML())
    
    print 'Done!'

# Just to protect this module when using the process pool
if __name__ == '__main__':
    main()