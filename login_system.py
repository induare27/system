#implement a user login system in python,
#user should be provided with 2 options login and register,
#login should take user name and password, 
#register should take the user details and save the user
#2 types of users, regular user and the admin user, if admin user user logs in he should be able to see all the regular users and
#if a regular user logs in show him his name.

class Login:
    def __init__(self):
        pass
    def login_acc(self,user_name,password,user_details):
        if len(user_details)<1:
            print("\nNo user information exist so, user should register first.\n")
            return
        for d in user_details:
             if d["user_name"]==user_name and d["password"]==password:
                if d["user_type"]=="admin":
                        print("Admin account")
                        for d in user_details:
                            print(d["name"])
                        return
                elif d["user_type"]=="regular":
                    print("Regular user account")
                    for d in user_details:
                        if d["user_name"]==user_name and d["password"]==password:
                            print(d["name"])
                            return
        print("\nUsername/password doesn't exit, please check your user_name/password.")
        print("Incase if you dont have any account please register first.\n")
        return
    def delete_acc(self,user_name,password,user_details):
        if len(user_details)<1:
            print("\nNo user information exist to delete account.\n")
            return
        for d in user_details:
            if d["user_name"]==user_name and d["password"]==password:
                user_details.remove(d)
                print("Account is deleted.")
                return
        print("\nUsername/password doesn't exit, please check your user_name/password to delete.")
        return
class Register:
    def __init__(self):
        pass
    def register_acc(self,name,user_name,user_type,password,email,dob,user_details):
        for d in user_details:
            if d["user_name"]==user_name:
                print("This username is already taken, try with another one.Incase you already registered then, please log in")
                return
        user_details.append({
                    "name":name,
                    "user_name":user_name,
                    "user_type":user_type,
                    "password":password,
                    "email":email,
                    "dob":dob
                })
        print("Successfully registered your account.")
        return

def main():
    user_details=[]
    ls=Login()
    rs=Register()
    while True:
        print("Choice 1 - Login")
        print("Choice 2 - Register")
        print("Choice 3 - Delete")
        Choice=int(input("Enter your choice: "))
        if Choice==1:
                print("__Login account__")
                user_name=input("Enter user name: ")
                password=input("Enter password: ")
                ls.login_acc(user_name,password,user_details)
        elif Choice==2:
                print("\n__Register account__")
                print("User details")
                print("Please mention user type as admin or regular.")
                name=input("Enter your name: ")
                user_name=input("Enter user name: ")
                user_type=input("Enter user type: ")
                password=input("Enter password: ")
                email=input("Enter your mail id: ")
                dob=input("Enter your Date of birth: ")
                if user_type=="admin" or user_type=="regular:
                    rs.register_acc(name,user_name,user_type,password,email,dob,user_details)
                else:
                    print("\nUser type is wrong, please check it and register again.")
        elif Choice==3:
                print("__Delete account__")
                user_name=input("Enter user name: ")
                password=input("Enter password: ")
                ls.delete_acc(user_name,password,user_details)
        elif Choice==4:
            print("Exiting...")
            break
        else:
            print("Enter valid choice.")

if __name__=="__main__":
    main()
