title_patterns = {
    "Software Engineer Intern": [
        ("software development engineer intern", '[{"LOWER": "software"}, {"LOWER": "development"}, {"LOWER": "engineer"}, {"LOWER": {"IN": ["intern", "internship"]} }]'),
        ("programmer analyst", '[{"LOWER": "programmer"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "analyst"}, {"LOWER": {"IN": ["intern", "internship"]} }]'),
        ("engineer intern", '[{"LOWER": {"IN": ["engineer", "developer", "programmer"]} }, {"LOWER": {"IN": ["intern", "internship"]} }]'),
    ],
    "Junior Software Engineer": [
        ("junior software engineer", '[{"LOWER": {"IN": ["junior", "jr.", "jr"]} }, {"LOWER": {"IN": ["software", "programmer", "application", "system", "systems", "computer"]} }, {"LOWER": {"IN": ["engineer", "developer", "programmer"]} }]'),
        ("junior software development engineer", '[{"LOWER": {"IN": ["junior", "jr.", "jr"]} }, {"LOWER": "software"}, {"LOWER": "development"}, {"LOWER": "engineer"}]'),
        ("junior programmer analyst", '[{"LOWER": {"IN": ["junior", "jr.", "jr"]} }, {"LOWER": "programmer"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "analyst"}]'),
        ("junior engineer", '[{"LOWER": {"IN": ["junior", "jr.", "jr"]} }, {"LOWER": {"IN": ["engineer", "developer", "programmer"]} }]'),
    ],
    "Intermediate Software Engineer": [
        ("intermediate software engineer", '[{"LOWER": "intermediate"}, {"LOWER": {"IN": ["software", "programmer", "application", "system", "systems", "computer"]} }, {"LOWER": {"IN": ["engineer", "developer", "programmer"]} }]'),
        ("intermediate software development engineer", '[{"LOWER": "intermediate"}, {"LOWER": "software"}, {"LOWER": "development"}, {"LOWER": "engineer"}]'),
        ("intermediate programmer analyst", '[{"LOWER": {"IN": ["junior", "jr.", "jr"]} }, {"LOWER": "programmer"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "analyst"}]'),
        ("software engineer I", '[{"LOWER": "software"}, {"LOWER": {"IN": ["engineer", "developer"]} }, {"LOWER": "i"}]'),
        ("intermediate engineer", '[{"LOWER": "intermediate"} }, {"LOWER": {"IN": ["engineer", "developer", "programmer"]} }]'),
    ],
    "Software Engineer": [
        ("software engineer", '[{"LOWER": {"NOT_IN": ["lead", "principal", "staff", "senior", "sr.", "sr", "intermediate", "junior", "jr.", "jr"]} }, {"LOWER": {"IN": ["software", "programmer", "application", "system", "systems", "computer"]} }, {"LOWER": {"IN": ["engineer", "developer", "programmer"]} }, {"LOWER": {"NOT_IN": ["i", "iii", "iv", "intern", "internship", "manager"]} }]'),
        ("software development engineer", '[{"LOWER": {"NOT_IN": ["lead", "principal", "staff", "senior", "sr.", "sr", "intermediate", "junior", "jr.", "jr"]} }, {"LOWER": "software"}, {"LOWER": "development"}, {"LOWER": "engineer"}, {"LOWER": {"NOT_IN": ["i", "iii", "iv", "intern", "internship", "manager"]} }]'),
        ("programmer analyst", '[{"LOWER": {"NOT_IN": ["lead", "principal", "staff", "senior", "sr.", "sr", "intermediate", "junior", "jr.", "jr"]} }, {"LOWER": "programmer"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "analyst"}, {"LOWER": {"NOT_IN": ["i", "iii", "iv", "intern", "internship", "manager"]} }]'),
        ("engineer consultant", '[{"LOWER": {"IN": ["engineer", "developer", "software", "technical", "programmer"]} }, {"LOWER": {"IN": ["consultant", "contractor", "associate"]} }]'),
        ("consultant engineer", '[{"LOWER": {"IN": ["consultant", "contractor", "associate"]} }, {"LOWER": {"IN": ["engineer", "developer", "programmer"]} }]'),
    ],
    "Senior Software Engineer": [
        ("senior software engineer", '[{"LOWER": {"IN": ["senior", "sr.", "sr"]} }, {"LOWER": {"IN": ["software", "programmer", "application", "system", "systems", "computer"]} }, {"LOWER": {"IN": ["engineer", "developer", "programmer"]} }]'),
        ("senior software development engineer", '[{"LOWER": {"IN": ["senior", "sr.", "sr"]} }, {"LOWER": "software"}, {"LOWER": "development"}, {"LOWER": "engineer"}]'),
        ("senior programmer analyst", '[{"LOWER": {"IN": ["senior", "sr.", "sr"]} }, {"LOWER": "programmer"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "analyst"}]'),
        ("software engineer iii", '[{"LOWER": {"IN": ["software", "programmer", "application", "system", "systems", "computer"]} }, {"LOWER": {"IN": ["engineer", "developer", "programmer"]} }, {"LOWER": {"IN": ["iii", "iv"]} }]'),
        ("senior engineer", '[{"LOWER": {"IN": ["senior", "sr.", "sr"]} }, {"LOWER": {"IN": ["engineer", "developer", "programmer"]} }]'),
    ],
    "Staff Software Engineer": [
        ("staff software engineer", '[{"LOWER": "staff"}, {"LOWER": {"IN": ["software", "programmer", "application", "system", "systems", "computer"]} }, {"LOWER": {"IN": ["engineer", "developer", "programmer"]} }]'),
        ("staff software development engineer", '[{"LOWER": "staff"}, {"LOWER": "software"}, {"LOWER": "development"}, {"LOWER": "engineer"}]'),
        ("staff programmer analyst", '[{"LOWER": "staff"}, {"LOWER": "programmer"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "analyst"}]'),
        ("staff engineer", '[{"LOWER": "staff"}, {"LOWER": {"IN": ["engineer", "developer", "programmer"]} }]'),
    ],
    "Principal Software Engineer": [
        ("principal software engineer", '[{"LOWER": "principal"}, {"LOWER": {"IN": ["software", "programmer", "application", "system", "systems", "computer"]} }, {"LOWER": {"IN": ["engineer", "developer", "programmer"]} }]'),
        ("principal software development engineer", '[{"LOWER": "principal"}, {"LOWER": "software"}, {"LOWER": "development"}, {"LOWER": "engineer"}]'),
        ("principal programmer analyst", '[{"LOWER": "principal"}, {"LOWER": "programmer"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "analyst"}]'),
        ("principal engineer", '[{"LOWER": "principal"}, {"LOWER": {"IN": ["engineer", "developer", "programmer"]} }]'),
    ],
    "Lead Software Engineer": [
        ("lead software engineer", '[{"LOWER": "lead"}, {"LOWER": {"IN": ["software", "programmer", "application", "system", "systems", "computer"]} }, {"LOWER": {"IN": ["engineer", "developer", "programmer"]} }]'),
        ("lead software development engineer", '[{"LOWER": "lead"}, {"LOWER": "software"}, {"LOWER": "development"}, {"LOWER": "engineer"}]'),
        ("lead programmer analyst", '[{"LOWER": "lead"}, {"LOWER": "programmer"}, {"IS_PUNCT": true, "OP": "?"}, {"LOWER": "analyst"}]'),
        ("lead engineer", '[{"LOWER": "lead"}, {"LOWER": {"IN": ["engineer", "developer", "programmer"]} }]'),
        ("technical lead", '[{"LOWER": {"IN": ["technical", "tech"]} }, {"LOWER": "lead"}]'),
    ],
    "Software Engineer Consultant": [
        ("engineer consultant", '[{"LOWER": {"IN": ["engineer", "developer", "software", "technical"]} }, {"LOWER": {"IN": ["consultant", "contractor", "associate"]} }]'),
        ("consultant engineer", '[{"LOWER": {"IN": ["consultant", "contractor", "associate"]} }, {"LOWER": {"IN": ["engineer", "developer"]} }]'),
    ],
    "Software Engineering Manager": [
        ("engineer manager", '[{"LOWER": {"IN": ["engineer", "engineering", "developer", "development", "program"]} }, {"LOWER": "manager"}]'),
    ],
    "Junior QA Engineer": [
        ("junior qa engineer", '[{"LOWER": {"IN": ["junior", "jr.", "jr"]} }, {"LOWER": {"IN": ["qa", "test"]} }, {"LOWER": {"IN": ["engineer", "analyst"]} }]'),
        ("junior quality assurance engineer", '[{"LOWER": {"IN": ["junior", "jr.", "jr"]} }, {"LOWER": "quality"}, {"LOWER": "assurance"}, {"LOWER": {"IN": ["engineer", "analyst"]} }]'),
        ("junior software test engineer", '[{"LOWER": {"IN": ["junior", "jr.", "jr"]} }, {"LOWER": "software"}, {"LOWER": "test"}, {"LOWER": {"IN": ["engineer", "analyst"]} }]'),
        ("junior test engineer", '[{"LOWER": {"IN": ["junior", "jr.", "jr"]} }, {"LOWER": "test"}, {"LOWER": {"IN": ["engineer", "analyst"]} }]'),
    ],
    "QA Engineer": [
        ("qa engineer", '[{"LOWER": {"NOT_IN": ["senior", "sr.", "sr", "junior", "jr.", "jr"]} }, {"LOWER": {"IN": ["qa", "test"]} }, {"LOWER": {"IN": ["engineer", "analyst"]} }]'),
        ("quality assurance engineer", '[{"LOWER": {"NOT_IN": ["senior", "sr.", "sr", "junior", "jr.", "jr"]} }, {"LOWER": "quality"}, {"LOWER": "assurance"}, {"LOWER": {"IN": ["engineer", "analyst"]} }]'),
        ("software test engineer", '[{"LOWER": {"NOT_IN": ["senior", "sr.", "sr", "junior", "jr.", "jr"]} }, {"LOWER": "software"}, {"LOWER": "test"}, {"LOWER": {"IN": ["engineer", "analyst"]} }]'),
        ("test engineer", '[{"LOWER": {"NOT_IN": ["senior", "sr.", "sr", "junior", "jr.", "jr"]} }, {"LOWER": "test"}, {"LOWER": {"IN": ["engineer", "analyst"]} }]'),
    ],
    "Senior QA Engineer": [
        ("senior qa engineer", '[{"LOWER": {"IN": ["senior", "sr.", "sr"]} }, {"LOWER": {"IN": ["qa", "test"]} }, {"LOWER": {"IN": ["engineer", "analyst"]} }]'),
        ("senior quality assurance engineer", '[{"LOWER": {"IN": ["senior", "sr.", "sr"]} }, {"LOWER": "quality"}, {"LOWER": "assurance"}, {"LOWER": {"IN": ["engineer", "analyst"]} }]'),
        ("senior software test engineer", '[{"LOWER": {"IN": ["senior", "sr.", "sr"]} }, {"LOWER": "software"}, {"LOWER": "test"}, {"LOWER": {"IN": ["engineer", "analyst"]} }]'),
        ("senior test engineer", '[{"LOWER": {"IN": ["senior", "sr.", "sr"]} }, {"LOWER": "test"}, {"LOWER": {"IN": ["engineer", "analyst"]} }]'),
    ],

}