name = input("Full Name: ")
phone = input("Phone: ")
email = input("Email: ")

vcard = f"""BEGIN:VCARD
VERSION:4.0
FN:{name}
TEL;TYPE=WORK:{phone}
EMAIL;TYPE=INTERNET:{email}
END:VCARD
"""

with open("1.vcf", "w") as f:
    f.write(vcard)

print("vCard created!")
