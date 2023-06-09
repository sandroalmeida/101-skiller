import mysql.connector
import os
import sys
from mysql.connector import Error

# Get the absolute path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the 'resources' folder to the Python module search path
resources_path = os.path.join(current_dir, '..', 'resources')
sys.path.append(resources_path)

from config import database_config

class DatabaseOperations:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(**database_config)
            self.cursor = self.cnx.cursor()
        except Error as e:
            print(f"Error connecting to database: {e}")
            self.cnx = None
            self.cursor = None

    def fetch_skill_patterns(self):
        if self.cursor is not None:
            try:
                query = "SELECT name, pattern, skill_id FROM skill_pattern"
                self.cursor.execute(query)
                return self.cursor.fetchall()
            except Error as e:
                print(f"Error executing query: {e}")
                return None
        else:
            print("No database connection.")
            return None

    def fetch_skills(self):
        if self.cursor is not None:
            try:
                query = "SELECT skill_id, skill_description, category, regex FROM skill_view"
                self.cursor.execute(query)
                return self.cursor.fetchall()
            except Error as e:
                print(f"Error executing query: {e}")
                return None
        else:
            print("No database connection.")
            return None
    
    def fetch_titles(self):
        if self.cursor is not None:
            try:
                query = "SELECT title_id, title_description, regex FROM title_view"
                self.cursor.execute(query)
                return self.cursor.fetchall()
            except Error as e:
                print(f"Error executing query: {e}")
                return None
        else:
            print("No database connection.")
            return None
        
    def fetch_title_patterns(self):
        if self.cursor is not None:
            try:
                query = "SELECT name, pattern, title_id FROM title_pattern"
                self.cursor.execute(query)
                return self.cursor.fetchall()
            except Error as e:
                print(f"Error executing query: {e}")
                return None
        else:
            print("No database connection.")
            return None
        
    def title_pattern_exists(self, pattern):
        if self.cursor is not None:
            try:
                query = "SELECT COUNT(*) FROM title_pattern WHERE pattern = %s"
                self.cursor.execute(query, (pattern,))
                return self.cursor.fetchone()[0] > 0
            except Error as e:
                print(f"Error executing query: {e}")
                return None
        else:
            print("No database connection.")
            return None
