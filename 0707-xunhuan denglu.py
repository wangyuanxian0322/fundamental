user = "wyx"
pwd = "1111"
count = 0;
while count < 3:
    username = input("username:")
    password = input("password:")
    if username == user and password == pwd:
        print("Welcome Login")
        count = 3
    else:
        print('Wrong username or password')
        count = count + 1
        print('you can try', 3 - count, 'times')