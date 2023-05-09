login = input('Enter your login >>> ')
password = input('Enter your password >>> ')

if not login.isalpha():
    print('Login must contain only letters!')
elif not password.isalnum():
    print('Password must contain only letters or/and numbers!')
else:
    x = input('Confirm your password >>> ')
    if x == password:
        print('You are logged in!')
        print('You were logged out due to your teacher preferences')
        login_1 = input('Confirm your login again >>> ')
        password_1 = input('Confirm your password again >>> ')
        if login_1 == login and password_1 == password:
            print('Congratulations! You are logged in again!')
        else:
            print('Incorrect data,try one more time!')
    else:
        print('Incorrect password!')








