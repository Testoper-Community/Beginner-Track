#AUTHOR : VIKAS RATHOD
#TODO APP

import mysql.connector
from datetime import datetime
from prettytable import from_db_cursor

#connected to mysql database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="vik@password",
    database="todo"
)

mycursor = db.cursor()

mycursor.execute("create database if not exists `todo`;")

mycursor.execute("""
CREATE TABLE IF NOT exists `todo`.`cred` (
  `username` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  PRIMARY KEY (`username`)
)""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS `todo`.`data` (
  `id` INT(10) NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(255) NOT NULL,
  `status` VARCHAR(45) NOT NULL,
  `title` VARCHAR(255) NOT NULL,
  `description` LONGTEXT NULL,
  `dateofcreation` DATE NOT NULL,
  `deadline` DATE NULL,
  `timestamp` DATETIME NOT NULL,
  `updated` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);
  """)

class account:

    def __init__(self):
        pass

    def start(self):
        try:
            tasks = (input('What would you like to do? \n1:[Register] \n2:[Login] \n3:[quit]\nChoose only one option from given choice: '))
            # Calling functions with that class object
            if tasks == '1':
                username = (input('Please enter username: '))
                password = (input('Please enter password: '))
                time = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
                self.register(username, password, time)

            elif tasks == '2':
                self.login()

            elif tasks == '3':
                print("See you later!")
                Stop = True

            else:
                print("❗❗❗ wrong input try again ❗❗❗\n")
                return self.start()

        except Exception as e:
            print('Error: ', e)
            return None

    def register(self,un, pw, time):
        try:
            newcred = "INSERT INTO cred (username,password,timestamp) VALUES (%s,%s,%s)"
            val = (un,pw,time)
            mycursor.execute(newcred,val)
            db.commit()
            print("Successfully registered, Please login again")
            self.login()

        except mysql.connector.IntegrityError:
            print("\nUSERNAME ALREADY EXIST, TRY AGAIN:\n")
            return self.start()
        except Exception as e:
            print('Error: ',e)
            return None

    def login(self):
        try:
            un = str(input("Enter username : "))
            pw = str(input("Enter Password (case sensetive): "))

            username = mycursor.execute("select * from cred WHERE username = '{}'".format(un))

            fetch_data = mycursor.fetchall()
            fetch_username = fetch_data[0][0]
            fetch_password = fetch_data[0][1]

            if pw == fetch_password:
                print("\nlogin sucessful\n")
                self.select_option(un)
            else:
                print("Wrong credentials, Let's try again....\n")
                return self.login()
        except IndexError:
            print("\nWrong credentials, Let's try again....\n")
            return self.login()
        except Exception as e:
            print('Error: ', e)
            return None

    def select_option(self,un):
        try:
            option = input("\n{} What would you like to do:\n1.Current Tasks 2.Insert Task 3.Complete Task 4. Delete Task 5. Check History 6.Exit\nEnter your choice from above: ".format(un))
            if option == '1':
                return self.current_tasks(un)
            elif option == '2':
                return self.add_task(un)
            elif option == '3':
                return self.complete_task(un)
            elif option == '4':
                return self.delete_task(un)
            elif option == '5':
                return self.get_all_tasks(un)
            elif option == '6':
                print("See you later, {} !!!".format(un))
                pass
            else:
                print("❗❗❗ wrong input try again ❗❗❗")
                return self.select_option(un)
        except Exception as e:
            print('Error: ', e)
            return None

    def pending_task(self,un):
        try:
            global fetch_username
            mycursor.execute("SELECT id, status, title, description,dateofcreation,deadline,updated FROM data where status = '⚫' and username = '{}' ".format(un))
            print(from_db_cursor(mycursor))
            self.select_option(un)
        except Exception as e:
            print('Error: ', e)
            return None

    def get_all_tasks(self,un):
        try:
            global fetch_username
            mycursor.execute("SELECT id, status, title, description,dateofcreation,deadline,updated FROM data where username = '{}' ".format(un))
            print(from_db_cursor(mycursor))
            self.select_option(un)
        except Exception as e:
            print('Error: ', e)
            return None

    def current_tasks(self, un):
        try:
            global fetch_username
            mycursor.execute("SELECT id, status, title, description,dateofcreation,deadline,updated FROM data where status = '⚫' and username = '{}' ".format(un))
            print(from_db_cursor(mycursor))
            self.select_option(un)
        except Exception as e:
            print('Error: ', e)
            return None

    def add_task(self,un):
        try:
            title = str(input("Enter Title: "))
            desc = str(input("Enter Description:\n"))
            deadline = str(input("Enter deadline format(YYYY-MM-DD): "))
            time = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
            createdate = datetime.today().strftime('%Y-%m-%d')
            mycursor.execute("INSERT INTO data (username, status, title, description, dateofcreation, deadline, timestamp) VALUES ('{0}','⚫','{1}','{2}','{3}','{4}','{5}')".format(un,title,desc,createdate,deadline,time))
            db.commit()
            print(" TASK ADDED SUCCESSFULLY ")
            self.select_option(un)
        except Exception as e:
            print('Error: ', e)
            return None

    def complete_task(self,un):
        try:
            complete = str(input("Enter ID: "))
            #UPDATE list SET status = ':check_mark:' WHERE id = 109
            mycursor.execute("UPDATE data SET status = '✔' WHERE id = {}".format(complete))
            db.commit()
            print(" TASK COMPLETED SUCCESSFULLY ")
            self.select_option(un)
        except Exception as e:
            print('Error: ', e)
            return None

    def delete_task(self,un):
        delete_id = input("Chose ID to delete task: ")
        try:
            mycursor.execute("delete from data where id ='{}'".format(delete_id))
            db.commit()
            print(" TASK DELETED SUCCESSFULLY ")
            self.select_option(un)
        except Exception as e:
            print('Error: ', e)
            return None


print("WELCOME to ✔ TO-DO ✔ APP")
ac =  account()
ac.start()