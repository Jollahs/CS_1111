def is_palindrome1(s):
    # iterate over first half of string
    for i in range(len(s)//2):
        # at each index, check the character is the same as that opposite
        if s[i] != s[-(i+1)]:
            return False
    return True


def is_palindrome2(s):
    # iterate over WHOLE string
    for i in range(len(s)):
        # at each index, check the character is the same as that opposite
        if s[i] != s[-(i+1)]:
            return False
    return True

def is_palindrome3(s):
    # create a reversed copy of the string
    s2 = ""
    for i in range(len(s)):
        s2 = s[i] + s2
    return s == s2

def parkers_is_palindrome(s):
    # create a reversed copy of the string
    rev_s = s[::-1]
    palindrome_check = (rev_s == s)
    return palindrome_check

    
for word in ["racecar", "John Jacob Jingleheimer Schmidt", "rotator"]:
    if parkers_is_palindrome(word):
        print(word, "is a palindrome")
