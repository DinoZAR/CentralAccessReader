import React from 'react';
import DocumentView from '../DocumentView';

describe('DocumentView', () => {
  it('renders correctly', () => {
    const wrapper = shallow(<DocumentView />);
    expect(wrapper).toMatchSnapshot();
  });
});
