def my_map(func, iterable):
    for item in iterable:
        yield func(item)
def my_filter(func, iterable):
    for item in iterable:
        if func(item):
            yield item
#For my_Map
result_map = my_map(lambda x: x**2, [1, 2, 3, 4, 5])
print(list(result_map))  # Need to be : [1, 4, 9, 16, 25]

# For My_Filter
result_filter = my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
print(list(result_filter))  # Output: [2, 4]
