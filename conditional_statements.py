# Example: Checking account status
account_balance = 8000
min_balance_required = 1000

if account_balance >= 10000:
    print("Premium Account: No extra charges.")
elif account_balance >= min_balance_required:
    print("Standard Account: Minimum balance maintained.")
else:
    print("Low Balance Warning: Please deposit funds.")
