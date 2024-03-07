def find_word(text, word):
    if text.find(word) != -1:
        return 'YES'
    else:
        return 'NO'
user_text = input("Enter the whole text: ")
search_word = input("Enter the word to findin text above: ")
result = find_word(user_text, search_word)
print(result)
