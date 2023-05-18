import spacy
import json
from spacy.matcher import Matcher

# Load a language model
nlp = spacy.load("en_core_web_lg")

# Read the text file
with open("resume_test_2.txt", "r") as file:
    text = file.read()

# Create a doc object
doc = nlp(text)

# Load the skills data
with open("language_skill_map.json", "r") as file:
    skills_data = json.load(file)

# Create a matcher object
matcher = Matcher(nlp.vocab)

# Add each skill pattern to the matcher object using a loop
for skill in skills_data:
    patterns = [pattern["pattern"] for pattern in skill["dictionary"]]
    matcher.add(skill["description"], patterns)

# Find all matches of the pattern in the doc
matches = matcher(doc)

# Collect the unique skill names and unmatched strings in a set
skills_set = set()
not_skills_set = set()
for match_id, start, end in matches:
    match_text = doc[start:end].text

    for skill in skills_data:
        for pattern in skill["dictionary"]:
            if any(alias.lower() == match_text.lower() for alias in pattern["alias"]):
                skills_set.add(skill["description"])
                break
        else:
            continue
        break
    else:
        not_skills_set.add(match_text)

print("Skills:")
for skill in skills_set:
    print(skill)

print("")

if not_skills_set:
    print("Not skills:")
    for skill in not_skills_set:
        print(skill)
