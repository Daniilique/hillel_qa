def sum_range(start, end):
    if start > end:
      start, end = end, start
    total = (end * (end + 1)) // 2 - ((start - 1) * start) // 2

    return total

# just some examples
print(sum_range(1, 5))
print(sum_range(3, 1))
