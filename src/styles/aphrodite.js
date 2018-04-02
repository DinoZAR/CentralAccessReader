import { StyleSheet as SS } from 'aphrodite/no-important';

const innerTagStylesExtension = {
  selectorHandler: (selector, className, generateSubtreeStyles) => {
    if (selector[0] !== '_') {
      return null;
    }
    return generateSubtreeStyles(`${className} ${selector.slice(1)}`);
  }
};

const directInnerTagStylesExtension = {
  selectorHandler: (selector, className, generateSubtreeStyles) => {
    if (selector[0] !== '>') {
      return null;
    }
    return generateSubtreeStyles(`${className} > ${selector.slice(1)}`);
  }
};

const { StyleSheet, css } = SS.extend([
  innerTagStylesExtension,
  directInnerTagStylesExtension,
]);

export { StyleSheet, css };