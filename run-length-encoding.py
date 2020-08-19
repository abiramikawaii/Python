class rle:
 def __init__(self,s):
  self.s=s
  l=len(s)
  i=0
  count=1
  string = ""

  for i in range(0,l-1):
   if(s[i] == s[i+1]):
    count+=1
   elif(s[i] != s[i+1]):
    if(count != 1):
     string += str(count) + s[i]
    else:
     string += s[i]
    count=1

  if(count != 1):
   string += str(count) + s[l-1]
  else:
   string += s[l-1]

  print(string)



s = rle("wwwwaaadexxxxaxxb")


