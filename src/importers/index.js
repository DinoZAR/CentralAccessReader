import path from 'path';
import temp from 'temp';

import importDocx from './docx';

// Cleanup temp directories on process exit
temp.track();

const EXT_IMPORTER = {
  '.docx': importDocx,
};

export default function importFile(filePath) {
  try {
    const ext = path.extname(filePath);
    const tmpDir = temp.mkdirSync();

    if (EXT_IMPORTER[ext]) {
      const content = EXT_IMPORTER[ext](filePath, tmpDir);
      return {
        success: true,
        content,
      };
    }
    return {
      success: false,
      error: `Can't import a ${ext} file.`
    };
  } catch (err) {
    return {
      success: false,
      content: [],
      error: err.toString(),
    };
  }
}