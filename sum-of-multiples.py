def sum_of_multiples(a,b, n):
    ans=0
    for i in range (1,n):
     if(i%a==0 or i%b==0):
      ans=ans+i
    print("Sum of multiples of ", a,"and",b,
          "for all the natural numbers below ", n, " is ", int(ans))
 
# Driver Code
sum_of_multiples(3,5, 20)
