import pandas as pd

class newAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        # 1. read the users csv file into the dataframe
        df = pd.read_csv('/todoUsers.csv')

        # 2. Verify if user account exist, if so, send error msg to user
        foundUser = df.loc[(df['username'] == username)] ####### & (df[self.password] == password)]
        if not foundUser.empty:
            print("Username is already taken")
        # 3. If not, save the new records and send success msg to user
        else:
            df2 = df.append(pd.DataFrame([[username, password]], columns=df.columns))
            df2.to_csv(r'/todoUsers.csv', index=False)
            print("Account saved successfully. Please login to view or create your todo list.")

class existingAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        # 1. read the users csv file into the dataframe
        df = pd.read_csv('/todoUsers.csv')

        # 2. Verify if user account is available, if so, send error msg to user
        foundUser = df.loc[(df['username'] == username)] ####### & (df[self.password] == password)]
        if foundUser.empty ==True:
            print("Invalid username or password.")
        # 3. If not, send success msg to user. Proceed with TODO tasks
        else:
            ans2 = input("Login is successful. Would you like to [V] view your existing TODO, or [A] add new items in teh list \n")
            if ans2 == 'V':
                viewTODO(username)
            elif ans2 == 'A':
                addTODO(username)
            else:
                 invalidOption()
class TODOtask:
    global df
    df = pd.read_csv('/todoTasks.csv')
    def __init__(self, username, date, time, description):
        self.username = username
        self.date = date
        self.time = time
        self.description = description
        df2 = df.append(pd.DataFrame([[username, date, time, description]], columns=df.columns))
        df2.to_csv(r'/todoTasks.csv', index=False)
        print("Record saved successfully.")

def viewTODO(xUser):
    df = pd.read_csv('/todoTasks.csv')
    foundTasks = df.loc[(df['username'] == xUser)]
    if not foundTasks.empty:
        print("Found your list:\n ")
        print(foundTasks)
    else:
        print("Sorry. Counldnt find any list \n")

def addTODO(xUser):
    ans3 = input("How many tasks you would like to add? \n")
    for a in range(int(ans3)):
        TODOtask(xUser,input(f"For task no {a +1}; Please type date as yyyy-mm-dd. \n"), input("Now please type time as hh:mm. \n"), input("Finally, please add a description \n"))

def invalidOption():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def TODO_bot():
    ans1 = input("Welcome to your TODO list. Would you like to [R] resgiter or [S] sign-in? \n")
    if ans1 == 'R':
        newAccount(input("Please type a username. \n"), input("Now please type a password. \n"))
    elif ans1 == 'S':
        existingAccount(input("Please type your username. \n"), input("Now please type your password. \n"))
    else:
        invalidOption()

TODO_bot()