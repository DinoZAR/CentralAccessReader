__author__ = 'Spencer Graffe'

from PyQt4.QtCore import QAbstractItemModel, QModelIndex, Qt

class GeneralTree(QAbstractItemModel):
    '''
    Creates a better tree model for a QTreeView. It allows one to set the
    templating for each of the different levels, or range of levels.
    '''

    def __init__(self, dataSource, parent=None):
        super(GeneralTree, self).__init__(parent)
        self._source = dataSource
        self._childrenAccessors = {}
        self._displayRules = {}

        self._tree = None

    def addChildrenRule(self, level, func):
        '''
        Adds a rule that determines how to access the children at a specific
        hierarchy level. If one is not defined for a level, it will try
        iteration on the object. If it doesn't support that, then no children
        will be gathered.

        The function must have the signature func(obj), and it must return an
        iterable of the children of obj.
        '''
        self._childrenAccessors[level] = func

    def addDisplayRule(self, level, func):
        '''
        Adds a rule on how to display a certain level of the hierachy.

        The function must have the signature func(obj) and returns a string.
        '''
        self._displayRules[level] = func

    def update(self):
        '''
        Updates the tree.
        '''
        self._tree = TreeItem(self._source, self._childrenAccessors)
        self.reset()

    def _checkForTree(self):
        if self._tree is None:
            self.update()

    #
    # QAbstractItemModel implementations
    #
    def index(self, row, column, parent=QModelIndex()):
        self._checkForTree()

        if not parent.isValid():
            parentItem = self._tree
        else:
            parentItem = parent.internalPointer()

        if row >= len(parentItem.children):
            return QModelIndex()
        else:
            return self.createIndex(row, column, parentItem.children[row])

    def parent(self, child=QModelIndex()):
        self._checkForTree()

        if not child.isValid():
            return QModelIndex()

        parentItem = child.internalPointer().parent
        if parentItem is not None:
            grandparentItem = parentItem.parent
            if grandparentItem is not None:
                row_number = grandparentItem.children.index(parentItem)
                return self.createIndex(row_number, 0, parentItem)

        return QModelIndex()

    def rowCount(self, parent=QModelIndex()):
        self._checkForTree()
        if parent.isValid():
            return len(parent.internalPointer().children)
        else:
            return len(self._tree.children)

    def columnCount(self, parent=QModelIndex()):
        self._checkForTree()
        return 1

    def data(self, index, role=Qt.DisplayRole):
        self._checkForTree()
        if index.isValid():
            if role == Qt.DisplayRole:
                item = index.internalPointer()
                if item.level in self._displayRules:
                    return self._displayRules[item.level](item.data)
                return unicode(index.internalPointer().data)
            else:
                return None
        else:
            return unicode(self._tree.data)

class TreeItem(object):

    def __init__(self, data, childAccessors, level=0):
        self.data = data
        self.level = level

        # Generate its children
        self.children = []
        iterable = data
        if level in childAccessors:
            iterable = childAccessors[level](data)

        try:
            for c in iterable:
                self.addChild(TreeItem(c, childAccessors, level=level + 1))
        except TypeError:
            pass

        self.parent = None

    def addChild(self, treeItem):
        self.children.append(treeItem)
        treeItem.parent = self