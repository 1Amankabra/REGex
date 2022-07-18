s = input('enter value')
old = s
while(s):

   a = s % 10
   rev = rev * 10 + a
   s = s / 10

if(old == rev):
   print("yes")
else:
   print("no")