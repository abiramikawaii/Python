sentence = input("enter the first strand ")
sentence1= input("enter the second strand ")
count=0
l=len(sentence)
l1=len(sentence1)
if (l != l1):
 print("The length of two strands does not match")
else:
 for i in range(0,l): 
  if(sentence[i]!=sentence1[i]):
   count+=1 
 print(str(count) + " is the hamming distance between the given strands")



