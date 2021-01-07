count = 0 
while True: 
    userName = input("enter your username: ") 
    password = input("enter your password: ")
    count = count + 1
    if count == 3: 
        break 
    else:
        if userName == 'elmo' and password == 'blue':
            print("welcome to page")
        else:
            print("username and password wrong")