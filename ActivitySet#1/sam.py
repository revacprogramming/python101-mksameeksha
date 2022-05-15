def computepay(h,r):
  if h>40:
    Gross_pay=(h-40) *r * 1.5 + 40*r
  else:
    Gross_pay=h*r
  print('In computepay',h,r)
  return Gross_pay 

hrs=input("Enter hrs : ")
h=float(hrs)
rate=input("Enter rate :")
r=float(rate)

Gross_pay = computepay(h,r)
print('Pay:', Gross_pay)
  