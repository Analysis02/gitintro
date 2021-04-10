import random

import time
t = time.localtime()
current_time = time.strftime('%H:%M:%S', t)


database = {}

def init():

    print('************  Welcome to Bank Som  ************')

    haveAccount = int(input("Do you have an account with us: 1 (Yes) 2 (No) \n"))

    if(haveAccount == 1):
        login()

    elif(haveAccount == 2):   
        register()

    else:
        print('Invalid Option Selected')
        init()


def register():

    print("********  Create an Account  ********")
    

    email = input('What is your email address? \n')
    first_name = input('What is your first name? \n')
    last_name = input('What is your last name? \n')
    password = input('Create a password \n')

    accountNumber = generateAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]

    print('Your account has been created')
    print('===== ===== ====== ====== =====')
    print('Your account number is: %d' % accountNumber)
    print('===== ===== ====== ====== =====')
    print('Make sure you keep it safe')
    print('===== ===== ====== ====== =====')

    login()

def login():
    
    print("********  Login  ********")
 
    accountNumberFromUser = int(input("Please Enter Your Account Number \n"))
    password = input("What is your password? \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)

        
        else:
            print('Invalid Account Number / Password Combination')
    login()


def bankOperation(user):

    print('Welcome %s ' % (user[0], ))
    print(current_time)

    print('What will you like to do?')
    print('(1) Deposit')
    print('(2) Withdraw')
    print('(3) Complaint')
    print('(4) Logout') 
    print('(5) Exit \n')
    selectedOption = int(input('Please Select an option \n'))
    if(selectedOption == 1):
        enterAmount = int(input('How much will you like to deposit? \n'))
        print('Current Balance = %s'  % enterAmount)
        depositOperation()

    elif(selectedOption == 2):
        enterAmount1 = int(input('How much will you like to withdraw? \n'))
        
        print('===========   ==========   ==========   ========')
        print('Please wait while your Transaction is processing')
        print('===========   ==========   ==========   ========')
        print('%d has been debited from your account' % enterAmount1)
        print('===========   ==========   ==========   ========')
        withdrawOperation()
    
    elif(selectedOption == 3):
        complaint = (input('Please enter your complaint \n'))
        print('=======   =======   =======')
        print('Thank you for contacting us')
        print('=======   =======   =======')
        complain()

    elif(selectedOption == 4):
        logout() 

    elif(selectedOption == 5):
        exit()

    else:
        print('Invalid option selected')
        bankOperation(user)

def depositOperation():
    print('=======   =======   =======')
    print('Transaction Successful')
    print('=======   =======   =======')

    anotherTransaction = int(input('Will you like to perform another transaction? (1) Yes (2) No \n' ))
    if(anotherTransaction == 1):
        login()
    elif(anotherTransaction == 2):
        exit()
    else:
        print('Invalid Option Selected')

def withdrawOperation():
    print('=======   =======   =======')
    print('Please Take your cash')
    print('=======   =======   =======')

    anotherTransaction = int(input('Will you like to perform another transaction? (1) Yes (2) No \n' ))
    if(anotherTransaction == 1):
        login()
    elif(anotherTransaction == 2):
        exit()
    else:
        print('Invalid Option Selected')

def complain():
    print('=========   ===========   =========')
    print('Your complain will be resolved soon')
    print('=========   ===========   =========')
    anotherTransaction = int(input('Will you like to perform another transaction? (1) Yes (2) No \n' ))
    if(anotherTransaction == 1):
        login()
    elif(anotherTransaction == 2):
        exit()
    else:
        print('Invalid Option Selected')

def generateAccountNumber():
    return random.randrange(6000000000,6999999999)

def logout():
    print('Thank you for banking with us')

def anotherTransaction():
    anotherTransaction = int(input('Will you like to perform another transaction? (1) Yes (2) No'))
    if(anotherTransaction == 1):
        login()
    elif(anotherTransaction == 2):
        exit()
    else:
        print('Invalid Option Selected')


        login()

init()