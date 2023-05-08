login = input('Enter your login >>> ')

if login.isalpha():
    pass
else:
    print('Only letters are acceptable!')

password = input('Enter your password >>> ')

if password.isalnum():
    pass
else:
    print('Incorrect data!')

x = input('Confirm your password >>> ')
if x == password:
    print('You are logged in!')
else:
    print('Incorrect password!')

print('You were logged out due to your teacher preferences')
login_1 = input('Confirm your login again >>> ')
password_1 = input('Confirm your password again >>> ')
if login_1 == login and password_1 == password:
    print('Congratulations! You are logged in again!')
else:
    print('Incorrect data,try one more time!')








