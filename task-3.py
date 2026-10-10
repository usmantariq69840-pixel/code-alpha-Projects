import os
import re

input_file = "input.txt"
output_file = "emails.txt"

if not os.path.exists(input_file):
    print("Can't find", input_file, "- put it in the same folder as this script.")
    exit()

f = open(input_file, "r")
text = f.read()
f.close()

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
found = re.findall(pattern, text)

emails = []
for e in found:
    e = e.lower()
    if e not in emails:
        emails.append(e)

if len(emails) == 0:
    print("No email addresses found in", input_file)
else:
    out = open(output_file, "w")
    for e in emails:
        out.write(e + "\n")
    out.close()

    print("Found", len(emails), "email addresses:")
    for e in emails:
        print(" ", e)
    print("Saved them to", output_file)