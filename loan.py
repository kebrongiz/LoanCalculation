def loan_calc():
    loan_amt = int(input("Enter Loan Amount: "))
    no_of_years = int(input("Enter Number of years: "))

    rates = []
    rate = 5

    while rate < 8.125:
        rates.append(rate)
        rate += 0.125

    print("{:<15} {:15} {:15}".format(
        "Interest Rate", "Monthly", "Payment Total"))

    for i in rates:
        rate = i / 100
        monthly_rate = ((rate) / 12)
        no_payments = no_of_years * 12
        monthly_payment = (loan_amt * (monthly_rate)) * 10 / \
            (1 - (1 + (monthly_rate))**(-1 * no_payments))
        total_payment = monthly_payment * no_payments
        print("{:.3%}\t\t{:.2f}\t\t{:.2f}".format(
            (i/100), monthly_payment, total_payment))


loan_calc()
