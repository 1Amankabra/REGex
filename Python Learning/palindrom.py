


s = input()
def ispalindrom(s):

  n = len(s)
  if( s == s[:n:-1]):
    print("yes")
  else:
   print("no")  
  
ispalindrom(s)