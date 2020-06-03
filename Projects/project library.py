import sqlite3
import pandas as pd
#from sqlalchmy import create_engine
import string
from random import *
import secrets
import csv
import datetime as dt
from csv import reader
from time import sleep

rowcount = 0
name = " ",
email = " ",
address = " "
username = " "
password = " "
reset = False

now = dt.datetime.now()

filename = "Login_file.csv"
file   = "Login_file.csv"#define write parameters
#engine = create_engine('sqlite://', echo = False)

print('Enter 1 for Sign in or 2 for Registration')
x = int(input())

line_count = 0

def reset_function():
   print("inside reset")
   characters = string.ascii_letters + string.punctuation  + string.digits
   password1 =  "".join(choice(characters) for x in range(randint(8, 16)))

   character = string.ascii_letters
   user_char = "".join(choice(characters) for x in range(randint(8, 16)))

def write_order(username, password):
    file   = "Orders Centric.xlsx"
    output = "Orders Centric1.xlsx"


        #creating a database in the memory

 #   engine = create_engine('sqlite://', echo = False)

    # Read excel data from sheet 1
    df = pd.read_excel(file, Sheet_name="Sheet1")
    start = dt.datetime.now()
    # df['date'] = start + start
    df['date'] = start + dt.timedelta(12)
    df["Entry Date"] = start

    result = df[df['User'] == "joy"]
    print(result)
    print ("file has been updated for: " , username)

    sleep (4)
    df.to_excel(output)

if x == 1:
    login = False
    username = input("Username: ")
    password = input("Password: ")
    with open("Login_file.csv", 'r') as csvfile:
        csv_reader = csv.reader(csvfile)

        for row in csv_reader:

            if line_count == 0:
                line_count += int(line_count+1)
            else:

                if row[4] == username and row[5] == password:

                   login = True
                else:

                    if row[3] != username or row[4] != password:
                        reset = True

                    else:
                        login = False
                if login == False and reset != True:
                   print("Complete New User Registration.")
                   exit()
                else:
                   if reset == True:
                      reset_function()

                   else:
                      print("You are now logged in!")
                      print("Enter ""Y"" to write order details or ""N"" to Exit")
                      x = input()
                      if x == "Y":
                          write_order(username, password)
                      else:
                          exit()
elif x == 2:
      print('Enter Name')
      name=input()
      print('email')
      email=input()
      print('Address')
      address=input()
      print('User Name')
      username = input()
      print('Password')
      password = input()

header = ("Row Number","Name", "email", "Address", "User Name", "Password", "User Type","Date and Time")
data = (line_count, name, email, address, username, password, "User", now)

def writer(header, data, filename):
        with open (filename, "w+", newline = "") as csvfile:
            with open (filename, "r") as csvread:

                 userdata = csv.writer(csvfile)
                 readdata = csv.reader(csvread)
                 #row_count = sum(1 for row in csvread)

                 #results = pd.read_csv(filename)
                 #print (results)
                 #print(len(results))
                 userdata.writerow(header)
                 userdata.writerow(data)
writer(header,data,filename)
