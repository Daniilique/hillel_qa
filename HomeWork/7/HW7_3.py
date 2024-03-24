def print_hi():
    print("Hi")
def print_hello():
    print("Hello")
def print_greetings():
    print("Greetings")
function_name = input("Enter function name: ")

if function_name in globals() and callable(globals()[function_name]):
    eval(function_name + "()")
else:
    print("Function does not exist or is not callable.")
