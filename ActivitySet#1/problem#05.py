def computepay(hours,rate):
  if hours>40:
    Gross_pay=(hours-40) * rate * 1.5 +40 * rate
  else:
    Gross_pay= hours*rate
    print('In computepay', hours,rate)
    return Gross_pay

hours=float(input('Enter horurs'))
rate=float(input('Enter rate'))

Gross_pay = computepay(hours,rate)
print('Pay:', Gross_pay)
