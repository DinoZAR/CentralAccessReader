import { remote } from 'electron';

export function openFile() {
  return (dispatch) => {
    const file = remote.dialog.showOpenDialog({
      properties: ['openFile', 'multiSelections']
    });


  }
}