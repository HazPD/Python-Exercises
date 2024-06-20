
income = float(input("Enter the annual income: ")) # first dot

if income < 85528:
	tax = income * 0.18 - 556.02

else:
    tax = (income - 85528) * 0.32 + 14839.02

if tax < 0.0:
    tax = 0.0

    
tax = round(tax,0)
print("The tax is:", tax, "thalers")
