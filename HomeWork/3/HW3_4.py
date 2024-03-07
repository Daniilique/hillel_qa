def display_last_three_elements(text):
    words_list = text.split()
    if len(words_list) < 3:
        print("The number of elements is less than 3. Current number of elements:", len(words_list))
    else:
        print("Last 3 elements from the list:", words_list[-3:])

user_text = input("Enter text separated by spaces: ")
display_last_three_elements(user_text)
