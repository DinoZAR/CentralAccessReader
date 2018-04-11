import { on } from '../ipcPromise';
import importFile from './importFile';

const ipcListeners = {
  'import-file': importFile
};

Object.entries(ipcListeners).forEach(([key, listener]) => {
  on(key, listener);
});