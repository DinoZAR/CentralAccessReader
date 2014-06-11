__author__ = 'Spencer Graffe'

from PyQt5.QtCore import QAbstractItemModel, QModelIndex, Qt

class GeneralTree(QAbstractItemModel):
    '''
    Creates a better tree model for a QTreeView. It allows one to set the
    templating for each of the different levels. It's more expressive this way
    and it uses Python's pervasive use of iteration to its benefit.
    '''

    def __init__(self, dataSource, parent=None):
        super(GeneralTree, self).__init__(parent)
        self._source = dataSource

        self._childrenAccessors = {}
        self._defaultChildrenAccessor = None

        self._displayRules = {}
        self._defaultDisplayRule = None

        self._selectableRules = {}

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

    def setDefaultChildrenRule(self, func):
        '''
        Sets the default rule for getting children.

        The function must have the signature func(obj), and it must return an
        iterable of the children of obj.
        '''
        self._defaultChildrenAccessor = func

    def addDisplayRule(self, level, func):
        '''
        Adds a rule on how to display a certain level of the hierachy.

        The function must have the signature func(obj) and returns a string.
        '''
        self._displayRules[level] = func

    def setDefaultDisplayRule(self, func):
        '''
        Sets the default display rule for all levels.

        The function must have the signature func(obj) and returns a string.
        '''
        self._defaultDisplayRule = func

    def addSelectableRule(self, level, func):
        '''
        Adds a rule determining whether an item is selectable for a certain
        hierarchy level.

        The function must have the signature func(obj) and return a boolean
        value indicating whether item is selectable.
        '''
        self._selectableRules[level] = func

    def getIndexFromPath(self, p, parent=None):
        '''
        Returns a QModelIndex given the path. The path is a list of names that
        correspond to the labels given for each item. Do not include the name of
        the root node.

        Returns an invalid index if it can't find it.
        '''
        if parent is None:
            parent = self._tree

        if len(p) > 0:
            myLabel = p.pop(0)
            for i in range(len(parent.children)):
                if self._getTreeItemLabel(parent.children[i]) == myLabel:
                    if len(p) == 0:
                        return self.createIndex(i, 0, parent.children[i])
                    return self.getIndexFromPath(p, parent.children[i])

        return QModelIndex()

    def getPathFromIndex(self, index):
        '''
        Returns a path from the QModelIndex. The path is a list of the
        underlying data of the tree items.
        '''
        myList = []

        myItem = index.internalPointer()
        while myItem is not None:
            myList.insert(0, myItem.data)
            myItem = myItem.parent

        # Remove the last one, since that is a duplicate and needs to be
        # removed
        return myList[1:]

    def update(self):
        '''
        Updates the tree.
        '''
        self.beginResetModel()
        self._tree = TreeItem(self._source, self._childrenAccessors, self._defaultChildrenAccessor)
        self.endResetModel()

    def _getTreeItemLabel(self, item):
        if item.level in self._displayRules:
            return self._displayRules[item.level](item.data)
        elif self._defaultDisplayRule is not None:
            return self._defaultDisplayRule(item.data)
        return unicode(item.data)

    #
    # QAbstractItemModel implementations
    #
    def _checkForTree(self):
        if self._tree is None:
            self.update()

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

    def flags(self, index):
        myFlags = 0
        myFlags = myFlags | Qt.ItemIsEnabled

        item = index.internalPointer()
        if item.level in self._selectableRules:
            if self._selectableRules[item.level](item.data):
                myFlags = myFlags | Qt.ItemIsSelectable
        else:
            myFlags = myFlags | Qt.ItemIsSelectable

        return myFlags

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
                return self._getTreeItemLabel(item)
            else:
                return None
        else:
            return unicode(self._tree.data)

class TreeItem(object):

    def __init__(self, data, childAccessors, defaultChildrenAccessor,  level=0):
        self.data = data
        self.level = level

        # Generate its children
        self.children = []
        iterable = data
        if level in childAccessors:
            iterable = childAccessors[level](data)
        elif defaultChildrenAccessor is not None:
            iterable = defaultChildrenAccessor(data)

        try:
            for c in iterable:
                self.addChild(TreeItem(c, childAccessors, defaultChildrenAccessor, level=level + 1))
        except TypeError:
            pass

        self.parent = None

    def addChild(self, treeItem):
        self.children.append(treeItem)
        treeItem.parent = self