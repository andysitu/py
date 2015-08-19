bal = float(raw_input('Enter the outstanding balance on your credit card:'))
inter = float(raw_input('Enter the annual credit card interest rate as a decimal:'))
payRate = float(raw_input('Enter the minimum monthly payment rate as a decimal'))

for i in range(1, 13):
    print 'Month: ', i
    minPay = payRate * bal
    print 'Minimum monthly payment: $' + str(round(minPay , 2))
    interPay = inter / 12 * bal
    prinPay = minPay - interPay
    print 'Principle paid: $' + str(round(prinPay , 2))
    bal = bal - prinPay
    print 'Remaining balance: $' + str(round(bal , 2))
