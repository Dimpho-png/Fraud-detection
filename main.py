# Cyber Gardians - Fraud Spotter for Hackathon 27th-28th
import csv

print("--- Fraud Spotter Starting ---")

def spot_fraud():
    fraud_count = 0
    try:
        with open('transactions.csv', 'r') as f:
            reader = csv.DictReader(f)
            print(f"Found columns: {reader.fieldnames}\n")

            for i, row in enumerate(reader, 1):
                # get amount safely no matter the column name
                amount_str = row.get('amount') or row.get('Amount') or row.get('AMOUNT') or '0'
                amount = float(str(amount_str).replace('R','').replace(',','').strip() or 0)

                # Simple fraud rules
                is_fraud = False
                reason = ""

                if amount > 10000:
                    is_fraud = True
                    reason = "Large amount"

                if amount < 0:
                    is_fraud = True
                    reason = "Negative amount"

                if is_fraud:
                    fraud_count += 1
                    print(f"🚨 ROW {i} FRAUD: R{amount} - {reason} - {row}")
                else:
                    print(f"✅ ROW {i} OK: R{amount}")

        print(f"\nDone! {fraud_count} fraud cases found.")

    except FileNotFoundError:
        print("ERROR: transactions.csv not found!")
        print("Create a file called transactions.csv on your Desktop with this inside:")
        print("date,amount,description")
        print("2026-10-25,500,groceries")
        print("2026-10-25,15000,unknown transfer")

spot_fraud()