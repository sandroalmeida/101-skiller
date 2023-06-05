import spacy
from application.resources.v1.skill_patterns import skill_patterns
from spacy.matcher import Matcher
import json

def extract_skills(resume_text):
    # Load a language model
    nlp = spacy.load("en_core_web_lg")

    # Create a doc object
    doc = nlp(resume_text)

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

    return official_skill_list, not_official_skill_list
