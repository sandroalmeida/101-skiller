import mysql.connector
import os
import sys

# Get the absolute path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the 'resources' folder to the Python module search path
resources_path = os.path.join(current_dir, '..', 'resources')
sys.path.append(resources_path)

from config import database_config

class DatabaseOperations:
    def __init__(self):
        self.cnx = mysql.connector.connect(**database_config)
        self.cursor = self.cnx.cursor()

    def fetch_skill_patterns(self):
        query = "SELECT name, pattern, skill_id FROM skill_pattern"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetch_skills(self):
        query = "SELECT skill_id, skill_description, category, alias, regex FROM skill_view"
        self.cursor.execute(query)
        return self.cursor.fetchall()
