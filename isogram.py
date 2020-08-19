
def is_isogram(word):
 a = word.lower()
 x=True
 for char in a:
  if a.count(char) >1:
   x = False
 if(x==True):
  print("isogram sentence")
 else:
  print("not a isogram sentence")

is_isogram("cara")

