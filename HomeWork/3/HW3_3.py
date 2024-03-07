def validate_email(email):
    if '@' in email and '.' in email:
        return 'YES'
    else:
        return 'NO'

user_email = input("Enter an email address: ")
result = validate_email(user_email)
print(result)
