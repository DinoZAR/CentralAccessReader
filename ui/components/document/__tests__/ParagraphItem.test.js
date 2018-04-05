import React from 'react';
import ParagraphItem from '../ParagraphItem';

describe('ParagraphItem', () => {
  it('renders text', () => {
    const wrapper = shallow(
      <ParagraphItem
        content={{
          type: 'text',
          content: 'Here is some text.'
        }}
      />
    );
    expect(wrapper).toMatchSnapshot();
  });
  it('renders images', () => {
    const wrapper = shallow(
      <ParagraphItem
        content={{
          type: 'image',
          url: 'some_image.png'
        }}
      />
    );
    expect(wrapper).toMatchSnapshot();
  });
});
