import re
with open("sample.txt","r") as file:
    content = file.read()
email_pattern = r"[a-zA-z0-9._%+-]+@[a-zA-z0-9.-]+\.[a-zA-Z{2,}]"
emails = set(re.findall(email_pattern,content))
with open("emails.txt","w") as output:
    for email in emails:
        output.write(email+"\n")
print("Extracted Email Address: ")
for email in emails:
    print(email)
print("\nEmails saved successfully in emails.txt")