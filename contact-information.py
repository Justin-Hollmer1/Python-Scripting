# This application will take in a website URL
# and return all the contact information for that website,
# like the email address, phone number, etc.

import re

# TODO -- Get an entire webpage and store it in a variable.

# webpage = urllib2.urlopen("")
phoneNumberString = "The phone number is 111-111-1111 and it's pretty basic."

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
theObject = phoneNumberRegex.search(phoneNumberString)
print(theObject.group(2))
