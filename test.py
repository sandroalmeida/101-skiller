import re

regex_test = ["test", "\w+\sc\s\w+"]
test_string = "xxx Python c Java xxxx"

for item in regex_test:
    print(item, re.search(item, test_string).string)

if any(
    (isinstance(item, str) and item.lower() == test_string.lower()) or
    (isinstance(item, str) and re.search(item, test_string))
    for item in regex_test):
    print("Found")

# match = re.search(regex_test.pop(0), test_string)
# print(match)

# if match:
#     print("Match at index %s, %s" % (match.start(), match.end()))
    