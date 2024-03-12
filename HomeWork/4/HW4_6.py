user_input = input("Enter a string: ")

char_count = {}
for char in user_input:
    char_count[char] = char_count.get(char, 0) + 1

result = ', '.join(f"{char},{char_count[char]}" for char in char_count)
print("Expected result:", result)
