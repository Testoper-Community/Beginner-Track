import csv
# import os.path
class User():
    def __init__(self, username = None, password = None, confirm_password = None):
        self.username = username
        self.password = password
        self.confirm_password = confirm_password


    def registerUser(self):

        # testfields = self.test(username, password, confirm_password)
        # if testfields == 1:
        #     print(username, password, confirm_password)
        db = 'db/db.csv'
        with open (db, 'a+') as file:
            fieldnames = ['User_name', 'Password', 'Confirm_password']
            store = csv.DictWriter(file, fieldnames=fieldnames, delimiter='\t')
            store.writeheader
            store.writerow({"User_name": self.username, "Password": self.password, "Confirm_password": self.confirm_password})
        # else:
        #     exit

    def loginUser(self, username, password):
            # test(username, password)
        db = 'db/db.csv'
        with open(db, 'r') as file:
            fieldnames = ['User_name', 'Password', 'Confirm_password']
            data = csv.DictReader(file, fieldnames=fieldnames)
            for user in data:
                # print(user['User_name'], user['Password'])
                # Stop here unable to compare fields name with row. not working i don't know why
                if user['User_name'] == username and user['Password'] == password:
                    print("Login")

class FiledErrors():
    emptyerror = "This field is required"
    passwordmismatch = "Enter same password as confirm password"
    lengtherror = " field should be more than 5 chars min"
        
    def __init__(self):
        pass

    def fieldcheck(self, field):
        if (field == ''):
            return FiledErrors.emptyerror
        elif (len(field) < 5):
            return FiledErrors.lengtherror
        else:
            return field
    
    def password_match(self, password, confirm_password):
        if (password != confirm_password):
            return FiledErrors.passwordmismatch
        else:
            return password, confirm_password

    

        


    # signup = User(username, password, confirm_password)
    # # test = signup.test(username = username, password = password, confirm_password = confirm_password)
    # # test = signup.test(username = username, password = password, confirm_password = confirm_password)
    # signup.registerUser()




# user = User
# user.registerUser('name')
# print(user.loginUser('name'))