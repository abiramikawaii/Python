def abbreviate(txt):
 text=txt
 p = str()
 l=len(text)
 for i in range(0,l):
  if (text[i].isupper()):
    p += text[i]
 print (p)




abbreviate("All India Radio")

