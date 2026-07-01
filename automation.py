import json
import os
import csv


with open("vendor-list.json", "r", encoding="utf-8") as file:
    gvl = json.load(file)

with open("vendor_contacts.json", "r", encoding="utf-8") as file:
    contacts = json.load(file)

contradictory_vendors = []

for vendor_id, vendor in gvl["vendors"].items():

    uses_cookies = vendor.get("usesCookies", False)
    purposes = vendor.get("purposes", [])

    if uses_cookies and 1 not in purposes:

        contradictory_vendors.append({
            "id": vendor_id,
            "name": vendor.get("name"),
            "email": contacts.get(vendor_id, {}).get("email", "No email available")
        })


os.makedirs("generated_emails", exist_ok=True)

log = []

for vendor in contradictory_vendors:

    email_text = f"""To: {vendor['email']}
Subject: Possible inconsistency in your TCF declaration

Hello,

We identified a possible inconsistency in your TCF declaration.

Vendor ID: {vendor['id']}
Vendor Name: {vendor['name']}

Our review found that your declaration indicates usesCookies = true, but Purpose 1 is not declared.

Could you please review your declaration?

Kind regards,
IAB Europe
"""

    safe_name = "".join(c for c in vendor["name"] if c.isalnum() or c in (" ", "_", "-")).strip()

    filename = f"generated_emails/{vendor['id']}_{safe_name}.txt"

    with open(filename, "w", encoding="utf-8") as email_file:
        email_file.write(email_text)

    log.append([
        vendor["id"],
        vendor["name"],
        vendor["email"],
        "Generated"
    ])


with open("generated_emails/report.csv", "w", newline="", encoding="utf-8") as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow([
        "Vendor ID",
        "Vendor Name",
        "Email",
        "Status"
    ])

    writer.writerows(log)

print(f"{len(contradictory_vendors)} emails generated successfully.")
print("Email log saved as generated_emails/report.csv")