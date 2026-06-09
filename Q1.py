''' /*Question 1: Write a python  program to print all natural numbers from 1 to n. using while loop.
Input:
n = 5

Output:
1 2 3 4 5

Explanation:
The program starts from 1 and prints numbers one by one until it reaches n.
The while loop continues as long as the number is less than or equal to n.

'''
n=int(input("Enter the number: "))
if n<=0:
    print("{} invalid input ".format(n))
else:
    i=1
    while i<=n:
        print("{}".format(i))
        i=i+1