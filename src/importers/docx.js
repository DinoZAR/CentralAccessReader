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
    // console.log('key:', key);
    // console.log(xmlString);
    const doc = new xmldoc.XmlDocument(xmlString);
    return resolve({ key, xml: doc });
  });
}

function parseDocumentXML(entries, tmpFolder) {
  const parseXMLs = Object.entries(entries).map(([key, value]) => parseXML(key, value));

  return Promise.all(parseXMLs)
    .then(xmls => xmls.reduce((accum, { key, xml }) => ({ ...accum, [key]: xml }), {}))
    .then(xmls => parseDocument(xmls, tmpFolder));
}

function parseImage(elem, builder, xmls) {
  // Get image info
  const blipFill = elem.descendantWithPath('wp:inline.a:graphic.a:graphicData.pic:pic.pic:blipFill');
  const id = blipFill.childNamed('a:blip').attr['r:embed'];

  // Lookup URL
  const rel = xmls.rels.childWithAttribute('Id', id);
  const url = rel.attr['Target'];

  builder.image({
    deferred: true,
    deferredData: { zipURL: url, altText: '' },
  });
}

function parseRow(elem, builder, xmls) {
  elem.children.forEach((child) => {
    switch (child.name) {
      case 'w:t':
        return builder.text({ content: child.val });
      case 'w:drawing':
        return parseImage(child, builder, xmls);
      default:
        return;
    }
  });
}

function parseParagraph(elem, builder, xmls) {
  builder.paragraph();
  elem.children.forEach((child) => {
    switch (child.name) {
      case 'w:r':
        return parseRow(child, builder, xmls);
      default:
        return;
    }
  });
}

function parseDocument(xmls, tmpFolder) {
  const body = xmls.document.childNamed('w:body');
  const builder = new DocBuilder(tmpFolder);
  builder.build((build) => {
    body.children.forEach((elem) => {
      switch (elem.name) {
        case 'w:p':
          return parseParagraph(elem, build, xmls);
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