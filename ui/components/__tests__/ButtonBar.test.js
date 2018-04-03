import React from 'react';
import ButtonBar from '../ButtonBar';

describe('ButtonBar', () => {
  it('renders correctly', () => {
    const wrapper = shallow(<ButtonBar />);
    expect(wrapper).toMatchSnapshot();
  });
});
