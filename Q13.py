'''
Question 14: Write a java program to check whether a number is palindrome or not.
Input:

Number = 121

Output:

Palindrome

Explanation:

The reversed number of 121 is also 121.
Since original and reversed numbers are equal, it is a palindrome
'''
word=input("enter your value :")
print(" palindrome" if word==word[::-1] else "not palindrome")