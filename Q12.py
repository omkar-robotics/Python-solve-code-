'''
Question 12: Write a python program to calculate the product of digits in a number.
Input:

Number = 1234

Output:

Product of digits = 24

Explanation:

Digits are extracted one by one.
1 × 2 × 3 × 4 = 24.
'''
n=int(input("Enter Number:"))
if n<=0:
    print("Invalid Input".format(n))
else:
    sum=1
    while n>0:
        digit=n%10
        sum=sum*digit
        n=n//10
print(sum)