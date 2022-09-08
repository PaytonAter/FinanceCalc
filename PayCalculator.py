rate = int(input("Enter hourly rate: "))

earnings = int(input("Enter hours worked this week: "))

weekly_gross_pay = (rate*earnings)

tax_ten = .90
tax_twelve = .88
tax_twentytwo = .78
tax_twenytyfour = .76
tax_thirtytwo = .68
tax_thirtyfive = .65
tax_thirtyseven = .63

if weekly_gross_pay < 200:
    tax_bracket = tax_ten
elif 200.01 < weekly_gross_pay <= 803.39:
    tax_bracket = tax_twelve
elif 803.4 < weekly_gross_pay <= 1712.99:
    tax_bracket = tax_twentytwo
elif 1713 < weekly_gross_pay <= 3270.2:
    tax_bracket = tax_twenytyfour
elif 3270.21 < weekly_gross_pay <= 4152.89:
    tax_bracket = tax_thirtytwo
elif 4152.9 < weekly_gross_pay <= 10382.7:
    tax_bracket = tax_thirtyfive
else:
    tax_bracket = tax_thirtyseven

if earnings <= 40:
    print("Your earning will be: ~", (weekly_gross_pay)*tax_bracket)
    exit()

else:
    ot_earnings = earnings-40
base_earnings = earnings-ot_earnings
ot_rate = rate*1.5
print("Your earnings will be: ~",
      ((rate*base_earnings)+(ot_rate*ot_earnings))*tax_bracket)
