#conditional execution

hrs=input('Enter hours:\n')
h=float(hrs)
rate=input('Enter rate:\n')
r=float(rate)
if h>40:
    Gross_pay=(h-40)*r*1.5+ 40*r
else:
    Gross_pay=h*r
print(Gross_pay)