import yauzl from 'yauzl';
import { parseString } from 'xml2js';

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
    parseString(xmlString, (err, result) => {
      if (err) {
        return reject(err);
      }
      return resolve({ key, xml: result });
    });
  });
}

function parseDocumentXML(entries, tmpFolder) {
  const parseXMLs = Object.entries(entries).map(([key, value]) => parseXML(key, value));

  return Promise.all(parseXMLs)
    .then((xmls) => xmls.reduce((accum, { key, xml }) => ({ ...accum, [key]: xml }), {}))
    .then(doc => parseDocument(doc));
}

function parseDocument(doc) {
  console.log(doc.document['w:document']['w:body']);
  return doc.document;
}

export default function importDoc(filePath, tmpFolder) {
  return getFileEntries(filePath, tmpFolder)
    .then(entries => parseDocumentXML(entries, tmpFolder));
}