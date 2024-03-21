def get_user_input():
  return eval(input("Enter a list, tuple, dictionary, or integer: "))
def print_data_type(data):
  try:
    if isinstance(data, dict):
      print(f"User is going to work with a dictionary.")
    else:
      raise TypeError
  except TypeError:
    try:
      if isinstance(data, list):
        print(f"User is going to work with a list.")
      else:
        raise TypeError

    except TypeError:
      try:
        if isinstance(data, tuple):
          print(f"User is going to work with a tuple.")
        else:
          raise TypeError

      except TypeError:
        print(f"User is going to work with an integer.")
user_data = get_user_input()
print_data_type(user_data)
