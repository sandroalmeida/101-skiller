import mysql.connector
import sys
import os

# Get the absolute path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the 'resources' folder to the Python module search path
resources_path = os.path.join(current_dir, '..', 'resources')
sys.path.append(resources_path)

from v2.official_title import official_title
from v2.official_title_regex import official_title_regex
from v2.title_patterns_dictionary import title_patterns

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="AlAcT@1306",
  database="profile_dashboard"
)

mycursor = mydb.cursor()

# Title
for key in official_title.keys():
    title_description = key
    sql = "INSERT IGNORE INTO title (title_id, description) VALUES (UUID(), %s)"
    val = (title_description,)
    mycursor.execute(sql, val)

for key in official_title_regex.keys():
    title_description = key
    sql = "INSERT IGNORE INTO title (title_id, description) VALUES (UUID(), %s)"
    val = (title_description,)
    mycursor.execute(sql, val)

# Title String Dictionary
for key, aliases in official_title.items():
    title_description = key
    mycursor.execute("SELECT title_id FROM title WHERE description = %s", (title_description,))
    title_id = mycursor.fetchone()[0]

    for alias in aliases:
        sql = "INSERT INTO title_string_dictionary (alias, title_id) VALUES (%s, %s)"
        val = (alias, title_id)
        mycursor.execute(sql, val)

# Title Regex Dictionary
for key, regex_list in official_title_regex.items():
    title_description = key
    mycursor.execute("SELECT title_id FROM title WHERE description = %s", (title_description,))
    title_id = mycursor.fetchone()[0]

    for regex in regex_list:
        sql = "INSERT INTO title_regex_dictionary (regex, title_id) VALUES (%s, %s)"
        val = (regex, title_id)
        mycursor.execute(sql, val)

# # Title Pattern
for key, pattern in title_patterns.items():
    title_description = key
    mycursor.execute("SELECT title_id FROM title WHERE description = %s", (title_description,))
    title_id = mycursor.fetchone()[0]

    for pattern in pattern:
        sql = "INSERT INTO title_pattern (name, pattern, title_id) VALUES (%s, %s, %s)"
        val = (pattern[0], pattern[1], title_id)
        mycursor.execute(sql, val)

mydb.commit()