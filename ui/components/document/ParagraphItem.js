import React from 'react';
import PropTypes from 'prop-types';

const TextItem = ({ content }) => {
  return <span>{content.content}</span>;
};

const ImageItem = ({ content }) => {
  return <img src={content.url} />;
};

const typesToItems = {
  text: TextItem,
  image: ImageItem,
};
const ParagraphItem = ({ content }) => {
  const Comp = typesToItems[content.type];
  return <Comp content={content} />;
};

export default ParagraphItem;
