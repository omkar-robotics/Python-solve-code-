'''Question 9: Write a python program to count the number of digits in a number
Input:

Number = 12345

Output:

Number of digits = 5

Explanation:

The program divides the number by 10 repeatedly until it becomes 0.
Each division reduces one digit, and a counter keeps track of total digits.

'''
n = int(input("Enter Number: "))

if n <= 0:
    print("{} invalid input".format(n))

else:
    count = 0

    while n > 0:
        count = count + 1
        n = n // 10

    print("Number of digits =", count)
