from user import Register, Login, ViewTask, CreateTask

# method to view specific user todos
def viewtask(current_user):
    viewtask = ViewTask(current_user)   
    viewtask.view()     

# method to create todo with login user
def Newtask(current_user):
    title = input("title: ")
    if not validateInput(title):
        trial = 1
        while trial < 3:
            title = input("Title: ")
            trial +=1
    else:
        description = input("Description: ")
        if not validateInput(description):
            trial = 1
            while trial < 3:
                description = input("Description: ")
                trial +=1
        else:
            date_created = input("Today Date: ")
            if not validateInput(date_created):
                trial = 1
                while trial < 3:
                    date_created = input("Today Date: ")
                    trial +=1
            else:
                due_date = input("End Date: ")
                if not validateInput(due_date):
                    trial = 1
                    while trial < 3:
                        due_date = input("End Date: ")
                        trial +=1
                else:
                    create = CreateTask(title, description, date_created, due_date, current_user)
                    submit = create.createTask()
                    if submit == None:
                        print("OOPS! Unable to add task")
                    else:
                        viewtask(current_user)

# Method to signup new user 
def signup():
    username = input("Username: ")
    if not validateInput(username):
        trial = 1
        while trial < 3:
            username = input("Usename: ")
            trial +=1
    else:
        password = input("Password: ")
        if not validateInput(password):
            trial = 1
            while trial < 3:
                password = input("Password: ")
                trial +=1
        else:
            confirm_password = input("Confirm Password: ")
            if not validateInput(confirm_password):
                trial = 1
                while trial < 3:
                    password = input("Password: ")
                    trial +=1
            elif not matchPassword(password, confirm_password):
                trial = 1
                while trial < 3:
                    confirm_password = input("Confirm Password: ")
                    trial +=1
            else:
                signup = Register(username, password, confirm_password)
                save = signup.saveDetails()
                if save == None:
                    return "OOPS!!! Unable to registry you. 'TRY AGAIN'"
                else:
                    return "Signed up sucessfully"

# method to login new user 
def login():
    username = input("Username: ")
    if not validateInput(username):
        trial = 1
        while trial < 3:
            username = input("Usename: ")
            trial +=1
    else:
        password = input("Password: ")
        if not validateInput(password):
            trial = 1
            while trial < 3:
                password = input("Password: ")
                trial +=1
        else:
            login = Login(username, password)
            current_user = login.confirmUser()
            if current_user == None:
                print("Invalid Credentials")
            else:
                print("\nTo View Existing todo? Enter 'View'\nTo Add New Todo? Enter 'New'\n")
                userInput = input("Type here..... ")
                userInput = userInput.capitalize()

                if userInput == "View":
                    viewtask(current_user)
                elif userInput == "New":
                    Newtask(current_user)
                else:
                    wrongOption()


# method to validate user enter fields
def validateInput(field):
    # username = input("Username: ")
    if field == '':
         print("This field is required")
    elif len(field) < 5:
        print("field should be more than 5 chars min")
    else:
        return True

# function to check if user password match confirm password
def matchPassword(password, confirm_password):
    if password != confirm_password:
        print(f"\n Please enter same 'Confirm Password' as {password}!")
    else:
        return True


def wrongOption():
    print("Sorry! Please enter corresponding option for your response.\nRun program again by 'py run.py'")
