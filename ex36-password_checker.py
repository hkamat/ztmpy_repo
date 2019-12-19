import getpass

user_name = input('Please enter your user name: ')
password = getpass.getpass(prompt='Please enter your password: ')

print(f'{user_name}, your password {"*" * len(password)} is {len(password)} letters long.')
print('Hello')
