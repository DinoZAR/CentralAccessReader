import React from 'react';

import { StyleSheet, css } from '../styles/aphrodite';
import constants from '../styles/constants';

class ButtonBar extends React.Component {
  render() {
    return (
      <div className={css(styles.bar)}>
        <button className={css(styles.button)}>
          <i className="fa fa-play fa-3x" />
        </button>
        <button className={css(styles.button)}>
          <i className="fa fa-cog fa-3x" />
        </button>
        <button className={css(styles.button)}>
          <i className="fa fa-music fa-3x" />
        </button>
        <div className={css(styles.smallSpacer)} />
        <button className={css(styles.button)}>
          <i className="fa fa-search-plus fa-3x" />
        </button>
        <button className={css(styles.button)}>
          <i className="fa fa-search-minus fa-3x" />
        </button>
        <button className={css(styles.button)}>
          <i className="fa fa-search fa-3x" />
        </button>
        <div className={css(styles.restSpacer)} />
        <button className={css(styles.button)}>
          <i className="fa fa-columns fa-3x" />
        </button>
      </div>
    );
  }
}

const styles = StyleSheet.create({
  bar: {
    backgroundColor: constants.lighterBackgroundColor,
    display: 'flex',
    flexDirection: 'column',
    width: '5rem',
    height: '100%',
    boxShadow: constants.panelShadow,
  },
  button: {
    height: '4rem',
    backgroundColor: constants.lighterBackgroundColor,
    color: 'white',
    border: 'none',
    ':hover': {
      backgroundColor: constants.primaryColor,
      cursor: 'pointer',
    }
  },
  smallSpacer: {
    flexGrow: 1,
    maxHeight: '4rem'
  },
  restSpacer: {
    flexGrow: 1,
  }
});

export default ButtonBar;