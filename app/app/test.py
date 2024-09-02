"""
Find the palindrome of the string. only consider alpha numeric value and ignore case sensitivity
 
nAman 
nAm, an
Na, ma ,n?
"""

def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    if (s == s[::-1]):
        return True
    else:
        return False 

print(is_palindrome("nAm, an"))
