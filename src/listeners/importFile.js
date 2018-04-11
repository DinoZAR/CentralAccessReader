import { dialog, BrowserWindow } from 'electron';

export default function importFile() {
  return new Promise((resolve, reject) => {
    const window = BrowserWindow.getFocusedWindow();
    const files = dialog.showOpenDialog(window, {
      properties: ['openFile', 'multiSelections']
    });
    resolve('The files on main is:' + files.join(', '));
  });
}