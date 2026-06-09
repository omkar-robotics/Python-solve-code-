'''Question 10: Write a pyhon program to calculate the sum of digits in a number.
Input:

Number = 1234

Output:

Sum of digits = 10

Explanation:

The program separates each digit using modulus (%) and division (/).
Digits are 1, 2, 3, 4 and their sum is 1 + 2 + 3 + 4 = 10.

'''
n=int(input("Enter Number:"))
if n<=0:
    print("{} invalid input ".format(n))
else:
    sum=0
    while n > 0 :
        digit=n%10
        sum=sum+digit
        n=n//10
print("Sum of digits: {}".format(sum))
