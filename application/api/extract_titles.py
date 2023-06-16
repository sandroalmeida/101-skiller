import spacy
from spacy.matcher import Matcher
import re
import json
import os
import sys

def extract_titles(resume_text):

    # Get the absolute path of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Add the 'resources' folder to the Python module search path
    resources_path = os.path.join(current_dir, '..', 'helper')
    sys.path.append(resources_path)

    # Import the database operations module
    from database_operations import DatabaseOperations
    db_operations = DatabaseOperations()

    # Get the title patterns from the database
    title_patterns = db_operations.fetch_title_patterns()

    # Get the titles from the database
    titles = db_operations.fetch_titles()

    # Load a language model
    nlp = spacy.load("en_core_web_lg")

    # Create a doc object
    doc = nlp(resume_text)

    # Create a matcher object
    matcher = Matcher(nlp.vocab, validate=True)

    # Add each title pattern to the matcher object using a loop
    for pattern_name, pattern, title_id in title_patterns:
        matcher.add(pattern_name, [json.loads(pattern)])

    # Find all matches of the pattern in the doc
    matches = matcher(doc)

    # Collect the unique title names and unmatched strings in a set
    official_title_list = set()
    not_official_title_list = set()
    for match_id, start, end in matches:
        match_text = doc[start:end].text

        for title_id, title_description, alias, regex in titles:
            if (
                (alias is not None and alias.lower() == match_text.lower()) or
                (regex is not None and re.match(regex, match_text.lower(), re.IGNORECASE))
            ):
                official_title_list.add(title_id + ' - ' + title_description)
                break
        else:
            not_official_title_list.add(match_text)

    return official_title_list, not_official_title_list
