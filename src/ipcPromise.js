import { ipcMain, ipcRenderer } from 'electron';

function successMessage(eventName) {
  return eventName + '__success';
}

function failedMessage(eventName) {
  return eventName + '__failed';
}

let ID_COUNTER = 0;

export function send(eventName, ...args) {
  const successEvent = successMessage(eventName);
  const failedEvent = failedMessage(eventName);
  const id = ID_COUNTER;
  ID_COUNTER += 1;

  return new Promise((resolve, reject) => {
    const onSuccess = (event, response) => {
      if (response.id !== id || response.eventName !== eventName) {
        return;
      }
      ipcRenderer.removeListener(successEvent, onSuccess);
      ipcRenderer.removeListener(failedEvent, onFailed);
      resolve(response.data);
    };

    const onFailed = (event, response) => {
      if (response.id !== id || response.eventName !== eventName) {
        return;
      }
      ipcRenderer.removeListener(successEvent, onSuccess);
      ipcRenderer.removeListener(failedEvent, onFailed);
      reject(response.data);
    };

    ipcRenderer.on(successEvent, onSuccess);
    ipcRenderer.on(failedEvent, onFailed);

    ipcRenderer.send(eventName, {
      data: args,
      eventName,
      id,
    });
  });
}

export function on(eventName, listener) {
  const successEvent = successMessage(eventName);
  const failedEvent = failedMessage(eventName);

  ipcMain.on(eventName, (event, args) => {
    listener.apply(null, args.data).then((data) => {
      event.sender.send(successEvent, {
        data,
        id: args.id,
        eventName,
      });
    }).catch((data) => {
      event.sender.send(failedEvent, {
        data,
        id: args.id,
        eventName,
      });
    });
  });
}
