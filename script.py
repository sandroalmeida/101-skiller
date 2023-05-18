import spacy
from skill_patterns import skill_patterns
from spacy.matcher import Matcher
import json

# Load a language model
nlp = spacy.load("en_core_web_lg")

# Read the text file
with open("resume_test.txt", "r") as file:
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
for pattern_name, pattern in skill_patterns.items():
    matcher.add(pattern_name, [pattern])

# Load the official skill list
with open("official_skill.json", "r") as file:
    official_skill = json.load(file)

# Find all matches of the pattern in the doc
matches = matcher(doc)

# Collect the unique skill names and unmatched strings in a set
official_skill_list = set()
not_official_skill_list = set()
for match_id, start, end in matches:
    match_text = doc[start:end].text

    for skill_name, skill_aliases in official_skill.items():
        if any(alias.lower() == match_text.lower() for alias in skill_aliases):
            official_skill_list.add(skill_name)
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
