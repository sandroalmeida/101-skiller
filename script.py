import spacy
from skill_patterns import skill_patterns
from spacy.matcher import Matcher
from official_skill import official_skill
import re

# Load a language model
nlp = spacy.load("en_core_web_lg")

# Read the text file
with open("resume_test_2.txt", "r") as file:
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

# Find all matches of the pattern in the doc
matches = matcher(doc)

# Collect the unique skill names and unmatched strings in a set
official_skill_list = set()
not_official_skill_list = set()
for match_id, start, end in matches:
    match_text = doc[start:end].text

    for skill_name, skill_aliases in official_skill.items():
        if any(
            (isinstance(alias, str) and alias.lower() == match_text.lower()) or
            (isinstance(alias, str) and re.match(alias, match_text.lower(), re.IGNORECASE))
            for alias in skill_aliases
        ):
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
