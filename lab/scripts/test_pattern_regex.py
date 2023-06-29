import spacy
from spacy.matcher import Matcher
import json
import re

# Testing variables
text = "I can develop systems using or better say develop complex systems"
regex_string = "develop\s+(application|applications)?\s+systems"
json_pattern = '[{"LOWER": "develop"}, {"LOWER": {"IN": ["operational", "complex"]}, "OP": "?"}, {"LOWER": "systems"}]'

# Load a language model
nlp = spacy.load("en_core_web_lg")

# Create a doc object for skill matching process
doc = nlp(text)

# Printing tokens
for token in doc:
    print(token.is_punct, token.text, token.pos_, token.dep_)

# Create a matcher object
matcher = Matcher(nlp.vocab, validate=True)
matcher.add("test", [json.loads(json_pattern)])

# Find all the skills matches of the pattern in the doc
matches = matcher(doc)

# Collect the unique skill names and unmatched strings in a set
official_skill_list = set()
not_official_skill_list = set()
for match_id, start, end in matches:
    match_text = doc[start:end].text
    print(match_text)
    if(re.match(regex_string, match_text.lower(), re.IGNORECASE)):
        official_skill_list.add(match_text)
    else:
        not_official_skill_list.add(match_text)

# Printing results
if(official_skill_list):
    print("official_skill_list")
    print(official_skill_list)
if(not_official_skill_list):
    print("not_official_skill_list")
    print(not_official_skill_list)