def dos(n):
 print("The number is "+str(n))
 square_of_sum = sum(range(1,n+1))**2
 sum_of_squares = sum(i*i for i in range(1,n+1))
 difference_of_squares = square_of_sum - sum_of_squares
 print("The difference between the square of the sum and the sum of the squares is "+str(difference_of_squares))
    

dos(10)
