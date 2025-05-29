import types

from PyQt4.QtCore import QModelIndex
from PyQt4.QtCore import Qt


class ASTTreeModel(QAbstractItemModel):
    def __init__(self, parent):
        super(ASTTreeModel, self).__init__(parent) #initialize the tree model
        self.headers = [
            self.tr("Attribute"), #set up the headers for the tree view
            self.tr("Value"),
        ]
        self.node = None  #LATER HOLD ROOT OF AST TREE

    def setNode(self, node):
        self.beginResetModel()
        self.node = ASTTreeItem(None, None)
        self.node.children.append(ASTTreeItem.create(node, self.node))



    # tHIS returns the no. of children for the  given parent node
    def rowCount(self, parent=QModelIndex()):
        if self.node is None:
            return 0
        parent_item = None
        if not parent.isValid():
            parent_item = self.node
        else:
            parent_item = parent.internalPointer()
        return len(parent_item.children)



    #Maps a _ row -- column _ pair for a specific child node in model
    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or role != Qt.DisplayRole:
            return QVariant()
        node = index.internalPointer()
        if index.column() == 0:
            return node.name
        elif index.column() == 1:
            return node.value
        return QVariant()

#retuns the parent of a given node
    def parent(self, index):
        item = index.internalPointer()
        if item.parent is None:
            # root case
            return QModelIndex()
        return self.createIndex(item.parent.row, 0, item.parent)







#new class 


class ASTTreeItem(object):

    NODE_TYPE = 1
    FIELD_TYPE = 2

    def __init__(type, parent=None):
        self.parent = parent   #reference to parent node
        self.children = []  #list of children nodes
