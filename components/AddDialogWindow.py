from PyQt5 import QtWidgets, QtCore, QtGui

class AddDialogWindow(QtWidgets.QDialog):

    def __init__(self, root, database_manager, locations, articles_table, *args, **kwargs):
        super(AddDialogWindow, self).__init__(*args, **kwargs)

        self.root = root
        self.database_manager = database_manager
        self.articles_table = articles_table

        ## A METTRE A JOUR
        self.setWindowTitle("Create an article")
        
        self.setFixedWidth(400)
        self.setFixedHeight(320)

        self.setFixedSize(self.size())
        
        self.nameEdit = QtWidgets.QLineEdit(self)
        self.nameEdit.setGeometry(QtCore.QRect(15, 15, 104, 21)) #110, 90, 104, 21
        self.nameEdit.setPlaceholderText("Name")
        self.nameEdit.setMaxLength(60)

        self.descriptionPlainTextEdit = QtWidgets.QPlainTextEdit(self)
        self.descriptionPlainTextEdit.setGeometry(QtCore.QRect(15, 50, 250, 200)) #110, 90, 104, 21
        self.descriptionPlainTextEdit.setPlaceholderText("Description")

        """
        self.color = QtWidgets.QPushButton(self)
        self.color.setGeometry(QtCore.QRect(15, 87, 104, 21))
        self.color.setText(" Color")
        self.color.setStyleSheet("color: #828282; background-color: white; border: 1px solid grey; text-align: left;")
        self.color.clicked.connect(self.select_color)
        """

        self.parentComboBox = QtWidgets.QComboBox(self)
        self.parentComboBox.setGeometry(QtCore.QRect(15, 264, 104, 21))
        self.parentComboBox.addItem("None", userData=None)
        for location in locations:
            self.parentComboBox.addItem(location[1], userData=location[0])
        
        # Buttons Ok / Cancel
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(30, 280, 340, 30)) #30, 240, 341, 32
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.buttonBox.accepted.connect(self.add_item)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)
    
    def add_item(self):
        name = self.nameEdit.text()
        description = self.descriptionPlainTextEdit.toPlainText()
        parent_location_id = self.parentComboBox.currentData()
        
        self.database_manager.add_entry(self.articles_table, [None, name, description, parent_location_id])
        
        self.root.reload()
        self.close()
    
    def select_color(self):
        
        selected_color = QtWidgets.QColorDialog.getColor()

        self.color.setText("")
        self.color.setStyleSheet(self.color.styleSheet() + "background-color: {};".format(selected_color.name()))