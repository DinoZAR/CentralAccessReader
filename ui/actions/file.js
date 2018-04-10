import { remote, ipcRenderer } from 'electron';

export function openFile() {
  return (dispatch) => {
    const files = remote.dialog.showOpenDialog({
      properties: ['openFile', 'multiSelections']
    });

    ipcRenderer.send('import-file-message', files);
  }
}