import React from 'react';
import PropTypes from 'prop-types';

import { StyleSheet, css } from '../../styles/aphrodite';
import constants from '../../styles/constants';

import ParagraphItem from './ParagraphItem';

const Paragraph = ({ content }) => (
  <p className={css(styles.paragraph)}>
    {content.map(c => <ParagraphItem key={c.id} content={c} />)}
  </p>
);

const Header = ({ content }) => (
  <h1 className={css(styles.header)}>
    {content.map(c => <ParagraphItem key={c.id} content={c} />)}
  </h1>
);

const typesToComponent = {
  paragraph: Paragraph,
  header: Header,
};

class DocumentContent extends React.Component {
  render() {
    const { content } = this.props;
    const Comp = typesToComponent[content.type];
    return <Comp content={content.content} />;
  }
}

DocumentContent.propTypes = {
  content: PropTypes.shape({
    id: PropTypes.number.isRequired,
    type: PropTypes.oneOf(['paragraph', 'header', 'mathParagraph']).isRequired,
    content: PropTypes.oneOfType([
      PropTypes.string,
      PropTypes.arrayOf(PropTypes.shape({})),
    ]).isRequired,
  }).isRequired,
};

const styles = StyleSheet.create({
  paragraph: {
    marginBottom: '2rem',
  },
  header: {
    marginBottom: '3rem',
    fontSize: '3rem',
  },
});

export default DocumentContent;
