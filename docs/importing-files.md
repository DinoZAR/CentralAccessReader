# Importing Files

The file processing itself will happen in the backend, which will communicate with the frontend via handles.

Generally speaking:

1. Frontend will show file picker
2. The selected file path is given to the backend
3. Backend chooses import function based on file extension
4. Backend compiles data to conform to document interface
5. Backend returns the document handle as Promise
6. Frontend uses handle to download chunks and everything else it needs

A big part of this is the document interface, which determines the set of features the frontend can do to a document.

## Document Interface

The document behavior will be the same for all file types. The only difference is the content, which will be a JSON structure.

The overall layout of the content is this:

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
    ]

It's a very similar layout to how Word documents are organized. Once a file importer converts the document to this format, it's given over to the document interface which works with this structure to generate TTS, split into chunks, and other things.