#implement a user login system in python,
#user should be provided with 2 options login and register,
#login should take user name and password, 
#register should take the user details and save the user
#2 types of users, regular user and the admin user, if admin user user logs in he should be able to see all the regular users and
#if a regular user logs in show him his name.

def login(user_name,reg_data,data):
    if user_name=="admin":
        print(reg_data)
    else:
        if user_name in data:
            print(data.get(user_name))
            return
        else:
            print("user_name doesn't exit, please check your user_name or if you dont have any account please register first.")
            return

def register(user_name,reg_data,data,adm_data,name):
    if user_name =="admin":
        if user_name not in adm_data:
            adm_data.append(user_name)
        return
    elif user_name not in reg_data:
        reg_data.append(user_name)
        data[user_name]=name
        return
    else:
        print("This user_name is already taken, try with another one.Incase you already registered then, please log in")
        return
def main():
    reg_data=[]
    adm_data=[]
    data={}
    while True:
        print("Choice 1 - Login")
        print("Choice 2 - Register")
        Choice=int(input("Enter your choice: "))
        if Choice==1:
            user_name=input("Enter Username: ")
            password=input("Enter password: ")
            login(user_name,reg_data,data)
            
        elif Choice==2:
            print("User Details")
            user_name=input("Enter Username: ")
            password=input("Enter password: ")
            name=input("Enter your name: ")
            register(user_name,reg_data,data,adm_data,name)
        elif Choice==3:
            print("Exiting...")
            break
        else:
            print("Enter a valid choice.")

if __name__=="__main__":
    main()
        