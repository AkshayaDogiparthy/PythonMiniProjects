import re

with open("input.txt", "r") as infile:
    content = infile.read()

email_list = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', content)

with open("extracted_emails.txt", "w") as outfile:
    outfile.write("\n".join(email_list))

print("Extracted Email Addresses:")
for address in email_list:
    print(address)

print("\nEmails saved to extracted_emails.txt")
