types = [1, 1000, 2, 12, {'key': 'value'}]

for item in types:
    if not isinstance(item, int):
        print(f"The loop does not work with {type(item)} data type")
        break
    print(item)
