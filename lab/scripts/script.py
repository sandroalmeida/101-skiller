import spacy
from spacy.matcher import Matcher
import re
import json
import os
import sys

# Get the absolute path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the 'resources' folder to the Python module search path
resources_path = os.path.join(current_dir, '..', '..', 'application/helper')
sys.path.append(resources_path)

# Import the database operations module
from database_operations import DatabaseOperations
db_operations = DatabaseOperations()

# Get the skill patterns from the database
skill_patterns = db_operations.fetch_skill_patterns()

# Get the titles patterns from the database
title_patterns = db_operations.fetch_title_patterns()

# Get the skills from the database
skills = db_operations.fetch_skills()

# Get the titles from the database
titles = db_operations.fetch_titles()

# Load a language model
nlp = spacy.load("en_core_web_lg")

# Importing the file text
file_text = os.path.join(current_dir, '..', 'resources', 'resume_test_2.txt')

# Read the text file
with open(file_text, "r") as file:
    text = file.read()

# Create a doc object for skill matching process
doc_skill = nlp(text)

# for token in doc_skill:
#     print(token.is_punct, token.text, token.pos_, token.dep_)

# Create a matcher object for skill matching process
matcher_skill = Matcher(nlp.vocab, validate=True)

# Add each skill pattern to the matcher object using a loop
for pattern_name, pattern, skill_id in skill_patterns:
    matcher_skill.add(pattern_name, [json.loads(pattern)])

# Find all the skills matches of the pattern in the doc
matches_skill = matcher_skill(doc_skill)

# Collect the unique skill names and unmatched strings in a set
official_skill_list = set()
not_official_skill_list = set()
for match_id, start, end in matches_skill:
    match_text = doc_skill[start:end].text

    for skill_id, skill_description, category, alias, regex in skills:
        if (
            (alias is not None and alias.lower() == match_text.lower()) or
            (regex is not None and re.match(regex, match_text.lower(), re.IGNORECASE))
        ):
            official_skill_list.add(skill_description)
            break
    else:
        not_official_skill_list.add(match_text)

# Create a doc object for title matching process
doc_title = nlp(text)

# Create a matcher object for skill matching process
matcher_title = Matcher(nlp.vocab, validate=True)

# Add each title pattern to the matcher object using a loop
for pattern_name, pattern, title_id in title_patterns:
    matcher_title.add(pattern_name, [json.loads(pattern)])

# Find all the titles matches of the pattern in the doc
matches_title = matcher_title(doc_title)

# Collect the unique title names and unmatched strings in a set
official_title_list = set()
not_official_title_list = set()
for match_id, start, end in matches_title:
    match_text = doc_title[start:end].text

    for title_id, title_description, alias, regex in titles:
        if (
            (alias is not None and alias.lower() == match_text.lower()) or
            (regex is not None and re.match(regex, match_text.lower(), re.IGNORECASE))
        ):
            official_title_list.add(title_description)
            break
    else:
        not_official_title_list.add(match_text)

if official_skill_list:
    print("Official skills:")
    for skill in official_skill_list:
        print(skill)
    print("")

if official_title_list:
    print("Official titles:")
    for title in official_title_list:
        print(title)
    print("")

if not_official_skill_list: 
    print("Not official skills:")
    for skill in not_official_skill_list:
        print(skill)
    print("")

if not_official_title_list:
    print("Not official titles:")
    for title in not_official_title_list:
        print(title)
