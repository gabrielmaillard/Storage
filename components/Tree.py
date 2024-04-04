from PyQt5 import QtWidgets, QtCore
from components.AddDialogWindow import AddDialogWindow
from components.LocationAddDialogWindow import LocationAddDialogWindow

class Tree(QtWidgets.QTreeWidget):

    def __init__(self, root, database_manager, parent=None):
        QtWidgets.QTreeWidget.__init__(self, parent)

        self.root = root
        self.database_manager = database_manager
        self.parent = parent

        self.itemSelectionChanged.connect(self.item_selected) # When the selected item change -> call the function self.item_selected()

    def contextMenuEvent(self, event):
        contextMenu = QtWidgets.QMenu(self)
        newAct = contextMenu.addAction("New article")
        newLocationAct = contextMenu.addAction("New location")
        openAct = contextMenu.addAction("Open")
        deleteAct = contextMenu.addAction("Delete")
        action = contextMenu.exec_(self.parent.mapToGlobal(event.pos() - QtCore.QPoint(-15, -80)))
        if action == newAct:
            contextMenu.close()
            self.add_article(locations=self.database_manager.select_all("Locations"))
        elif action == newLocationAct:
            contextMenu.close()
            self.add_location(locations=self.database_manager.select_all("Locations"))
        elif action == openAct:
            return
        elif action == deleteAct:
            if self.selectedItems() != []:
                self.deleted()
    
    def add_article(self, locations, articles_table="Articles"):

        self.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)

        self.first_dialog = AddDialogWindow(self.root, self.database_manager, locations, articles_table)
        self.first_dialog.exec_()

        self.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
    
    def add_location(self, locations, locations_table="Locations"):

        self.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)

        self.first_dialog = LocationAddDialogWindow(self.root, self.database_manager, locations, locations_table)
        self.first_dialog.exec_()

        self.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
    
    def deleted(self, articles_table="Articles", locations_table="Locations"):
        selected_widget = self.selectedItems()[0]
        if selected_widget.type == "location" and selected_widget.childCount() > 0:
            no_window = QtWidgets.QMessageBox()
            no_window.setIcon(QtWidgets.QMessageBox.Warning)
            no_window.setWindowTitle("Can't delete")
            no_window.setText("Error while trying to delete this location")
            no_window.setInformativeText("Can't delete this location as it contains articles")
            no_window.setFixedSize(200, 150)
            no_window.exec()
            return
        try:
            sure_window = QtWidgets.QMessageBox()
            sure_window.setWindowTitle("Sure to delete ?")
            sure_window.setText("Are you sure to delete ?")
            sure_window.setIcon(QtWidgets.QMessageBox.Question)
            sure_window.setFixedSize(500, 150)
            sure_window.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            sure_window.setDefaultButton(QtWidgets.QMessageBox.Cancel)

            clicked_button = sure_window.exec()

            if clicked_button == QtWidgets.QMessageBox.Ok:
                if selected_widget.type == "location":
                    self.database_manager.delete_entry(locations_table, int(selected_widget.id))
                elif selected_widget.type == "article":
                    self.database_manager.delete_entry(articles_table, int(selected_widget.id))
                self.root.reload()
                self.root.tree_item_deleted_refresh_tab()
        
        except Exception as e:
            print("[Error 00136] :\n\t", e)
    
    def item_selected(self, table_name="test"):

        self.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        selected_item = self.selectedItems()