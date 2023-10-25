##Write a program to check String is Palindrome or not.

def ispalindrome(s):
    return s == s [:: -1]

s = "anna"
a = ispalindrome(s)

if a:
    print("is palindrome")
else:
    print("is not palindrome")