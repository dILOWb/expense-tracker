print("========================================")
print("EXPENSE TRACKER")
print("Know where your money goes.")
print("========================================")
print("MAIN MENU")
print("[1] Add an expense (coming soon)")
print("[2] View all expenses (coming soon)")
print("[3] Show total spent (coming soon)")
print("[4] Exit (coming soon)")

user_name = input("What's your name? ")
print(f"Welcome, {user_name}! Let's log two expenses.")

expense1_name = input("First expense? ")
expense1_amount = float(input("Amount? "))

if expense1_amount > 200:
    print("  Huge expense - are you sure?")
elif expense1_amount > 100:
    print("  Big expense.")
elif expense1_amount > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

expense2_name = input("Second expense? ")
expense2_amount = float(input("Amount? "))

if expense2_amount > 200:
    print("  Huge expense - are you sure?")
elif expense2_amount > 100:
    print("  Big expense.")
elif expense2_amount > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

if expense1_amount > 100 and expense2_amount > 100:
    print("  Two big expenses in a row - slow down!")

tax_rate = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

subtotal = expense1_amount + expense2_amount
average = subtotal / 2
tax_amount = subtotal * (tax_rate / 100)
grand_total = subtotal + tax_amount
over_budget = grand_total > budget
left_in_budget = budget - grand_total

print("-" * 40)
print("SUMMARY")
print(f"- {expense1_name}: ${expense1_amount}")
print(f"- {expense2_name}: ${expense2_amount}")
print(f"Subtotal: ${subtotal}")
print(f"Average: ${average}")
print(f"Tax ({tax_rate}%): ${tax_amount}")
print(f"Grand total: ${grand_total}")

if over_budget:
    print(f"Over budget by ${abs(left_in_budget)}!")
elif grand_total > (budget * 0.90):
    print(f"Careful: only ${left_in_budget} left.")
else:
    print(f"Within budget. ${left_in_budget} left.")

print("-" * 40)
print(f"Made by: {user_name} | Installment 4")