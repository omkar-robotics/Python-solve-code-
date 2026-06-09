''' Question 4: Write a python program to print all odd numbers between 1 to 100.
Input:

No input required

Output:

1 3 5 7 ... 99

Explanation:

Odd numbers are not divisible by 2.
The program prints numbers where number % 2 is not equal to 0

'''
n=int(input("Enter the number: "))
if n<=0:
    print("{} invalid syntax".format(n))
else:
    i=1
    while i<=n:
        print("{} odd number".format(i))
        i=i+2