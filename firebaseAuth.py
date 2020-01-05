import pyrebase
import json
from getpass import getpass

with open('config.json') as config_file:
    firebaseConfig = json.load(config_file)

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def get_em_and_pw():
    email = input('Please enter your email: ')
    password = getpass('Please enter your pw: ')
    return email, password

def sign_up(em, pw):
    try:
        sign_up = auth.create_user_with_email_and_password(em, pw)
        auth.send_email_verification(sign_up['idToken'])
        print('Verification email sent to your email address')
    except Exception as e:
        print('ERROR')
        print(e)

def login(em, pw):
    try:
        auth.sign_in_with_email_and_password(em, pw)
        print ('Login Successfull')
    except Exception as e:
        print('ERROR')
        print(e)

while True:
    decision = input('Login (L) or Sign up (S)? ')
    if decision.upper() == 'L':
        login(*get_em_and_pw())
        print('...')
        break
    elif decision.upper() == 'S':
        sign_up(*get_em_and_pw())
    else:
        print('Please choose L or S. ')
        pass


