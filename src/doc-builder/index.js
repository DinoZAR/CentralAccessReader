import fs from 'fs';
import path from 'path';

/**
 * Builds up a document and saves the chunks to the temp directory.
 *
 * @param {string} tmpFolder - Folder that was allocated from the importer
 */
function DocBuilder(tmpFolder) {
  this.tmpFolder = tmpFolder;
  this.idCounter = 0;
  this.chunkCounter = 0;
  this.content = [];

  this.paragraphInfo = null;
  this.paragraphContent = [];
}

DocBuilder.prototype.__newID = function() {
  this.idCounter += 1;
  return this.idCounter;
};

DocBuilder.prototype.__newChunkID = function() {
  const prevID = this.chunkCounter;
  this.chunkCounter += 1;
  return prevID;
};

DocBuilder.prototype.__writeParagraph = function() {
  this.content.push({
    ...this.paragraphInfo,
    content: this.paragraphContent,
  });
  this.paragraphInfo = null;
  this.paragraphContent = [];
};

DocBuilder.prototype.__writeChunk = function() {
  const id = this.__newChunkID();
  fs.writeFile(
    path.join(this.tmpFolder, '__chunks', `${id}.json`),
    JSON.stringify(this.content),
    (err) => {
      if (err) throw err;
    }
  );
};

DocBuilder.prototype.__done = function() {
  this.__writeParagraph();
  this.__writeChunk();
};

DocBuilder.prototype.build = function(buildFunc) {
  buildFunc(this);
  this.__done();
};

DocBuilder.prototype.paragraph = function() {
  this.paragraphInfo = {
    id: this.__newID(),
    type: 'paragraph',
  };
};

DocBuilder.prototype.text = function({ content }) {
  this.paragraphContent.push({
    id: this.__newID(),
    type: 'text',
    content,
  });
};

DocBuilder.prototype.math = function({ mathml }) {
  this.paragraphContent.push({
    id: this.__newID(),
    type: 'math',
    mathml,
  });
};

DocBuilder.prototype.image = function({ url }) {
  this.paragraphContent.push({
    id: this.__newID(),
    type: 'image',
    url,
  });
};

export default DocBuilder;