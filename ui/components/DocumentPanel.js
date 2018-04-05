import React from 'react';

import { StyleSheet, css } from '../styles/aphrodite';
import constants from '../styles/constants';

class DocumentPanel extends React.Component {
  render() {
    return (
      <div className={css(styles.window)}>
        <div className={css(styles.panel)}>
          <p>Some cool text to have here</p>
        </div>
      </div>
    );
  }
}

const styles = StyleSheet.create({
  window: {
    display: 'flex',
    flexDirection: 'row',
    justifyContent: 'center',
    width: '100%',
    height: '100%',
  },
  panel: {
    backgroundColor: 'black',
    color: 'white',
    maxWidth: '50rem',
    width: '100%',
    padding: '1rem',
    boxShadow: constants.panelShadow,
  }
});

export default DocumentPanel;
