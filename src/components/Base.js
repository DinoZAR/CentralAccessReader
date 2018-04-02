import React from 'react';
import { StyleSheet, css } from '../styles/aphrodite';

class Base extends React.Component {
  render() {
    return (
      <div className={css(styles.globals, styles.base)}>
        <h1>Something</h1>
      </div>
    );
  }
}

const styles = StyleSheet.create({
  base: {
    backgroundColor: '#515960',
    height: '100%',
  }
});

export default Base;
