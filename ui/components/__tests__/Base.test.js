import React from 'react';
import Base from '../Base';

describe('Base', () => {
  it('renders correctly', () => {
    const wrapper = shallow(<Base />);
    expect(wrapper).toMatchSnapshot();
  });
});
