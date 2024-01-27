# input(furrerw)
# input(Password1!)

# print("{username}, your password \"{******}\" is {passwordlength} is characters long")


# My first solution ------------------------------------------------------------
# username = input("Username: ")
# password = input("Password: ")
# password_example = "*" * 10

# print(f"{username}, your password \"{password_example}\" is {len(password)} characters long.")

# My first solution ------------------------------------------------------------

# Andrei's Solution ------------------------------------------------------------

username = input('what is your username?')
password = input('what is your password?')

password_length = len(password)
hidden_password = '*' * password_length

print(f'{username}, your password, {hidden_password}, is {password_length} letters long')


