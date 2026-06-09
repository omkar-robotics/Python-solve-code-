''' Question 2: Write a python program to print all natural numbers in reverse (from n to 1). using a while loop.
Input:

n = 5

Output:

5 4 3 2 1

Explanation:

The program starts from n and decreases the number by 1 each time.
The loop runs until the number becomes

'''
n=int(input("Enter the number: "))
if n<=0:
    print("{} invalid input".format(n))
else:
    i=n
    while i>=0:
        print("{}".format(i))
        i=i-1