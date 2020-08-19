def is_pangram(word):
 w1 = word.lower()
 x=True
 alph="abcdefghijklmnopqrstuvwxyz"
 for char in alph:
  if char not in w1:
   x = False
 if(x==True):
  return True
 else:
  return False


is_pangram("gog")
