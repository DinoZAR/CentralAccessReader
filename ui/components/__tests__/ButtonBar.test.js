import React from 'react';
import ButtonBar from '../ButtonBar';

describe('Base', () => {
  it('renders correctly', () => {
    const wrapper = shallow(<ButtonBar />);
    expect(wrapper).toMatchSnapshot();
  });
});
