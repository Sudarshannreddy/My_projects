total_bill = float(input("Enter total bill: \n"))
tip_percentage = float(input("Enter percentage of tip (10, 12, or 15): \n"))
split = int(input("How many people should the bill be split?\n"))

# Calculate tip amount
tip_amount = total_bill * (tip_percentage / 100)

# Total bill including tip
final_bill = total_bill + tip_amount

# Split per person
split_amount = final_bill / split

print(f"Your total split should be: {split_amount:.2f}")
