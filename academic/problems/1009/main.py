saler_name = str(input())
saler_salary = float(input())
sales_in_month = float(input())

month_payment = saler_salary + ((15.00 / 100) * sales_in_month)

print(f"TOTAL = R$ {month_payment:.2f}")
