import re

class phone():
 def __init__(self,phnum):
  self.phnum=phnum
  phnum=re.sub('[^A-Za-z0-9]+', '', phnum)
  phnum.strip()
  print(phnum)
  x=len(phnum)
  if(x==10):
   print("valid number = "+phnum)
  elif(x==11):
   if phnum[0]!=1:
    print("valid country code") 
   else:
    print("invalid number") 
  else:
   print("invalid number")
   



phnum = phone("+1 613-995-0253")

