bal = float(raw_input('Enter the outstanding balance on your credit card:'))
annual_rate = float(raw_input('Enter the annual credit card interest rate as a decimal:'))

rate = 1.0 + annual_rate / 12.0

minPay = 0
newBal = bal
months = 0

while ( newBal > 0 ):
    print "test", months, minPay
    newBal = bal
    minPay += 10.0
    months = 0
    while ( months < 12):
        months += 1
        newBal = newBal * (rate) - minPay
        print newBal

print minPay, months
