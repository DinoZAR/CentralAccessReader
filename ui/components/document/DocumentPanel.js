import React from 'react';
import PropTypes from 'prop-types';

import { StyleSheet, css } from '../../styles/aphrodite';
import constants from '../../styles/constants';

import DocumentContent from './DocumentContent';

class DocumentPanel extends React.Component {
  render() {
    const { content } = this.props;
    return (
      <div className={css(styles.window)}>
        <div className={css(styles.panel)} style={{ maxWidth: '50rem' }}>
          {content.map(c => <DocumentContent key={c.id} content={c} />)}
        </div>
      </div>
    );
  }
}

DocumentPanel.propTypes = {
  content: PropTypes.arrayOf(PropTypes.shape({
    id: PropTypes.number.isRequired,
  })).isRequired,
};

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
    width: '100%',
    padding: '2rem',
    boxShadow: constants.panelShadow,
  }
});

export default DocumentPanel;
