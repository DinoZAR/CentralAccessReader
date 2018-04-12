import path from 'path';
import temp from 'temp';

import importDoc from './doc';

// Cleanup temp directories on process exit
temp.track();

const EXT_IMPORTER = {
  '.docx': importDoc,
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