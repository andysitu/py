bal = float(raw_input('Enter the outstanding balance on your credit card:'))
annual_rate = float(raw_input('Enter the annual credit card interest rate as a decimal:'))

rate = 1.0 + annual_rate / 12.0

low = round(bal/12, 2)
up = round((bal * rate ** 12) / 12, 2)
newBal = bal

while ( newBal >= 0 or newBal <= -0.2):
    newBal = bal
    guess = (low + up) / 2
    for  i in range (0, 12):
          newBal = newBal * (rate) - guess
    if newBal > 0:
        low = guess
    elif newBal < 0:
        up = guess
print 'Result'
print 'Monthly payment to pay off debt in 1 year:', round(guess, 2)
print 'Number of months need:', i
print 'Balance:', round(newBal,2)
