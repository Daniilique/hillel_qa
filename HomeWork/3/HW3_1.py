def is_palindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False
word = input("Enter a word to check: ")
if is_palindrome(word):
    print(f"{word} + YES it is a palindrome.")
else:
    print(f"{word} - is NOT a palindrome.")
