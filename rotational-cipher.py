def rotc(string,k):
 #string="ABC"
 #k=12
 string=string.lower()
 encryptedmessage=''
 for char in string:
  c=(ord(char)+k)%126
  if c<32:
   c+=31
  encryptedmessage+=chr(c)
 print(encryptedmessage)




rotc("ABC",3)

