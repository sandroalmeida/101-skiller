import spacy
from spacy.matcher import Matcher
import re
import mysql.connector
import json
import os

# Connect to the database
cnx = mysql.connector.connect(
    user='root',
    password='AlAcT@1306',
    host='localhost',
    database='profile_dashboard'
)

# Get the skill patterns from the database
cursor = cnx.cursor()
query = ("SELECT name, pattern, skill_id FROM skill_pattern")
cursor.execute(query)
skill_patterns = cursor.fetchall()

# Get the skills from the database
cursor = cnx.cursor()
query = ("SELECT skill_id, skill_description, category, alias, regex FROM skill_view")
cursor.execute(query)
skills = cursor.fetchall()

# Load a language model
nlp = spacy.load("en_core_web_lg")

# Get the absolute path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path
file_path = os.path.join(current_dir, '..', 'resources', 'resume_test_2.txt')


# Read the text file
with open(file_path, "r") as file:
    text = file.read()

# Create a doc object
doc = nlp(text)

# Print all tokens in the doc object
# print("All tokens:")
# for token in doc:
#     print(token.is_punct, token.text, token.pos_, token.dep_)

# Create a matcher object
matcher = Matcher(nlp.vocab, validate=True)

# Add each skill pattern to the matcher object using a loop
for pattern_name, pattern, skill_id in skill_patterns:
    matcher.add(pattern_name, [json.loads(pattern)])

# # Find all matches of the pattern in the doc
matches = matcher(doc)

# # Collect the unique skill names and unmatched strings in a set
official_skill_list = set()
not_official_skill_list = set()
for match_id, start, end in matches:
    match_text = doc[start:end].text

    for skill_id, skill_description, category, alias, regex in skills:
        if (
            (alias is not None and alias.lower() == match_text.lower()) or
            (regex is not None and re.match(regex, match_text.lower(), re.IGNORECASE))
        ):
            official_skill_list.add(skill_description)
            break
    else:
        not_official_skill_list.add(match_text)

print("Official skills:")
for skill in official_skill_list:
    print(skill)

print("")

if not_official_skill_list:    
    print("Not official skills:")
    for skill in not_official_skill_list:
        print(skill)
