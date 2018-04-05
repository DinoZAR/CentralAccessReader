import React from 'react';
import { StyleSheet, css } from '../styles/aphrodite';

import constants from '../styles/constants';
import ButtonBar from './ButtonBar';
import DocumentPanel from './document/DocumentPanel';
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
          <DocumentPanel
            content={[
              {
                id: 1,
                type: 'paragraph',
                content: [
                  { id: 1, type: 'text', content: 'Here is some text.'},
                  { id: 2, type: 'text', content: 'More text.'},
                ]
              },
              {
                id: 2,
                type: 'header',
                content: [
                  { id: 1, type: 'text', content: 'Here is some text.'},
                  { id: 2, type: 'text', content: 'More text.'},
                ]
              },
              {
                id: 3,
                type: 'paragraph',
                content: [
                  { id: 1, type: 'text', content: 'Here is some text.'},
                  { id: 2, type: 'text', content: 'More text.'},
                  { id: 3, type: 'image', url: 'https://d2kwjcq8j5htsz.cloudfront.net/2012/08/02101610/sleepingparrot.jpg'},
                  { id: 4, type: 'text', content: 'More text.'},
                ]
              },
              {
                id: 4,
                type: 'paragraph',
                content: [
                  { id: 1, type: 'text', content: 'Here is some text.'},
                  { id: 2, type: 'text', content: 'More text.'},
                ]
              },
            ]}
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
