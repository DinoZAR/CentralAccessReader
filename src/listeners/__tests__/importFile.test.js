describe('importFile()', () => {

  beforeEach(() => {
    jest.resetModules();
  });

  it('returns contents of importer on success', () => {
    jest.doMock('electron', () => {
      return {
        BrowserWindow: {
          getFocusedWindow: () => 'stuff',
        },
        dialog: {
          showOpenDialog: () => ['a file.txt']
        }
      };
    });
    jest.doMock('../../importers', () => {
      return () => Promise.resolve('some content');
    });
    const importFile = require('../importFile').default;

    return importFile().then((contents) => {
      expect(contents).toEqual({
        status: 'success',
        content: 'some content'
      });
    });
  });

  it('returns canceled when no file is selected', () => {
    jest.doMock('electron', () => {
      return {
        BrowserWindow: {
          getFocusedWindow: () => 'stuff',
        },
        dialog: {
          showOpenDialog: () => undefined
        }
      };
    });
    jest.doMock('../../importers', () => {
      return () => Promise.resolve('');
    });
    const importFile = require('../importFile').default;

    return importFile().then((contents) => {
      expect(contents).toEqual({
        status: 'canceled'
      });
    });
  });

  it('returns rejection when something bad happens', () => {
    jest.doMock('electron', () => {
      return {
        BrowserWindow: {
          getFocusedWindow: () => 'stuff',
        },
        dialog: {
          showOpenDialog: () => ['a file.txt']
        }
      };
    });
    jest.doMock('../../importers', () => {
      return () => Promise.reject('Something');
    });
    const importFile = require('../importFile').default;

    return importFile().catch((contents) => {
      expect(contents).toEqual({ status: 'failed', error: 'Something' });
    });
  });

  it('returns rejection when an exception is raised in importer', () => {
    jest.doMock('electron', () => {
      return {
        BrowserWindow: {
          getFocusedWindow: () => 'stuff',
        },
        dialog: {
          showOpenDialog: () => ['a file.txt']
        }
      };
    });
    jest.doMock('../../importers', () => {
      return () => new Promise((resolve) => {
        const things = {};
        return resolve(things.stuff.and.things(3));
      });
    });
    const importFile = require('../importFile').default;

    return importFile().catch((contents) => {
      expect(contents).toEqual({
        status: 'failed',
        error: "TypeError: Cannot read property 'and' of undefined"
      });
    });
  });
});