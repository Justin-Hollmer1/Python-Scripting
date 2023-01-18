# This application will take in a website URL
# and return all the contact information for that website,
# like the email address, phone number, etc.

import re
import requests
from bs4 import BeautifulSoup

# TODO -- Get an entire webpage and store it in a variable.

def getThePageContents(url):

    response = requests.get(url)

    if response.status_code==200:
        print("The web page has been opened: The contents of the page are: ")


        rawContents = BeautifulSoup(response.text, 'html.parser')
        emailAddressRegex = re.compile(r'((?<=>)[A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,}<)+')
        emailAddress = emailAddressRegex.search(str(rawContents)).group()
        print("The email address is: " + emailAddress[0:-1])


getThePageContents("https://justin-hollmer1.github.io/")