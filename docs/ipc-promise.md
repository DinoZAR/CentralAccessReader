# IPC As Promises

The native Node IPC system is event-based, which can be a huge pain to orchestrate correctly with other async events. To manage it, both the renderer and main will use the Promise-based version of the API.

The renderer will have `send(eventName, args) -> Promise` and the main process will have `on(eventName, Promise)`. The promise in `on()` will be supplied the args from the event.