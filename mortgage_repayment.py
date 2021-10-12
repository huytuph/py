print("""
>> Mortgage Repayment Calculator <<
""")

p = float(input("Principal ammount: ")) # Principal loan ammount
i = float(input("Interest Rate p.a: ")) / 100 # Interest rate
t = int(input("Term: ")) # Duration of the loan in years
n = int(input("Number of repayments per year: ")) # number of repayments p.a

bal = p * -1 # remaining Balance

r_n = n * t # remaining Number of payments

i_n = i / n # interest Rate per repayment

i_charged = (bal * -1) * i_n # interest charged per repayment
p_pay = bal / r_n # Principal payable per repayment

i_total = 0 # total Interest paid
n_total = 0 # total Number of payments

while bal < 0:
    i_total += i_charged
    n_total += 1
    r_n -= 1
    bal -= p_pay
           
y = n_total // n # years
m = n_total % n # months

print(f"""
===========================================
total Interest Paid: {i_total}
total Number of repayments made: {n_total}
Paid off in: {y} years and {m} months
current balance: {bal}
""")
