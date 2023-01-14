import pyperclip
import re
import PyPDF2


# This should be a file that takes in a resume and prints
# out the owners email address and phone number


# Takes in the file path to the resume file
pdfFile = open('../Justin_Hollmer_Resume.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFile)

# A quick test to make sure that it al works correctly
# print("The resume has: " + str(len(pdfReader.pages)) + " pages")

# Now storing the page text in the page text variable.
pageObject = pdfReader.pages[0]
pageText = pageObject.extract_text()
# print("The page text is " + pageText)

# Defining a couple of other parameters
phoneNumberRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
otherPhoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumber = phoneNumberRegex.search(pageText)







print(phoneNumber.group())
