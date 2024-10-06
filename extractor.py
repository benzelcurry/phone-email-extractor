import pyperclip, re

phone_regex = re.compile(r'''(
    (?:\d{3}|\(\d{3}\))?              # area code
    (?:\s|-|.)?                       # separator
    \d{3}                           # first 3 digits
    (?:\s|-|.)                        # separator
    \d{4}                           # last 4 digits
    (?:\s*(ext|x|ext.)\s*\d{2,5})?    # extension
    )''', re.VERBOSE)

email_regex = re.compile(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}')

page_contents = pyperclip.paste()

phone_numbers = phone_regex.findall(page_contents)
email_addresses = email_regex.findall(page_contents)

print(phone_numbers)
print(email_addresses)
