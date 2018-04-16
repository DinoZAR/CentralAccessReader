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
            id: 1,
            type: 'paragraph',
            content: [
                {
                    id: 1,
                    type: 'text',
                    content: 'Some text to show.',
                    format: [
                        { type: 'bold', start: 5, end: 9 }
                    ]
                },
                {
                    id: 2,
                    type: 'math',
                    content: '<some MathML>',
                },
                {
                    id: 3,
                    type: 'image',
                    content: '<file URL>',
                },
            ]
        },
        {
            id: 2,
            type: 'header',
            level: 1 <from 1 to 6>
            content: [...same as paragraph]
        },
        {
            id: 3,
            type: 'mathParagraph',
            content: '<some MathML>'
        },
        ...more paragraphs
        {
            id: 4,
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
4. Specific importer uses the doc builder to convert the content from the file to the the content CAR expects. It processes the entire file.
5. Doc builder will automatically chunk the content and ID everything that needs an ID, saving it to temp.
6. Doc interface will handle fetching chunks from this temp folder.

# Doc Builder

To separate how to convert the content and how to load the content, a doc builder is used, which builds up the document sequentially. The doc build will handle generating the document data structure, chunking, and the method in which it resolves deferred content.

The API will look like this:

* .paragraph({ content: <paragraphObject> }) - Returns a `Paragraph` instance which has the following fields
   - .text({ content })
   - .image({ url, deferred: false, deferredData: {} }) - If deferred, the url will be resolved later via a deferred event
   - .math({ mathml, deferred: false, deferredData: {} }) - If deferred, the MathML will be resolved later via a deferred event
* .mathParagraph({ mathml, deferred: false, deferredData: {} }) - If deferred, the MathML will be resolved later via a deferred event

## Adding deferred content

Certain items take significantly longer to process than other items, and it may make more sense to load these resources dynamically instead of right when the file is imported. This notably includes images and math equations.

The doc builder will support this by parameters that specify that its deferred. Something like this:

`builder.math({ deferred: true, deferredData: { ...data importer needs to resolve it }})`

Then, when we need it, it will pass an event to the importer with the `data` supplied in the parameter. The importer will then process it and return the object they would have supplied to the builder function. For instance, for math, it would return `{ mathml: <MathML string> }`. For an image, `{ url: <url of the image> }`. This way if there are more parameters in the future, they would only need to be added to the event handler.

The event data will be an object of form `{ type: <mathParagraph, math, or image>, data: <what was in deferredData>}`.

