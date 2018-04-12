import { dialog, BrowserWindow } from 'electron';
import importer from '../importers';

export default function importFile() {
  return new Promise((resolve, reject) => {
    const window = BrowserWindow.getFocusedWindow();
    const file = dialog.showOpenDialog(window, {
      properties: ['openFile']
    });
    if (file) {
      try {
        const result = importer(file[0]);
        if (result.success) {
          return resolve({
            status: 'success',
            content: result.content,
          });
        }
        return reject({
          status: 'failed',
          error: result.error,
        });
      } catch (err) {
        return reject({
          status: 'failed',
          error: err.toString(),
        });
      }
    }
    return resolve({
      status: 'canceled'
    });
  });
}