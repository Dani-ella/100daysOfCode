#This code allows user to input a positive integer (m) and displays the sum of values from 1 to that integer (m).

m = int(input("\n Enter any positive integer for m \n")) # allows user input   
sum_score = (m * (m + 1)) / 2 

# For 1, sum gives 1, for 2, sum gives 3, for 3, sum gives 6. Coining a simple formula for any integer 'm' will be the
#product of the integer 'm' amd the integer'm' plus 1. The result of this divided by 2. Simply put as (m*(m+1))/2 

print("\n Total score for sum is : ",sum_score ) # displays recult for sum from 1 to m.
