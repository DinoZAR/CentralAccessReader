import path from 'path';
import importDocx from '../docx';
import { calls, resetCalls } from '../../doc-builder';

jest.mock('../../doc-builder');

describe('importDocx()', () => {
  it('parses a basic doc with text in it', () => {
    resetCalls();
    return importDocx(path.join(__dirname, './test_files/basic-text.docx'), '/tmp').then(() => {
      expect(calls()).toMatchSnapshot();
    });
  });

  it('parses images and text', () => {
    resetCalls();
    return importDocx(path.join(__dirname, './test_files/text-with-images.docx'), '/tmp').then(() => {
      expect(calls()).toMatchSnapshot();
    });
  });
});