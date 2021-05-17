
# getpass.getpass(prompt='Password: ', stream=None)
# Prompt the user for a password without echoing. The user is prompted using the string prompt, which defaults to 'Password: '.
# On Unix, the prompt is written to the file-like object stream using the replace error handler if needed.
# stream defaults to the controlling terminal (/dev/tty) or if that is unavailable to sys.stderr (this argument is ignored on Windows)
# getpass()
# from getpass import getpass

# try:
#     passwd = getpass()
#     print(passwd)
# except Exception as er:
#     print(f'er is {er}')
#
# else:
#     print(f"passwd is {passwd}")

import getpass
# pwd = getpass.getpass(prompt = 'What is your favorite colour?')
# if pwd == 'Crimson':
#    print('You are in!')
# else:
#    print('Try Again')

pwd = getpass.getpass(prompt='Password: ', stream=None)
print(pwd)

getpass.getpass(prompt='passwd ', stream=None)
# Warning: Password input may be echoed.
# passwd >? kdkd
# Out[7]: 'kdkd'
username = getpass.getuser()
print(username)
# return user login name
# Out[8]: 'jsun'

www = input("wwww is  ")
print(www)