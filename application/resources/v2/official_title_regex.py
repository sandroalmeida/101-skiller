official_title_regex = {
    "Software Engineer Intern": [
        "software\s+development\s+engineer\s+(intern|internship)",
        "programmer\s+analyst\s+(intern|internship)",
        "programmer\/analyst\s+(intern|internship)",
        "(engineer|developer|programmer)\s+(intern|internship)",
    ],
    "Junior Software Engineer": [
        "(junior|jr.|jr)\s+(software|programmer|application|system|systems|computer)\s+(engineer|developer|programmer)",
        "(junior|jr.|jr)\s+software\s+development\s+engineer",
        "(junior|jr.|jr)\s+programmer\s+analyst",
        "(junior|jr.|jr)\s+programmer\/analyst",
    ],
    "Intermediate Software Engineer": [
        "intermediate\s+(software|programmer|application|system|systems|computer)\s+(engineer|developer|programmer)",
        "intermediate\s+software\s+development\s+engineer",
        "intermediate\s+programmer\s+analyst",
        "intermediate\s+programmer\/analyst",
        "software\s+engineer\s+i",
    ],
    "Software Engineer": [
        "(\w+\s+)?((software|programmer|application|system|systems|computer)\s+(engineer|developer|programmer))(\s+\w+)?"
        "(\w+\s+)?software\s+development\s+engineer(\s+\w+)?",
        "(\w+\s+)?programmer\s+analyst(\s+\w+)?",
        "(\w+\s+)?programmer\/analyst(\s+\w+)?",
        "(contractor|consultant|associate)\s+(engineer|developer|programmer)",
        "(engineer|developer|programmer|software|technical)\s+(contractor|consultant|associate)",
    ],
    "Senior Software Engineer": [
        "(senior|sr.|sr)\s+(software|programmer|application|system|systems|computer)\s+(engineer|developer|programmer)"
        "(senior|sr.|sr)\s+software\s+development\s+engineer",
        "(senior|sr.|sr)\s+programmer\s+analyst",
        "(senior|sr.|sr)\s+programmer\/analyst",
        "(software|programmer|application|system|systems|computer)\s+(engineer|developer|programmer)\s+(iii,iv)",
        "(senior|sr.|sr)\s+(engineer|developer|programmer)",
    ],
    "Staff Software Engineer": [
        "staff\s+(software|programmer|application|system|systems|computer)\s+(engineer|developer|programmer)"
        "staff\s+software\s+development\s+engineer",
        "staff\s+programmer\s+analyst",
        "staff\s+programmer\/analyst",
        "staff\s+(engineer|developer|programmer)",
    ],
    "Principal Software Engineer": [
        "principal\s+(software|programmer|application|system|systems|computer)\s+(engineer|developer|programmer)"
        "principal\s+software\s+development\s+engineer",
        "principal\s+programmer\s+analyst",
        "principal\s+programmer\/analyst",
        "principal\s+(engineer|developer|programmer)",
    ],
    "Lead Software Engineer": [
        "lead\s+(software|programmer|application|system|systems|computer)\s+(engineer|developer|programmer)"
        "lead\s+software\s+development\s+engineer",
        "lead\s+programmer\s+analyst",
        "lead\s+programmer\/analyst",
        "lead\s+(engineer|developer|programmer)",
        "(technical|tech)\s+lead",
    ],
    "Software Engineering Manager": [
        "(engineer|engineering|developer|development|program)\s+manager",
    ],
    "Junior QA Engineer": [
        "(junior|jr.|jr)\s+qa\s+(engineer|analyst)",
        "(junior|jr.|jr)\s+quality\s+assurance\s+(engineer|analyst)",
        "(junior|jr.|jr)\s+software\s+test\s+(engineer|analyst)",
        "(junior|jr.|jr)\s+test\s+(engineer|analyst)",
    ],
    "QA Engineer": [
        "(\w+\s+)?qa\s+(engineer|analyst)(\s+\w+)?",
        "(\w+\s+)?quality\s+assurance\s+(engineer|analyst)(\s+\w+)?",
        "(\w+\s+)?software\s+test\s+(engineer|analyst)(\s+\w+)?",
        "(\w+\s+)?test\s+(engineer|analyst)(\s+\w+)?",
    ],
    "Senior QA Engineer": [
        "(senior|sr.|sr)\s+qa\s+(engineer|analyst)",
        "(senior|sr.|sr)\s+quality\s+assurance\s+(engineer|analyst)",
        "(senior|sr.|sr)\s+software\s+test\s+(engineer|analyst)",
        "(senior|sr.|sr)\s+test\s+(engineer|analyst)",
    ],
}