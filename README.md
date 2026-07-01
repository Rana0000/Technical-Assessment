# Technical-Assessment
## Overview

The script automates the process of identifying vendors with potential inconsistencies in the Global Vendor List (GVL) and prepares personalised emails for them.

## What the script does

- Reads the GVL JSON file.
- Checks each vendor.
- Identifies vendors where:
  - `usesCookies = true`
  - Purpose 1 is missing.
- Saves the Vendor ID and Vendor Name.
- Generates personalised emails for the identified vendors.
- Sends emails automatically using Python.

## Files

- `vendor_email_automation.py` – Main Python script.
- `sample_vendor_contacts.json` – Example contact list used by the script.

## Notes

The GVL JSON file is not included in this repository because it is publicly available and updated regularly.

It can be downloaded from:

https://vendor-list.consensu.org/v3/vendor-list.json
