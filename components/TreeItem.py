from PyQt5 import QtWidgets

class TreeItem(QtWidgets.QTreeWidgetItem):

    def __init__(self, parent, strings, id, type):
        QtWidgets.QTreeWidgetItem.__init__(self, parent, strings)

        self.id = id
        self.type = type

        if self.type == "location":
            self.setChildIndicatorPolicy(TreeItem.ShowIndicator)

