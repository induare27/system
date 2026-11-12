#implement a user login system in python,
#user should be provided with 2 options login and register,
#login should take user name and password, 
#register should take the user details and save the user
#2 types of users, regular user and the admin user, if admin user user logs in he should be able to see all the regular users and
#if a regular user logs in show him his name.

class System:
    def __init__(self):
        self.reg_users=[]
        self.adm_users=[]
    def login(self,user_name,password,data,isadmin):
        if len(data)<1:
            print("No user information exist so, user should register first.")
            return
        if isadmin:
                for d in data:
                    print(d["user_name"])
                return
        else:

            for d in data:
                if d["user_name"]==user_name and d["password"]==password:
                    print(d["name"])
                    return
        print("Username/password doesn't exit, please check your user_name/password." \
                    " Incase if you dont have any account please register first.")
        return
        


    def register(self,name,user_name,password,email,dob,data,adm_data,isadmin):
        if isadmin:
            if user_name not in self.adm_users:
                adm_data.append({
                    "name":name,
                    "user_name":user_name,
                    "password":password,
                    "email":email,
                    "dob":dob
                })
                self.adm_users.append(user_name)
                return
            else:
                print("This username is already taken, try with another one.Incase you already registered then, please log in")
                return

        else:
            if user_name not in self.reg_users:
                data.append({
                    "name":name,
                    "user_name":user_name,
                    "password":password,
                    "email":email,
                    "dob":dob
                })
                self.reg_users.append(user_name)
                return
            else:
                print("This username is already taken, try with another one.Incase you already registered then, please log in")
                return

def main():
    data=[]
    adm_data=[]
    ls=System()
    while True:
        print("Choice 1 - Login")
        print("Choice 2 - Register")
        Choice=int(input("Enter your choice: "))
        if Choice==1:
            print("Choice 1 - Admin login.")
            print("Choice 2 - Regular user login.")
            isadmin=False
            choice=int(input("Enter your choice: "))
            user_name=input("Enter user name: ")
            password=input("Enter password: ")
            if choice==1:
                isadmin=True
                ls.login(user_name,password,data,isadmin)
            elif choice==2:
                ls.login(user_name,password,data,isadmin)
            else:
                print("Enter valid choice.")
        elif Choice==2:
            print("User details")
            print("Choice 1 - Admin register.")
            print("Choice 2 - Regular user register.")
            isadmin=False
            choice=int(input("Enter your choice: "))
            name=input("Enter your name: ")
            user_name=input("Enter user name: ")
            password=input("Enter password: ")
            email=input("Enter your mail id: ")
            dob=input("Enter your Date of birth: ")
            if choice==1:
                isadmin=True
                ls.register(name,user_name,password,email,dob,data,adm_data,isadmin)
            elif choice==2:
                ls.register(name,user_name,password,email,dob,data,adm_data,isadmin)
            else:
                print("Enter valid choice.")
        elif Choice==3:
            print("Exiting...")
            break
        else:
            print("Enter valid choice.")

if __name__=="__main__":
    main()
        
