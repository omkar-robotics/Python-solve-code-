'''Question 8: Write a python program to print a multiplication table of any number.
Input:

Number = 5

Output:

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50

Explanation:

The program multiplies the given number by values from 1 to 10.
Each result is printed in table format

'''
n=int(input("Enter a number: "))
if n<=0:
    print("{} invalid input ".format(n))
else:
    i=1
    while i<=n:
        print("{} x {} = {}".format(n,i,n*i))
        i=i+1
