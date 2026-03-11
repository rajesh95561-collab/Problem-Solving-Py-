# Write a program that calculates the in-hand salary after deducting HRA (10%), DA (5%), PF (3%), and tax.
# If the salary is between 5-10 lakh, apply a 10% tax;
# for salaries between 11-20 lakh, apply a 20% tax;
# for salaries above 20 lakh, apply a 30% tax.
# If the salary is between 0-1 lakh, print 'k'.

salary = float(input("Enter your salary in lakhs: "))

if 0 <= salary <= 1:
    print("k")
else:
    # Deduct HRA (10%), DA (5%), PF (3%)
    hra = salary * 0.10
    da = salary * 0.05
    pf = salary * 0.03
    taxable_income = salary - (hra + da + pf)

    # Apply tax based on slabs
    if salary > 20:
        tax = taxable_income * 0.30
    elif 11 <= salary <= 20:
        tax = taxable_income * 0.20
    elif 5 <= salary <= 10:
        tax = taxable_income * 0.10
    else:
        tax = 0

    in_hand_salary = taxable_income - tax
    print(f"Your in-hand salary is {in_hand_salary:.2f} lakhs.")



