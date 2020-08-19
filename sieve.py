def sieve(n):
   primerange=n
   primenumber= [True for i in range(n+1)]
   p= 2
   while (p*p <= primerange) :
    if (primenumber[p] == True):
     for i in range(p*2, primerange+1, p):
      primenumber[i] = False
      p=p+1
   for p in range(2, primerange):
    if primenumber[p]:
     print(p)




sieve(30)
