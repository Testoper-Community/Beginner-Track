"""
import db
from db import session, User, Task
from datetime import datetime, date

class UserClass:
    def __init__(self, username, password, confirm_password=''):
        self.username = username
        self.password = password
        self.confirm_password = confirm_password


    def registerUser(self):
        user = User(self.username, self.password, self.confirm_password)
        session.add(user)
        session.commit()
        return True


    def loginUser(self): 
        result = session.query(User).filter(User.username == self.username). \
            filter(User.password == self.password)
        for user in result:
            return user.user_id

class TaskClass(UserClass):

    def __init__(self, title, description, date_created, due_date, user_id):
        self.title = title
        self.description = description
        self.date_created = date_created
        self.due_date = due_date
        self.user_id = user_id
        
    def createTask(self):
        task = TaskClass(self.title, self.description, self.date_created, self.due_date, self.user_id)
        session.add(task)
        session.commit()
        print("You have successfully add task")
        

    def viewTask(self):
        for tasks in session.query(Task).\
           filter(User.username==self.username).\
           filter(User.password==self.password):
           print(users)


        for user, task in session.query(User, Task).\
            filter(Task.user_id==1).\
            all():
            print(task.title)
            # print(user.username)

adduser1 = AddUser("Jonasjoe", "mypassword", "pass")
adduser2 = AddUser("femi", "password", "pass")
adduser3 = AddUser("daniel", "password1", "pass")
adduser4 = AddUser("james", "password1", "pass")
adduser5 = AddUser("olaide", "password2", "pass")
adduser1.registerUser()
adduser2.registerUser()
adduser3.registerUser()
adduser4.registerUser()
adduser5.registerUser()


user = TaskClass("Jonas", "John", "John", "22-22-22", 1)
user.viewTask()

date1 = datetime.now()
addtask = TaskClass("Title", "some descriptions", date1, date1)
addtask.viewTask()
"""









