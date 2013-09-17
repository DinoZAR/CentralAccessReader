'''
Created on May 21, 2013

@author: Spencer Graffe
'''
from PyQt4.QtCore import Qt, QAbstractItemModel, QModelIndex

class PageNode(object):
    '''
    classdocs
    '''
    def __init__(self, parent, name, anchorId):
        self.parent = parent
        self.children = []
        self.name = name
        self.anchorId = anchorId
        
        if parent != None:
            parent.children.append(self)
            
    def __len__(self):
        return len(self.children)
    
    def insertChild(self, child, position=0):
        self.children.insert(position, child)
        
    def childAtRow(self, row):
        assert 0 <= row <= len(self.children)
        return self.children[row]

    def row(self):
        if self.parent:
            return self.parent.children.index(self)
        return 0
    
class PagesTreeModel(QAbstractItemModel):
    '''
    This tree model is used for the page navigation for our view.
    '''
    
    def __init__(self, pageNumbers, parent=None):
        QAbstractItemModel.__init__(self, parent)
        self.root = PageNode(None, '-1', '-1')
        
        for page in pageNumbers:
            PageNode(self.root, page, 'page' + page)
    
    def flags(self, index):
        """Returns the item flags for the given index. """
        return Qt.ItemIsEnabled|Qt.ItemIsSelectable


    def data(self, index, role):
        """Returns the data stored under the given role for the item
        referred to by the index."""

        if not index.isValid():
            return None
        node = index.internalPointer()
        if role == Qt.DisplayRole:
            return unicode(node.name)
        else:
            return None


    def columnCount(self, parent):
        """The number of columns for the children of the given index."""
        return 1


    def rowCount(self, parent):
        """The number of rows of the given index."""

        if not parent.isValid():
            parent_node = self.root
        else:
            parent_node = parent.internalPointer()
        return len(parent_node)


    def index(self, row, column, parent=QModelIndex()):
        """Creates an index in the model for a given node and returns it."""
        
        obj = None
        if parent.internalPointer() != None:
            parentNode = parent.internalPointer()
            obj = parentNode.children[row]
        else:
            obj = self.root.children[row]
        return self.createIndex(row, column, obj)

    def parent(self, child):
        """The parent index of a given index."""
        
        node = child.internalPointer()
        if node is None:
            return QModelIndex()
        parent = node.parent
        if parent is None:
            return QModelIndex()
        
        # Check for grandparent. Need to do this to get row count for parent
        grandparent = parent.parent
        if grandparent is None:
            return QModelIndex()
        
        # Search for the parent in the grandparent to get the row count
        currRow = 0
        for c in grandparent.children:
            if c == parent:
                break
            currRow += 1
        
        return self.createIndex(currRow, 0, parent)
    
    def hasIndex(self, row, column, parent=QModelIndex()):
        '''
        Returns whether this index at row, column is a valid index.
        '''
        parent_node = None
        if not parent.isValid():
            parent_node = self.root
        else:
            parent_node = parent.internalPointer()
            
        return (column == 0) and (len(parent_node) > 0) and (row >= 0) and (row < len(parent_node))