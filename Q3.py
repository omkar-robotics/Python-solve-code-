''' Question 3: Write a python program to print all even numbers between 1 to 100.- using while loop
Input:

No input required

Output:

2 4 6 8 ... 100

Explanation:

Even numbers are divisible by 2.
The program checks each number from 1 to 100 and prints it if it is divisible by 2

'''
n=int(input("Enter the number: "))
if n<=0:
    print("{} invalid input ".format(n))
else:
    i=2
    while i<=n:
        print("{} natural number ".format(i))
        i=i+2