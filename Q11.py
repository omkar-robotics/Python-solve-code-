'''
Question 11: Write a python program to calculate the product of digits in a number.
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
    print("{} invalid input".format(n))
else:
    reverse=0
    while n>0:
        digit=n%10
        reverse=reverse*10+digit
        n=n//10
print(reverse)