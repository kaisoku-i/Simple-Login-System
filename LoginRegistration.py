import csv
import re

class user_choice():
    def choose(choice):
        item=selection[choice]
        if callable(item):
            item()

class user_registration(user_choice):

    def __init__(self, email,password):
        self.email=email
        self.password=password
    
    def Register():
        email_pattern=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}\b'
        password_pattern=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$"
        user_credentials=[]

        while True:
            email=input("Enter your email id: ")
            if not re.fullmatch(email_pattern,email):
                print('Enter valid email')    
            else:
                user_credentials.append(email)
                break

        while True:
            password=input("""Enter your password: Password should contain below
                        password length(5-16)
                        Must have minimum one special character
                        one digit
                        one uppercase 
                        one lowercase character : """)
            if not re.fullmatch(password_pattern,password):
                print('Invalid Password')      
            else: 
                user_credentials.append(password)
                break

        with open("UserDetails.csv","a+",newline='') as file:
            csv.writer(file).writerow(user_credentials)
            file.close()

        print("Registered Successfully!!!")
    
    def Login():
        email=input("Enter your registered email id: ")        
        with open("UserDetails.csv",newline='') as file:
            email_list=[row[0] for row in csv.reader(file)]
            file.close()
            if email in email_list:
                print("Logged in!!!")
                quit()
            else:   
                print("""User doesn't exist please register:
                            1.Login
                            2.Register
                            3.Forget Password""")
            choice=input()
            user_choice.choose(choice)

    def ForgetPassword():
        email=input("Enter your registered email id: ")        
        with open('UserDetails.csv') as file:
            email_list=[row[0] for row in csv.reader(file)]
            file.close()
        with open('UserDetails.csv') as file:
            password_list=[row[1] for row in csv.reader(file)]
            file.close()
    
        if email in email_list:
            print("Your Password is: ",password_list[email_list.index(email)])
            quit()
        else:
            print("""User doesn't exist please register:
                            1.Login
                            2.Register
                            3.Forget Password""")
        choice=input()
        user_choice.choose(choice)

    def Exit():
        quit()

def field_writer():
    with open("UserDetails.csv","a+",newline='') as file:
        if file.tell()==0:
            csv.writer(file).writerow(['user_email','user_password'])
        file.close()

field_writer()

selection={"1":user_registration.Login,"2":user_registration.Register,"3":user_registration.ForgetPassword,"4":user_registration.Exit}
print("""Select an option:
    1.Login
    2.Register
    3.Forget Password
    4.Exit""")
choice=input()
user_choice.choose(choice)
