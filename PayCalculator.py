rate = int(input("Enter hourly rate: "))

earnings = int(input("Enter hours worked: "))

if earnings <= 40:
    print("Your earning will be: ~", (rate*earnings)*.75)
    exit()

else:
    ot_earnings = earnings-40
base_earnings = earnings-ot_earnings
ot_rate = rate*1.5
print("Your earnings will be: ~", ((rate*base_earnings)+(ot_rate*ot_earnings))*.75)
