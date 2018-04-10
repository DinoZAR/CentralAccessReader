import { ipcMain } from 'electron';

ipcMain.on('import-file-message', (event, filePath) => {
  console.log('The file path:', filePath);
  event.sender.send('import-file-reply', 'stuff');
});
