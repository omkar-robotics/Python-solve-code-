'''Question 5: Write a python program to find the sum of all natural numbers between 1 to n.
Input:

n = 5

Output:

Sum = 15

Explanation:

The program adds numbers from 1 to 5.
1 + 2 + 3 + 4 + 5 = 15

'''
n=int(input("Enter a number: "))
if n<=0:
    print("{} invalid input".format(n))
else:
    sum=0
    i=1
    while i<=n:
        sum=sum+i
        i=i+1
print(sum)