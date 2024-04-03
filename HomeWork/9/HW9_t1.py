def custom_range(start, stop, step=1):
    current = start
    while current < stop:
        yield current
        current += step
for i in custom_range(1, 16, 2):
    print(i)
