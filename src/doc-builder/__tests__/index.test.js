import DocBuilder from '../index';
import fs from 'fs';

jest.mock('fs');

describe('DocBuilder()', () => {
  it('builds a paragraph and writes to disk', () => {
    const builder = new DocBuilder('tmp');
    builder.build((build) => {
      build.paragraph();
      build.text({ content: 'Some text' });
      build.math({ mathml: '<mathml>x</mathml>' });
      build.image({ url: 'image.png' });
    });
    expect(fs.writeFile.mock.calls).toHaveLength(1);
    expect(fs.writeFile.mock.calls[0][0]).toBe('tmp/__chunks/0.json');
    expect(fs.writeFile.mock.calls[0][1]).toMatchSnapshot();
  });
});
