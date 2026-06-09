'''Question 7: Write a python program to find the sum of all odd numbers between
Input:

n = 10

Output:

Sum = 25

Explanation:

Odd numbers between 1 and 10 are 1, 3, 5, 7, 9.
Their sum is 1 + 3 + 5 + 7 + 9 = 25.


'''
n=int(input("Enter a number: "))
if n<=0:
    print("{} invalid input".format(n))
else:
    sum=0
    i=1
    while i<=n:
        sum=sum+i
        i=i+2
print(sum)