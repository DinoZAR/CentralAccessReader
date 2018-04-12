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
      return () => ({
        success: true,
        content: 'some content',
      });
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
      return () => '';
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
      return () => ({ success: false, error: 'Something' });
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
      return () => {
        const things = {};
        return things.stuff.and.things(3);
      };
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