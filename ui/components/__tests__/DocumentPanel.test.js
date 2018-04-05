import React from 'react';
import DocumentPanel from '../DocumentPanel';

describe('DocumentPanel', () => {
  it('renders correctly', () => {
    const wrapper = shallow(<DocumentPanel />);
    expect(wrapper).toMatchSnapshot();
  });
});
