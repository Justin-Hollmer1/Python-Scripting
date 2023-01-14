import re

message = "The phone number is 111-111-1111"

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('REDACTED', "Agent bob shot Agent 48 in the head."))

