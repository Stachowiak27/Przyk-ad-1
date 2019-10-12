
def check_palindrome(word):
    if word[:] == word[::-1]:
        return True
    else:
        return False

c = check_palindrome("anna")

print(c)