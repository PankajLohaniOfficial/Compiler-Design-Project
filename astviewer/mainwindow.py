# -*- coding: utf-8 -*-

import ast

import six


from models import ASTTreeModel


class MainWindow(QMainWindow):

    
    def __init__(self, parent=None):

        self.treeModel = ASTTreeModel(self)
        self.ui.treeView.setModel(self.treeModel)

    
    def on_actionParse_triggered(self):
        source = six.text_type(self.ui.plainTextEdit.toPlainText())
        node = ast.parse(source)
        self.ui.treeView.expandAll()
