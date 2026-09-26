# LedgerPro Accountants - Password Policy

LedgerPro Accountants is a small accounting firm based in Lahore. This repository implements a secure password policy to protect client financial data, invoices, and tax records.

## Password Policy Rules
- Minimum 12 characters
- At least 1 uppercase letter (A-Z)
- At least 1 lowercase letter (a-z)
- At least 1 number (0-9)
- At least 1 special character (!@#$%^&*)
- Must NOT contain company name "LedgerPro" or "ledgerpro"
- Must NOT be a common password like "password123"
- Cannot reuse last 3 passwords

## How to Run
1. Make sure Python 3 is installed
2. Run the checker:
   python policy_checker.py

## How to Check / Test
Run with test data:
   python policy_checker.py --test
This will validate sample LedgerPro users and show if passwords pass or fail.

## Sample Data
This project uses realistic accounting data:
- Users: ali.ahmed@ledgerpro.pk (Senior Auditor), sara.khan@ledgerpro.pk (Tax Consultant)
- Clients: Al-Hamd Traders, Crescent Textiles Pvt Ltd
- Invoices: INV-LP-2025-1045, INV-LP-2025-1046
