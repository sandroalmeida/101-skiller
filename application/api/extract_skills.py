import spacy
from spacy.matcher import Matcher
import re
import json
import os
import sys

def extract_skills(resume_text):

    # Get the absolute path of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Add the 'resources' folder to the Python module search path
    resources_path = os.path.join(current_dir, '..', 'helper')
    sys.path.append(resources_path)

    # Import the database operations module
    from database_operations import DatabaseOperations
    db_operations = DatabaseOperations()

    # Get the skill patterns from the database
    skill_patterns = db_operations.fetch_skill_patterns()

    # Get the skills from the database
    skills = db_operations.fetch_skills()

    # Load a language model
    nlp = spacy.load("en_core_web_lg")

    # Create a doc object
    doc = nlp(resume_text)

    # Create a matcher object
    matcher = Matcher(nlp.vocab, validate=True)

    # Add each skill pattern to the matcher object using a loop
    for pattern_name, pattern, skill_id in skill_patterns:
        matcher.add(pattern_name, [json.loads(pattern)])

    # Find all matches of the pattern in the doc
    matches = matcher(doc)

    # Collect the unique skill names and unmatched strings in a set
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

    return official_skill_list, not_official_skill_list
