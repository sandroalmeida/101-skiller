import mysql.connector
from official_skill import official_skill
from skill_patterns import skill_patterns

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="AlAcT@1306",
  database="profile_dashboard"
)

mycursor = mydb.cursor()

for key in official_skill.keys():
    category_description = key.split("|")[2]
    sql = "INSERT IGNORE INTO skill_category (skill_category_id, description) VALUES (UUID(), %s)"
    val = (category_description,)
    mycursor.execute(sql, val)

mydb.commit()

for key in official_skill.keys():
    category_description = key.split("|")[2]
    skill_description = key.split("|")[1]
    mycursor.execute("SELECT skill_category_id FROM skill_category WHERE description = %s", (category_description,))
    skill_category_id = mycursor.fetchone()[0]

    sql = "INSERT IGNORE INTO skill (skill_id, description, skill_category_id) VALUES (UUID(), %s, %s)"
    val = (skill_description, skill_category_id)
    mycursor.execute(sql, val)

mydb.commit()

for key, aliases in official_skill.items():
    skill_description = key.split("|")[1]
    mycursor.execute("SELECT skill_id FROM skill WHERE description = %s", (skill_description,))
    skill_id = mycursor.fetchone()[0]

    for alias in aliases:
        sql = "INSERT INTO skill_string_dictionary (alias, skill_id) VALUES (%s, %s)"
        val = (alias, skill_id)
        mycursor.execute(sql, val)

mydb.commit()

