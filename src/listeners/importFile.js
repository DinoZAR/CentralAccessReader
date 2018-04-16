import { dialog, BrowserWindow } from 'electron';
import importer from '../importers';

export default function importFile() {
  return new Promise((resolve, reject) => {
    const window = BrowserWindow.getFocusedWindow();
    const file = dialog.showOpenDialog(window, {
      properties: ['openFile']
    });
    if (file) {
      return importer(file[0])
        .then((content) => {
          return resolve({
            status: 'success',
            content,
          });
        })
        .catch((err) => {
          return reject({
            status: 'failed',
            error: err.toString(),
          });
        });
    }
    return resolve({
      status: 'canceled'
    });
  });
}