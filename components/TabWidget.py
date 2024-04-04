from PyQt5 import QtWidgets

class QCustomTabWidget (QtWidgets.QTabWidget):
    def __init__ (self, parent = None):
        """
        Setting the basics of the widget like heritage from the basic QTabWidget from PyQt
        """

        super(QCustomTabWidget, self).__init__(parent)

        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.closeTab)

        self.setStyleSheet("QTabBar::tab { text-align: left; } ::close-button { image: url(img/cross.png); padding-top: 1px; }")

        self.add_tab = QtWidgets.QToolButton(self)
        self.add_tab.setText("+")
        self.add_tab.setStyleSheet("text-align: left;")

        self.number_tabs = self.count()

        self.add_tab.setFixedHeight(20)
        self.add_tab.setFixedWidth(24)
        self.add_tab.setStyleSheet(".QToolButton { border: 1px solid lightgrey; margin-left: 2px; border-bottom: 0px; }")

        self.add_tab.clicked.connect(self.new_tab)

        self.move_add_tab()

    def closeTab (self, currentIndex):
        """
        Function called when the "Close tab" button is clicked
        """

        currentQWidget = self.widget(currentIndex)
        currentQWidget.deleteLater()
        self.removeTab(currentIndex) # Close the selected tab

        # If there is only one tab -> we can close it, so we disable closable
        if self.count() == 1:
            self.setTabsClosable(False)
        
        self.move_add_tab()

    def new_tab(self):
        """
        Function called the button "Add a tab" is pushed
        """

        # Creating the new tab
        self.widget_new = QtWidgets.QWidget() # Creating the object
        self.addTab(self.widget_new, "Untitled") # Adding it
        self.setCurrentIndex(self.count() - 1) # Atributing an index to the tab

        # Settling the style (css) of the tab
        self.add_tab.setStyleSheet(".QToolButton { border: 1px solid lightgrey; margin-left: 2px; border-bottom: 0px; }")

        # Settling the sizes of the "Add a tab" button
        if self.count() > 1:
            self.add_tab.setFixedHeight(24)
            self.add_tab.setFixedWidth(28)
            self.setTabsClosable(True)

        self.move_add_tab()

    def move_add_tab(self):
        """
        Refresh the sizes and the position of the "Add a tab" button
        """

        tab_width = self.tabBar().geometry().getRect()[2]

        self.add_tab.move(int(tab_width), 0)
    
    def tab_name_change(self):
        """
        Function called when an item is selected -> so we change the name of the tab
        """
        
        if self.count() == 1:
            self.add_tab.setFixedHeight(20)
            self.add_tab.setFixedWidth(27)