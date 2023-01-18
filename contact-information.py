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

        print(rawContents)


getThePageContents("https://misinforeview.hks.harvard.edu/article/twitter-flagged-donald-trumps-tweets-with-election-misinformation-they-continued-to-spread-both-on-and-off-the-platform/")