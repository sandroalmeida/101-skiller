import re
import sys
import os

# # Get the absolute path of the current script
# current_dir = os.path.dirname(os.path.abspath(__file__))

# # Add the 'resources' folder to the Python module search path
# resources_path = os.path.join(current_dir, '..', '..', 'application/resources')
# sys.path.append(resources_path)

regex_test = [
        "(senior|sr.|sr)\s+(software|programmer|application|system|systems|computer)\s+(engineer|developer|programmer)",
    ]
test_string = "senior software engineer"

for regex in regex_test:
    if re.match(regex, test_string.lower(), re.IGNORECASE):
        print(regex)
        print(re.search(regex, test_string))

# if any(
#     (isinstance(item, str) and item.lower() == test_string.lower()) or
#     (isinstance(item, str) and re.search(item, test_string))
#     for item in regex_test):
#     print("Found")

# match = re.search(regex_test.pop(0), test_string)
# print(match)

# if match:
#     print("Match at index %s, %s" % (match.start(), match.end()))

# from v2.skill_patterns_dictionary import skill_patterns

# for skill, patterns in skill_patterns.items():
#     print(skill)
#     for items in patterns:
#         print(items[0], ' - ', items[1])
