import Enzyme, { shallow, render, mount } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

Enzyme.configure({ adapter: new Adapter() });

global.shallow = shallow;
global.render = render;
global.mount = mount;

function mockCreate(obj) {
  return obj;
}

function mockExtend() {
  return {
    StyleSheet: {
      create: mockCreate,
      extend: mockExtend
    },
    css: () => {},
  };
}

jest.mock('aphrodite/no-important', () => ({
  StyleSheet: {
    create: mockCreate,
    extend: mockExtend,
  },
  css: () => {}
}));

jest.mock('./ui/car', () => ({
  hello: () => {},
}));