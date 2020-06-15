import db
from db import session, User, Task
from datetime import datetime, date

# Class to register first users
class Register:
    def __init__(self, username, password, confirm_password):
        self.username = username
        self.password = password
        self.confirm_password = confirm_password

    # This is to store user data into the db. Store user id, username, password, and corresponding confirm password
    def saveDetails(self):
        user = User(self.username, self.password, self.confirm_password)
        session.add(user)
        session.commit()

# class to log in an existing user. check on username and password
class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    # method to check if user exist in the db
    def confirmUser(self):
        result = session.query(User).filter(User.username == self.username). \
            filter(User.password == self.password)
        for user in result:
            return user.id
        
# Class to fetch user existing todo. 
class ViewTask:
    def __init__(self, currennt_user):
        self.currennt_user = currennt_user

    # method to list user todos if any exist
    def view(self):
        for user, task in session.query(User, Task).\
            filter(Task.user_id == self.currennt_user).\
            all():
            print(task.title)


# Class to add new todo and store into db. with parameters["Title", "Descriptions", "Date_Created", "Due_Date", "User_foriegn key"]
class CreateTask(Login):
    def __init__(self, title, description, date_created, due_date, user_id=""):
        self.title = title
        self.description = description
        self.date_created = date_created
        self.due_date = due_date
        # self.user_id = user_id
    

    # method to store user todo with associated user
    def createTask(self):
        current_user = super().confirmUser()
        if current_user == None:
            print("\nInvalid credentials")
        else: 
            task = CreateTask(self.title, self.description, self.date_created, self.due_date, current_user)
            session.add(task)
            session.commit()
            print("You have successfully add task")


