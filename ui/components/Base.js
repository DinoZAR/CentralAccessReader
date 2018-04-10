import React from 'react';

import { StyleSheet, css } from '../styles/aphrodite';
import constants from '../styles/constants';

import ButtonBar from './ButtonBar';
import DocumentPanel from './document/DocumentPanel';
import DocumentTabsContainer from '../containers/DocumentTabsContainer';
import Tabs from './Tabs';
import car from '../car';

class Base extends React.Component {
  render() {
    return (
      <div className={css(styles.base)}>
        <div style={{ flexShrink: 0, zIndex: 2 }}>
          <ButtonBar />
        </div>
        <div style={{ flex: '1 1 100%', zIndex: 1 }}>
          <DocumentTabsContainer
            showAdd
            tabs={[]}
          />
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
    overflow: 'hidden',
  }
});

export default Base;
