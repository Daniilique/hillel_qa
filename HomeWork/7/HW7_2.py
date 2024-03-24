def my_func(x):
    return lambda y: y ** x
power_of_2 = my_func(2)
print(power_of_2(3))
power_of_3 = my_func(3)
print(power_of_3(4))
