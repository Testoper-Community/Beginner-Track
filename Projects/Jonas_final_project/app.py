from user import User, FiledErrors

program_name = "Todo"
intro = "First time please enter '1' to Signup \nEnter '2' if already have an account\n"
print(intro)
signup_or_login = int(input("Login? Enetr 1: \n" + "Signup? Enter 2: \n\n" + "Action here....  "))

validate = FiledErrors()
def field_trial(lebalname):
    global prompt
    name = 0
    while name != 3:
        field_trial.prompt = input(lebalname)
        if lebalname == "Username: " or lebalname == "Password: " or lebalname == "Confirm Password: " :
            field_trial.valid = validate.fieldcheck(field_trial.prompt)
            if field_trial.valid == validate.emptyerror:
                return validate.emptyerror  
            elif field_trial.valid == validate.lengtherror:
                return validate.lengtherror 
            else:
                return field_trial.prompt

def password_match_trail(password, confirm_password):
    name = 0
    while name != 3:
        password_match_trail.valid = validate.password_match(password, confirm_password)
        if password_match_trail.valid == validate.passwordmismatch:
            name +=1
            return validate.passwordmismatch
        else:
            return password_match_trail.valid
        # if password == confirm_password:
        #     return True
        #     name = 3
        # elif password != confirm_password:
        #     print("fail")
        #     name +=1       
if signup_or_login != 1 and signup_or_login != 2:
    raise Exception("Enter 1 to Login or 2 to Signup as new user")
elif signup_or_login == 1: 
    prompt = field_trial("Username: ")
    if  prompt != field_trial.prompt:
        print(prompt)
    else:
        prompt_pass = field_trial("Password: ")
        if  prompt_pass != field_trial.prompt:
            print(prompt_pass)
        else:
            user = User()
            user.loginUser(prompt, prompt_pass)
            print("Login successful")


elif signup_or_login == 2: 
    prompt = field_trial("Username: ")
    if  prompt != field_trial.prompt:
        print(prompt)
    else:
        # global prompt_pass
        prompt_pass = field_trial("Password: ")
        if  prompt_pass != field_trial.prompt:
            print(prompt_pass)
        else:
            prompt_confirm = field_trial("Confirm Password: ")
            if prompt_confirm != field_trial.prompt:
                print(prompt_confirm)
            else:
                prompt_confirm2 = password_match_trail(prompt_pass, prompt_confirm)
                # print(prompt_confirm2)
                if prompt_confirm2 == validate.passwordmismatch:
                    print("Fail")
                else:
                    user = User(prompt, prompt_pass, prompt_confirm)
                    user.registerUser()
                    print("Name saved")