"""
Lessons for learning data types in Python
"""


# Lists
banks = ["charles schwab", "capital one", "american express"]

# Dict
banks = [
    {"name": "charles schwab"},
    {"name": "capital one"},
    {"name": "american express"},
]

# Tuples
cash_accounts = ("checking", "savings")
investment_accounts = ("stock", "bond", "mutual_fund")
credit_accounts = ("credit_card", "student_loan", "mortgage")
print("The largest credit account is", max(credit_accounts), "\n")

#------------------------------------------------------------------

# List iteration
for bank in banks:
  print(bank)

# Dict deconstruction
bank_names = [bank["name"] for bank in banks]
print(bank_names)
