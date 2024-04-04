"""
Root window
"""

from PyQt5 import QtWidgets, QtCore, QtGui
from components.TabWidget import QCustomTabWidget
from components.Tree import Tree
from components.TreeItem import TreeItem

class Root(QtWidgets.QMainWindow):
    """
    Main window
    """

    def __init__(self, y_pos, x_pos, width, height, database_manager, articles_table, locations_table):
        super(Root, self).__init__()

        self.database_manager = database_manager

        self.current_tab = None
        self.validate = None

        self.articles_table = articles_table
        self.locations_table = locations_table

        self.setGeometry(y_pos, x_pos, width, height)
        self.setWindowTitle("D&velopp")
        self.setWindowIcon(QtGui.QIcon("img/add.ico"))
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui()
        self.move_center()
        self.reload()
    
    def purge_ui(self):

        purge_center_qlineedit = self.centered.findChildren(QtWidgets.QLineEdit)

        for entry_purge_center_qlineedit in purge_center_qlineedit:
            entry_purge_center_qlineedit.clear()

    def reset_ui(self):

        self.central.deleteLater()
        self.central = None

        self.widget.deleteLater()
        self.widget = None

        self.verticalLayout.deleteLater()
        self.verticalLayout = None

        self.search_bar.deleteLater()
        self.search_bar = None

        self.tree.deleteLater()
        self.tree = None

        self.hbox.deleteLater()
        self.hbox = None
        
        self.splitter1.deleteLater()
        self.splitter1 = None

    def ui(self):
        
        self.central = QtWidgets.QWidget(self)
        
        self.widget = QtWidgets.QWidget(self.central)
        self.widget.setGeometry(QtCore.QRect(380, 10, 258, 1001))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.search_bar = QtWidgets.QLineEdit(self.widget)
        self.search_bar.setObjectName("lineEdit")
        self.search_bar.setPlaceholderText("🔍 Search...")
        self.search_bar.setStyleSheet("font-family: Segoe UI Symbol;")
        self.search_bar.textChanged.connect(self.search_bar_changed)

        self.verticalLayout.addWidget(self.search_bar)

        self.tree = Tree(self, self.database_manager, self)
        self.tree.adjustSize()
        self.tree.itemSelectionChanged.connect(lambda: self.get_info(self.tree.selectedItems()))

        self.verticalLayout.addWidget(self.tree)
        self.widget.setMinimumWidth(310)
        self.widget.setMaximumWidth(500)

        self.horizontalLayoutWidget = QtWidgets.QWidget()

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.pushButton = QtWidgets.QPushButton("New article", self.horizontalLayoutWidget)
        self.pushButton.setIcon(QtGui.QIcon("img/add_.png"))
        self.pushButton.setFixedHeight(34)
        self.pushButton.setIconSize(QtCore.QSize(24, 17))
        self.pushButton.clicked.connect(lambda: self.tree.add_article(self.database_manager.select_all(self.locations_table), self.articles_table))
        self.horizontalLayout.addWidget(self.pushButton)

        self.locationAddButton = QtWidgets.QPushButton("New location", self.horizontalLayoutWidget)
        self.locationAddButton.setIcon(QtGui.QIcon("img/add_.png"))
        self.locationAddButton.setFixedHeight(34)
        self.locationAddButton.setIconSize(QtCore.QSize(24, 17))
        self.locationAddButton.clicked.connect(lambda: self.tree.add_location(self.database_manager.select_all(self.locations_table), self.locations_table))
        self.horizontalLayout.addWidget(self.locationAddButton)


        self.pushButton_2 = QtWidgets.QPushButton("Delete", self.horizontalLayoutWidget)
        self.pushButton_2.setIcon(QtGui.QIcon("img/delete.png"))
        self.pushButton_2.setFixedHeight(34)
        self.pushButton_2.setIconSize(QtCore.QSize(24, 17))
        self.pushButton_2.clicked.connect(lambda: self.tree.deleted(self.articles_table, self.locations_table))
        self.horizontalLayout.addWidget(self.pushButton_2)

        """
        self.pushButton_3 = QtWidgets.QPushButton("Structure", self.horizontalLayoutWidget)
        self.pushButton_3.setIcon(QtGui.QIcon("img/structure.png"))
        self.pushButton_3.setFixedHeight(34)
        self.pushButton_3.setIconSize(QtCore.QSize(24, 17))
        self.horizontalLayout.addWidget(self.pushButton_3)


        self.pushButton_4 = QtWidgets.QPushButton("Duplicate", self.horizontalLayoutWidget)
        self.pushButton_4.setIcon(QtGui.QIcon("img/structure.png"))
        self.pushButton_4.setFixedHeight(34)
        self.pushButton_4.setIconSize(QtCore.QSize(24, 17))
        self.horizontalLayout.addWidget(self.pushButton_4)
        """

        self.verticalLayout.addWidget(self.horizontalLayoutWidget)
        
        self.hbox = QtWidgets.QHBoxLayout(self.central)

        self.centered = QCustomTabWidget(self)
        self.centered.setMinimumWidth(1000)
        self.centered.currentChanged.connect(lambda: self.tree.clearSelection())
        
        self.centered.new_tab()

        self.centered.add_tab.move(61, 0)
        
        if self.centered.count() == 1:
            self.centered.setTabsClosable(False)

        self.splitter1 = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.splitter1.addWidget(self.widget)
        self.splitter1.addWidget(self.centered)
        self.splitter1.setCollapsible(0, False)
        self.splitter1.setCollapsible(1, False)
        
        self.hbox.addWidget(self.splitter1)
        self.central.setLayout(self.hbox)
        self.setCentralWidget(self.central)

        self.menu()

        self.translating()
    
    def move_center(self):
        try:
            screen = QtWidgets.QDesktopWidget().screenGeometry()
            self.move(int((screen.width() / 2)) - int((self.frameSize().width() / 2)), int((screen.height() / 2)) - int((self.frameSize().height() / 2)))
        
        except Exception as e:
            print("Error [161.00] : \n \t", e)
    
    def translating(self):
        _translate = QtCore.QCoreApplication.translate
        self.tree.headerItem().setText(0, _translate("Root", "ID"))
        self.tree.headerItem().setText(1, _translate("Root", "Name"))
        self.tree.setSortingEnabled(True)

    def menu(self):

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 21))

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuDatabase = QtWidgets.QMenu(self.menuFile)

        self.setMenuBar(self.menubar)

        self.actionReset_database = QtWidgets.QAction(self)
        self.actionReset_database.triggered.connect(self.reset_database)
        self.menuDatabase.addAction(self.actionReset_database)

        self.actionReset_ui = QtWidgets.QAction(self)
        self.actionReset_ui.triggered.connect(self.purge_ui)
        self.menuDatabase.addAction(self.actionReset_ui)

        self.menuFile.addAction(self.menuDatabase.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Root", "Storage"))
        self.menuFile.setTitle(_translate("Root", "File"))

        self.menuDatabase.setTitle(_translate("Root", "Database"))
        self.actionReset_database.setText(_translate("Root", "Reset database..."))
        self.actionReset_ui.setText(_translate("Root", "Reset ui"))
    
    def reset_database(self):
        self.database_manager.delete_all_entries(self.articles_table)

    def search(self):
        search_text = self.search_bar.text()
        if search_text:
            articles = self.database_manager.search_articles(search_text, self.articles_table)
            self.reload_search_results(articles)
        else:
            self.reload_articles()
    
    def reload_search_results(self, articles):
        self.tree.clear()
        for article in articles:
            TreeItem(self.tree, [str(article[0]), article[1]], article[0], "article")

    def tree_item_deleted_refresh_tab(self):
        self.reset_infos()

        for index in range(self.centered.count()):
            tab_text = self.centered.tabText(index)
            if tab_text == self.centered.tabText(self.centered.currentIndex()):
                self.centered.setTabText(index, "Untitled")
                self.centered.move_add_tab()

    def reload(self):
        self.tree.clear()

        root_locations = self.database_manager.select_parent_locations()

        for root_location in root_locations:
            self.load_location(root_location)

    def load_location(self, current_location, parent_location_widget=None):
        if parent_location_widget == None:
            parent_location_widget = self.tree

        parent_item = TreeItem(parent_location_widget, [str(current_location[0]), current_location[1]], current_location[0], "location")
        parent_item.setChildIndicatorPolicy(TreeItem.ShowIndicator)

        child_locations = self.database_manager.select_child_locations(current_location[0])
        articles = self.database_manager.select_articles_by_location(self.articles_table, current_location[0])

        for article in articles:
            TreeItem(parent_item, [
                str(article[0]), article[1]
            ], article[0], "article")

        for child_location in child_locations:
            self.load_location(child_location, parent_item)


    def search_bar_changed(self):

        if self.search_bar.text() != "":
            self.reload()
            self.search()

        else:
            self.reload()
    
    def reset_infos(self):
        current_tab = self.get_current_tab()

        elements = [
            QtWidgets.QLineEdit,
            QtWidgets.QLabel
        ]

        for element in elements:
            for instance in current_tab.findChildren(element):
                instance.deleteLater()
        
        if self.validate:
            self.validate.hide()
    
    def get_current_tab(self):

        self.current_tab_index = self.centered.currentIndex()

        return self.centered.widget(self.current_tab_index)
    
    def get_info(self, selected_widgets):
        if not selected_widgets:
            ## A METTRE A JOUR (le purge ui ne vide pas le titre de l'onglet)
            self.purge_ui()
            return
        selected_widget = selected_widgets[0]

        # Check if it's an article
        if selected_widget.type == "location":
            self.set_tab_location(selected_widget)
        elif selected_widget.type == "article":
            self.set_tab_article(selected_widget)
    
    def set_tab_location(self, item_widget):
        datas = self.database_manager.select_entry(self.locations_table, item_widget.id)
        fields = self.database_manager.get_table_fields(self.locations_table)

        if not datas:
            return
        
        self.set_tab(item_widget, self.locations_table, datas, fields, ["id"], ["location_parent_id"])
    
    def set_tab_article(self, item_widget):
        datas = self.database_manager.select_entry(self.articles_table, item_widget.id)
        fields = self.database_manager.get_table_fields(self.articles_table)

        if not datas:
            return
        
        self.set_tab(item_widget, self.articles_table, datas, fields, ["id"], ["location_id"])

    def set_tab(self, item_widget, table, datas, fields, disabled=[], invisible=[]):
        """
        Disabled = list of fields that must be disabled (id, parent_id, ...)
        Invisible = same thing
        """

        id = item_widget.id
        type = item_widget.type

        current_tab = self.get_current_tab()
        self.reset_infos()

        if self.current_tab == self.centered.widget(self.centered.currentIndex()):
            self.validate.hide()

        y = 15
        for index, data in enumerate(datas):
            self.label = QtWidgets.QLabel(current_tab)
            self.label.setText(str(fields[index][1]).capitalize())
            self.label.setGeometry(10, y, 70, 21)

            self.entry = QtWidgets.QLineEdit(current_tab)
            self.entry.setText(str(data))
            self.entry.setGeometry(95, y, 240, 21)
            self.entry.textChanged.connect(lambda: self.validate.setEnabled(True))

            if fields[index][1] in disabled:
                self.entry.setEnabled(False)

            if fields[index][1] not in invisible:
                self.entry.show()
                self.label.show()
                y += 35
        
        self.validate = QtWidgets.QPushButton("Validate modifications", current_tab)
        self.validate.setFixedSize(150, 21)
        # self.validate.move(current_tab.geometry().width() - (self.validate.geometry().width() + 10), current_tab.geometry().height() - (self.validate.geometry().height() + 10))
        self.validate.move(10, y)
        self.validate.setEnabled(False)
        self.validate.clicked.connect(lambda: self.validate_modifications(table, id, type, current_tab.findChildren(QtWidgets.QLineEdit)))

        self.validate.show()

        self.centered.setTabText(self.centered.currentIndex(), datas[1] + " | " + str(datas[0]))
        self.centered.move_add_tab()
        self.centered.tab_name_change()

        self.current_tab = self.centered.widget(self.centered.currentIndex())

    def validate_modifications(self, table_name, id_, type, entries):
        try:
            field_values = [entry.text() for entry in entries[1:]]
            success = self.database_manager.update_entry(table_name, id_, field_values)
            if success:
                self.reload_item(self.tree.selectedItems()[0], table_name, type)
        except Exception as e:
            print(f"Error while validating modifications: {e}")
    
    def reload_item(self, item, table, type):

        index = self.tree.indexFromItem(item)
        self.tree.takeTopLevelItem(index.row())

        row = self.database_manager.select_entry(table, int(item.text(0))) #from data module
        row = list(row)

        item = TreeItem(self.tree, tuple(row), int(item.text(0)), type)
        self.tree.setCurrentIndex(self.tree.indexFromItem(item))