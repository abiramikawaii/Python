
def atbash(plaintxt): 
 plaintext = plaintxt 
 cipher = "zyxwvutsrqponmlkjihgfedcba"
 print("the plain text is " + plaintext)
 text = encryptMessage(cipher, plaintext)
 print("the encrypted text is " + text )
 text = decryptMessage(cipher, plaintext)
 print("the decrypted text is " + text )
 
 
def encryptMessage( cipher, plaintext):
 text = ''
 charsA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 charsB =  cipher
 for symbol in plaintext:
  if symbol.upper() in charsA:
   symIndex = charsA.find(symbol.upper())
   if symbol.isupper():
    text += charsB[symIndex].upper()
   else:
    text += charsB[symIndex].lower()
  else:
   text += symbol
 return text


def decryptMessage( cipher, plaintext):
 text = ''
 charsB = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 charsA =  cipher
 for symbol in plaintext:
  if symbol.upper() in charsA:
   symIndex = charsA.find(symbol.upper())
   if symbol.isupper():
    text += charsB[symIndex].upper()
   else:
    text += charsB[symIndex].lower()
  else:
   text += symbol
 return text
 
 


atbash(" gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt")






