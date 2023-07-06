import mysql.connector
import sys
import os

# Get the absolute path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the 'resources' folder to the Python module search path
resources_path = os.path.join(current_dir, '..', 'resources')
sys.path.append(resources_path)

from v2.official_skill_regex import official_skill_regex
from v2.skill_patterns_dictionary import skill_patterns

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="AlAcT@1306",
  database="profile_dashboard"
)

mycursor = mydb.cursor()

# Truncate tables
mycursor.execute("TRUNCATE TABLE skill_pattern")
mycursor.execute("TRUNCATE TABLE skill_regex_dictionary")
mycursor.execute("TRUNCATE TABLE skill")
mycursor.execute("TRUNCATE TABLE skill_category")

# Skill Category
for key in official_skill_regex.keys():
    category_description = key.split("|")[1]
    sql = "INSERT IGNORE INTO skill_category (skill_category_id, description) VALUES (UUID(), %s)"
    val = (category_description,)
    mycursor.execute(sql, val)

# Skill
for key in official_skill_regex.keys():
    category_description = key.split("|")[1]
    skill_description = key.split("|")[0]
    mycursor.execute("SELECT skill_category_id FROM skill_category WHERE description = %s", (category_description,))
    skill_category_id = mycursor.fetchone()[0]

    sql = "INSERT IGNORE INTO skill (skill_id, description, skill_category_id) VALUES (UUID(), %s, %s)"
    val = (skill_description, skill_category_id)
    mycursor.execute(sql, val)

# Skill Regex Dictionary
for key, regex_list in official_skill_regex.items():
    skill_description = key.split("|")[0]
    mycursor.execute("SELECT skill_id FROM skill WHERE description = %s", (skill_description,))
    skill_id = mycursor.fetchone()[0]

    for regex in regex_list:
        sql = "INSERT INTO skill_regex_dictionary (regex, skill_id) VALUES (%s, %s)"
        val = (regex, skill_id)
        mycursor.execute(sql, val)

# Skill Pattern
for key, patterns in skill_patterns.items():
    skill_description = key
    mycursor.execute("SELECT skill_id FROM skill WHERE description = %s", (skill_description,))
    skill_id = mycursor.fetchone()[0]

    for pattern in patterns:
        sql = "INSERT INTO skill_pattern (name, pattern, skill_id) VALUES (%s, %s, %s)"
        val = (pattern[0], pattern[1], skill_id)
        mycursor.execute(sql, val)

mydb.commit()
