import re

pattern = r"hello"
string = "hello world"

match1 = re.match(pattern, string)

if match1:
    print("Match found")
else:
    print("No match found")
