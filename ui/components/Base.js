import React from 'react';
import { StyleSheet, css } from '../styles/aphrodite';

import constants from '../styles/constants';
import ButtonBar from './ButtonBar';
import DocumentView from './DocumentView';
import car from '../car';

console.log(car.hello());

class Base extends React.Component {
  render() {
    return (
      <div className={css(styles.base)}>
        <div style={{ flexShrink: 0 }}>
          <ButtonBar />
        </div>
        <div style={{ flex: '1 1 100%' }}>
          <DocumentView  />
        </div>
      </div>
    );
  }
}

const styles = StyleSheet.create({
  base: {
    backgroundColor: constants.backgroundColor,
    height: '100%',
    display: 'flex',
    flexDirection: 'row',
  }
});

export default Base;
