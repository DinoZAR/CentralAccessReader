import yauzl from 'yauzl';
import xmldoc from 'xmldoc';

import DocBuilder from '../doc-builder';

const ENTRIES_NEEDED = new Map([
  ['word/_rels/document.xml.rels', 'rels'],
  ['word/document.xml', 'document'],
  ['word/numbering.xml', 'numbering'],
  ['word/styles.xml', 'styles'],
]);

function streamToString(stream, callback) {
  const chunks = [];
  stream.on('data', (chunk) => {
    chunks.push(chunk.toString());
  });
  stream.on('end', () => {
    callback(chunks.join(''));
  });
}

function getFileEntries(filePath) {
  return new Promise((resolve, reject) => {
    const entries = {};

    yauzl.open(filePath, null, (err, zipFile) => {
      if (err) {
        return reject(err);
      }

      zipFile.on('entry', (entry) => {
        if (ENTRIES_NEEDED.has(entry.fileName)) {
          zipFile.openReadStream(entry, (err, readStream) => {
            streamToString(readStream, (contents) => {
              entries[ENTRIES_NEEDED.get(entry.fileName)] = contents;
            });
          });
        }
      });

      zipFile.on('close', () => {
        resolve(entries);
      });
    });
  });
}

function parseXML(key, xmlString) {
  return new Promise((resolve, reject) => {
    const doc = new xmldoc.XmlDocument(xmlString);
    return resolve({ key, xml: doc });
  });
}

function parseDocumentXML(entries, tmpFolder) {
  const parseXMLs = Object.entries(entries).map(([key, value]) => parseXML(key, value));

  return Promise.all(parseXMLs)
    .then(xmls => xmls.reduce((accum, { key, xml }) => ({ ...accum, [key]: xml }), {}))
    .then(doc => parseDocument(doc, tmpFolder));
}

function parseRow(elem, builder) {
  elem.children.forEach((child) => {
    switch (child.name) {
      case 'w:t':
        return builder.text({ content: child.val });
      default:
        return;
    }
  });
}

function parseParagraph(elem, builder) {
  builder.paragraph();
  elem.children.forEach((child) => {
    switch (child.name) {
      case 'w:r':
        return parseRow(child, builder);
      default:
        return;
    }
  });
}

function parseDocument(doc, tmpFolder) {
  const body = doc.document.childNamed('w:body');
  const builder = new DocBuilder(tmpFolder);
  builder.build((build) => {
    body.children.forEach((elem) => {
      switch (elem.name) {
        case 'w:p':
          return parseParagraph(elem, build);
        default:
          return;
      }
    });
  });
}

export default function importDoc(filePath, tmpFolder) {
  return getFileEntries(filePath, tmpFolder)
    .then(entries => parseDocumentXML(entries, tmpFolder));
}