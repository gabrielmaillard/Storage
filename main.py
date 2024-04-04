"""
Main file to execute
"""

try:
    import sys
    import json
    import data
    from PyQt5 import QtWidgets
    from PyQt5.QtWidgets import *
    from dev.debug import line_info
    from components.Root import Root

except Exception as e:
    # If an error has occured while loading the modules
    # -> print the error with l. and stop the program.
    print(f"Error [{line_info()}.00] : \n \t", e)
    exit()

with open("configuration.json") as configuration_file:
    configuration = json.load(configuration_file)

DB_FILE = configuration['sqlite']['dbURL']
ARTICLES_TABLE = configuration['tables']['tables.articles']
LOCATIONS_TABLE = configuration['tables']['tables.locations']
WINDOW_WIDTH = configuration['window']['window.width']
WINDOW_HEIGHT = configuration['window']['window.height']
WINDOW_X = configuration['window']['window.x']
WINDOW_Y = configuration['window']['window.y']

database_manager = data.DatabaseManager(DB_FILE)
app = QtWidgets.QApplication(sys.argv)
if(QtWidgets.QDialog.Accepted == True):
    root = Root(WINDOW_X, WINDOW_Y, WINDOW_WIDTH, WINDOW_HEIGHT, database_manager, ARTICLES_TABLE, LOCATIONS_TABLE)
    root.show()

sys.exit(app.exec_())