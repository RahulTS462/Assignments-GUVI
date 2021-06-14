import re

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'


def check():
    global mail, password
    invalid_mail_id_char = ['0','1','2','3','4','5','6','7','8','9','@','!','#','$','%','^','&','*','(',')']
    mail = input("E-mail: ")
    password = input("Password: ")
    if re.search(regex, mail) and mail[0] not in invalid_mail_id_char:
        mailchecker = True
    else:
        mailchecker = False

    while True:
        if len(password) > 16 or len(password) < 5:
            flag = -1
            break
        elif not re.search("[a-z]", password):
            flag = -1
            print("Password should contain at least one lowercase alphabet")
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            print("Password should contain at least one uppercase alphabet")
            break
        elif not re.search("[0-9]", password):
            flag = -1
            print("Password should contain at least one digit")
            break
        elif not re.search("[!@#$%^&*_()+=]", password):
            flag = -1
            print("Password should contain at least one specialcharacter")
            break
        elif re.search("\s", password):
            flag = -1
            break
        else:
            flag = 0
            break

    if not mailchecker:
        print("Invalid mail. Try again")
    if flag == -1:
        print("Invalid password. Try again")

    if mailchecker is True and flag == 0:
        return True
    else:
        return False


def login():
    print("--------LOGIN--------")
    uname = input("Username/Mail id: ")
    lpass = input("Password: ")
    try:
        f = open(uname, 'r')
    except:
        print("Invalid username! Please register")
        reg()
        return

    ch1 = 0
    stud_profile = f.read().split()
    if uname == stud_profile[2]:
        if lpass == stud_profile[3]:
            print('Login successful')
            print(stud_profile)
        else:
            print("Login failed")
            ch1 = int(input('\n1. Try again\n2. Forgot password: '))
            if ch1 == 1:
                login()
            elif ch1 == 2:
                print("Your password is: " + stud_profile[3])
    else:
        print("User doesn't exist! Please register")
        reg()


def reg():
    print("--------REGISTER--------")
    flag = 0
    name = input("Name: ")
    add = input("Address: ")
    #check()

    if check():
        f = open(mail, 'w')
        f.write('\n' + name + '\n')
        f.write(add + '\n')
        f.write(mail + '\n')
        f.write(password + '\n\n')
        f.close()
        print("Registered successfully!")

    else:
        if not check():
            print("Enter valid e-mail address")
        if flag == -1:
            print("Enter password in correct format")


print("Welcome")
print("1. Register\n2. Login")
ch = int(input("Enter your option: "))
if ch == 1:
    reg()
elif ch == 2:
    login()
else:
    print("Invalid choice")


