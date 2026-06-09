'''
Question 6: Write a python program to find the sum of all even numbers between 1 to n.
Input:

n = 10

Output:

Sum = 30

Explanation:

Even numbers between 1 and 10 are 2, 4, 6, 8, 10.
Their sum is 2 + 4 + 6 + 8 + 10 = 30.*/
'''
n=int(input("Enter a number: "))
if n<=0:
    print("{} invalid input".format(n))
else:
    sum=0
    i=2
    while i<=n:
        sum=sum+i
        i=i+2
print(sum)