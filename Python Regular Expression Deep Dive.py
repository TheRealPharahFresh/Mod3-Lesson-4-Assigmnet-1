# Task 1: 
# Email Extraction Enhancement

# Problem Statement: 
# You have a script that extracts email addresses from a text but needs to be refined to exclude certain domains 
# (e.g., '[exclude.com](http://exclude.com/)'). Modify the script to extract all email addresses except those from the specified domain.



import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
pattern = r"\w+@domain\.com"
emails = re.findall(pattern, text)
print(emails)
