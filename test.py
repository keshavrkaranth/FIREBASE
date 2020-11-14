from pyrebase import pyrebase


conf = {'apiKey': "AIzaSyDETON3XBDIZMyOSeLAmuoYUz6hNTte3Gs",
        'authDomain': "testdjango-3c1af.firebaseapp.com",
        'databaseURL': "https://testdjango-3c1af.firebaseio.com",
        'projectId': "testdjango-3c1af",
        'storageBucket': "testdjango-3c1af.appspot.com",
        'messagingSenderId': "176178552105",
        'appId': "1:176178552105:web:63e740248851fc73c3eb38",
        }

firebase = pyrebase.initialize_app(conf)
auth = firebase.auth()
auth.send_password_reset_email("keshavarkarantha@gmail.com")
auth.
def signup(auth,email,password):
    try:
        auth.create_user_with_email_and_password(email=email,password=password)
        print("User is created Sucesssfully")
    except :
        print('User Alredy Exixst')


def login(auth,email,password):
    try:
        auth.sign_in_with_email_and_password(email=email,password=password)
        print("Login Sucess")
    except:
        print("User dosent exist")


print("1.Signup\n2.Login\n3.Exit")
choice = int(input("Enter your choice: "))




if choice==1:
    email = input('Enter your Email: ')
    password = input("Enter your Password: ")
    signup(auth=auth,email=email,password=password)

elif choice==2:
    email = input('Enter your Email: ')
    password = input("Enter your Password: ")
    login(auth,email=email,password=password)
else:
    exit()