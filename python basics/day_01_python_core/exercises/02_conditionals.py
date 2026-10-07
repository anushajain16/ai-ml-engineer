old_passwords = []

while True:
    new_password = input("Enter your new password: ")

    if new_password in old_passwords:
        print("Password cannot be same as any of the last 3 passwords used.")
    elif len(new_password) < 10:
        print("Password must be at least 10 characters long.")
    elif not any(char.islower() for char in new_password):
        print("Password must contain at least one lowercase alphabet [a-z].")
    elif not any(char.isupper() for char in new_password):
        print("Password must contain at least one uppercase alphabet [A-Z].")
    elif not any(char.isdigit() for char in new_password):
        print("Password must contain at least one numeric character [0-9].")
    elif not any(char in "_@$" for char in new_password):
        print("Password must contain at least one special character from [ _ @ $ ].")
    else:
        old_passwords.append(new_password)

        if len(old_passwords) > 3:
            old_passwords.pop(0)

        print("Password changed successfully.")
        # ask again
        again = input("Do you want to change password again? (y/n): ")
        if again.lower() != "y":
            break