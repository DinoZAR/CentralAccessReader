import { remote, ipcRenderer } from 'electron';
import { send } from '../../src/ipcPromise';

export function openFile() {
  return (dispatch) => {
    return send('import-file').then((stuff) => {
      console.log('On renderer:', stuff);
    });
  }
}