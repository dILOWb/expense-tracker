print("=" * 40)
print("  EXPENSE TRACKER - Installment 5")
print("=" * 40)

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

print(f"Welcome, {name}!")

subtotal = 0.0
count = 0

while True:
    print("\nMAIN MENU")
    print("[1] Add an expense")
    print("[2] View all expenses (coming soon)")
    print("[3] Show total spent")
    print("[4] Exit")
    
    choice = input("Choose 1-4: ")
    
    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1
        
        if amount > 200:
            print("Huge expense - are you sure?")
        elif amount > 100:
            print("Big expense.")
        elif amount > 50:
            print("Moderate expense.")
        else:
            print("Small expense.")
            
    elif choice == "2":
        print("Coming soon: the tracker can't remember each item yet.")
        
    elif choice == "3":
        tax_amount = subtotal * (tax_percent / 100)
        grand_total = subtotal + tax_amount
        
        print(f"Expenses: {count}")
        print(f"Subtotal: ${subtotal:.1f}")
        print(f"Tax ({tax_percent:.1f}%): ${tax_amount:.1f}")
        print(f"Grand total: ${grand_total:.1f}")
        
        if grand_total > budget:
            over_amount = grand_total - budget
            print(f"Over budget by ${over_amount:.1f}!")
        elif grand_total >= budget * 0.9:
            left_amount = budget - grand_total
            print(f"Careful: only ${left_amount:.1f} left.")
        else:
            left_amount = budget - grand_total
            print(f"Within budget. ${left_amount:.1f} left.")
            
    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("-" * 40)
        print(f"Made by: {name} | Installment 5")
        print("=" * 40)
        break
        
    else:
        print("Please choose 1, 2, 3 or 4.")