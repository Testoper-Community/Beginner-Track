from app import signup, login, wrongOption

def run():
    print("\t\t\t\t\t\t\t\t\t\t\t\nTodoApp\n" + "\nWelcome to TodoApp.\n\nBasicly this app signup new users, then allow user to login with valid details.\nHence you can either 'Add New' task to your list or 'View' your task lists")
    print("\nLet get going........\n")
    print("Login? Enter 'Login'\nSigup? Enter 'Signup'\n")

    userOption = input("Action here.....  ")
    userOption = userOption.capitalize()
    if userOption == "Login":
        login()

    elif userOption == "Signup":  
        if signup():
            print("\nLogin to continue...")
            login()
    else:
        wrongOption()    

# method to start app
run()

