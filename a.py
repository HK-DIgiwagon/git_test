print("Main branch push.")
print("New New change 1")
print("New New change 2")
print("login added")
print("new login feature")
print("new login feature v2")


def login():
    user=input("Enter username: ")
    password=input("Enter password: ")
    print(f"Logging in {user}...")
    user=check_credentials(user, password)
    if user:
        print("Login successful!")
    else:
        print("Login failed. Please check your credentials.")
