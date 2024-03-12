camel_case_vars = ["FirstItem", "FriendsList", "MyTuple"]
snake_case_vars = []

for var_name in camel_case_vars:
    snake_case = ""
    for char in var_name:
        if char.isupper() and snake_case:
            snake_case += "_" + char.lower()
        else:
            snake_case += char.lower()
    snake_case_vars.append(snake_case)

print(snake_case_vars)
