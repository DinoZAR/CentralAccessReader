const DocBuilder = require.requireActual('../index').default;

const TRACKED_CALLS = new Set([
  'paragraph',
  'text',
  'math',
  'image',
]);

const UNTOUCHED_CALLS = new Set([
  'build'
]);

let __calls = [];

function MockBuilder(tmpFolder) {
  DocBuilder.call(this, tmpFolder);
}
MockBuilder.prototype = Object.entries(DocBuilder.prototype).reduce((accum, [funcName, func]) => {
  if (TRACKED_CALLS.has(funcName)) {
    return {
      ...accum,
      [funcName]: function(...params) {
        __calls.push({
          func: funcName,
          params,
        });
      }
    };
  } else if (UNTOUCHED_CALLS.has(funcName)) {
    return {
      ...accum,
      [funcName]: func
    };
  }
  return {
    ...accum,
    [funcName]: () => {}
  };
}, {});

export function calls() {
  return __calls;
}

export function resetCalls() {
  __calls = [];
}

export default MockBuilder;