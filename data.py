"""
This module has for objective to implement all the most used features in order to use it easily and
quickly. So, this module saves time by stopping repetiting tasks. You can implement a complex feature in
only one line. If you don't know what a function is for, the descriptions are here to help you (you can
print each description of each function with help(name_of_the_function)).
"""

import sqlite3

class DatabaseManager:
    def __init__(self, db):
        """
        Initializes the DatabaseManager object.
        Args:
            db (str): The name of the database file.
        """
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

    def create_table(self, name, fields):
        """
        Creates a new table in the database with the specified fields.
        Args:
            name (str): The name of the table.
            fields (list): A list of tuples containing field names and types.
        Returns:
            int: The number of fields created.
        """
        try:
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {name} (id INTEGER PRIMARY KEY AUTOINCREMENT)")
            for field in fields:
                self.cursor.execute(f"ALTER TABLE {name} ADD COLUMN {field[0]} {field[1]}")
            return len(fields)
        except Exception as e:
            print(f"Error creating table: {e}")
            return 0

    def add_entry(self, table_name, entry):
        """
        Adds a new entry to the specified table in the database.
        Args:
            table_name (str): The name of the table.
            entry (list): The data of the entry to add.
        Returns:
            str: Confirmation message.
        """
        try:
            fields = self.cursor.execute(f"PRAGMA table_info({table_name})").fetchall()
            interrogations_point = "?" + ", ?" * (len(fields) - 1)
            self.cursor.execute(f"INSERT INTO {table_name} VALUES ({interrogations_point})", entry)
            self.connection.commit()
            return "ADDED!"
        except Exception as e:
            print(f"Error adding entry: {e}")
            return ""

    def delete_entry(self, table_name, entry_id):
        """
        Deletes an entry from the specified table in the database.
        Args:
            table_name (str): The name of the table.
            entry_id (int): The ID of the entry to delete.
        Returns:
            str: Confirmation message.
        """
        try:
            self.cursor.execute(f"DELETE FROM {table_name} WHERE id = ?", (entry_id,))
            self.connection.commit()
            return "DELETED!"
        except Exception as e:
            print(f"Error deleting entry: {e}")
            return ""

    def select_entry(self, table_name, entry_id):
        """
        Searches for an entry in the specified table based on its ID.
        Args:
            table_name (str): The name of the table.
            entry_id (int): The ID of the entry to search for.
        Returns:
            tuple: The selected entry.
        """
        try:
            self.cursor.execute(f"SELECT * FROM {table_name} WHERE id = ?", (entry_id,))
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Error selecting entry: {e}")
            return None

    def delete_all_entries(self, table_name):
        """
        Deletes all entries from the specified table in the database.
        Args:
            table_name (str): The name of the table.
        Returns:
            str: Confirmation message.
        """
        try:
            self.cursor.execute(f"DELETE FROM {table_name}")
            self.connection.commit()
            return "DELETED ALL!"
        except Exception as e:
            print(f"Error deleting all entries: {e}")
            return ""

    def select_entry_by_name(self, table_name, entry_name):
        """
        Searches for entries in the specified table based on their name.
        Args:
            table_name (str): The name of the table.
            entry_name (str): The name of the entry to search for.
        Returns:
            list: The selected entries.
        """
        try:
            self.cursor.execute(f"SELECT * FROM {table_name} WHERE name LIKE ? OR id LIKE ?", (entry_name, entry_name))
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error selecting entry by name: {e}")
            return []

    def select_all(self, table_name):
        """
        Retrieves all entries from the specified table in the database.
        Args:
            table_name (str): The name of the table.
        Returns:
            list: All entries in the table.
        """
        try:
            self.cursor.execute(f"SELECT * FROM {table_name}")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error selecting all entries: {e}")
            return []
    
    def get_table_fields(self, table_name):
        """
        Retrieve the column names and details of a table.
        """
        try:
            self.cursor.execute(f"PRAGMA table_info({table_name})")
            columns_info = self.cursor.fetchall()
            return columns_info
        except Exception as e:
            print(f"Error while retrieving table columns for {table_name}: {e}")
            return None
    
    def update_entry(self, table_name, id_, field_values):
        """
        Update an entry in the specified table with the given field values.
        """
        try:
            self.cursor.execute(f"PRAGMA table_info({table_name})")
            column_info = self.cursor.fetchall()
            
            set_fields = ", ".join([f"{column_info[i][1]} = ?" for i in range(1, len(column_info))])
            sql = f"UPDATE {table_name} SET {set_fields} WHERE id = ?"
            
            field_values.append(id_)
            self.cursor.execute(sql, field_values)
            self.cursor.connection.commit()
            return True
        except Exception as e:
            print(f"Error while updating entry in {table_name}: {e}")
            return False

    def close(self):
        """
        Closes the connection to the database.
        """
        self.connection.close()
    
    def select_articles_by_location(self, articles_table, location_id):
        """
        Select all articles associated with a given location.
        """
        sql = f"SELECT * FROM {articles_table} WHERE location_id = ?"
        self.cursor.execute(sql, (location_id,))
        articles = self.cursor.fetchall()
        return articles

    def search_locations(self, search_text, locations_table):
        """
        Recherche les emplacements correspondant au texte de recherche.
        Retourne une liste de tuples (id_emplacement, nom_emplacement).
        """
        try:
            query = f"SELECT id, name FROM {locations_table} WHERE name LIKE ?"
            self.cursor.execute(query, ('%' + search_text + '%',))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print("Error while searching locations:", e)
            return []

    def search_articles(self, search_text, articles_table):
        """
        Recherche les articles correspondant au texte de recherche.
        Retourne une liste de tuples (id_article, nom_article).
        """
        try:
            query = f"SELECT id, name FROM {articles_table} WHERE name LIKE ?"
            self.cursor.execute(query, ('%' + search_text + '%',))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print("Error while searching articles:", e)
            return []
    
    def select_child_locations(self, parent_location_id):
        """
        Sélectionne tous les emplacements enfants du parent_location_id donné.
        :param parent_location_id: ID de l'emplacement parent.
        :return: Liste des emplacements enfants.
        """
        query = "SELECT * FROM Locations WHERE location_parent_id = ?"
        params = (parent_location_id,)
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def select_parent_locations(self):
        """
        Selects top-level locations (locations without a parent).
        Returns a list of top-level locations.
        """
        query = "SELECT * FROM locations WHERE location_parent_id IS NULL"
        self.cursor.execute(query)
        parent_locations = self.cursor.fetchall()
        return parent_locations

