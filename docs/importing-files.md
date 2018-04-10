# Importing Files

The file processing itself will happen in the backend, which will communicate with the frontend via handles.

Generally speaking:

1. Frontend will show file picker
2. The selected file path is given to the backend
3. Backend chooses import function based on file extension
4. Backend compiles data to conform to document interface
5. Backend returns the document handle as Promise
6. Frontend uses handle to download chunks and everything else it needs

## Document Data Structure

    [
        {
            type: 'paragraph',
            content: [
                {
                    type: 'text',
                    content: 'Some text to show.',
                    format: [
                        { type: 'bold', start: 5, end: 9 }
                    ]
                },
                {
                    type: 'math',
                    content: '<some MathML>',
                },
                {
                    type: 'image',
                    content: '<file URL>',
                },
            ]
        },
        {
            type: 'header',
            level: 1 <from 1 to 6>
            content: [...same as paragraph]
        },
        {
            type: 'mathParagraph',
            content: '<some MathML>'
        },
        ...more paragraphs
        {
            type: 'paragraph',
            content: [...],
        }
    ]

# File Importer Flow

1. Frontend gets file path from file picker or via drag and drop
2. Calls importer function
  * Provides callback for handling importing events, like progress
  * Returns a Promise
3. Importer finds specific importer to use for the file by its extension
4. Specific importer implements interface to stream content. Sometimes it's simply "all of it", but for larger files, it will render content on demand.

## Stream Interface

The importer object will stick around in memory, tied in lifecycle to the document that's being viewed. If the document is closed, the importer is cleaned up. Otherwise, it sticks around to stream content from the document to the view.

Every importer is given temp space to save or cache whatever they need to from the file. The temp space also will have the same lifecycle as the importer.

The importer must implement:

* `length()`: the length of the file in chunks
* ...other things