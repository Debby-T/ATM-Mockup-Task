import datetime
import time
print('Welcome to Zuri Bank')
print('====================')
print('Insert your card here')
print('====================')
username = ['Tosin','Mike','Love','Joe']
password = ['Tosin321','Mike321','Love321','Joe321']


def user_info ():
    name  = input('What is your name: \n') 
    if (name in username):
        print('Welcome! ', name)
        pswrd = input('Enter your password: \n')
        reg_pswrd = username.index(name)
        if (pswrd == password[reg_pswrd]):
            print('Access granted, Pls select the desired operation')
            withdrawal ()
        else:
            print('Password is incorrect, access denied.')
    
    else:
        print('Incorrect username, pls try again.')
       
    
def withdrawal ():
    
    print('1.Withdrawal')
    print('2.Cash Deposit')
    print('3.Complaint')
    selected_service = int(input('Pls selected an option: \n'))
    
    if selected_service == 1:
        print('How much would you like to withdraw?')
        print('Withdrawal is between #1000 - #50000')
        
        selectedOptionB = int(input('Please select an amount: \n'))
        if(selectedOptionB > 50000):
            print('Transaction limit exceeded, please try again')
        elif(selectedOptionB >= 1000):
            print('The transaction is processing...')
        else:
            print('Notes can only be printed in #1000 bills')
        
    elif (selected_service == 2):
        deposit()
        
    elif (selected_service == 3):
        complaint()
        
    else:
        print('You have selected an incorrect option, try again')
        
def deposit ():
    amt = int(input('Enter the amount to be deposited: \n'))
    if amt >= 50000:
        print('This amount cannot be deposited via the ATM, pls go to the banking hall.')
    elif amt < 500:
        print('Notes below #500 bills cannot be deposited')
    else: 
        print('Pls neatly place the cash into the receptacle')
        print('Your cash is being counted...')
        

def complaint():
    print('What issue would you like to report?')
    print('1.Deposit complaints')
    print('2.Withdrawal complaints')
    print('3.Card complaints')
    complnt = int(input('Pls, select an option: \n'))
    if (complnt == 1):
        print('Pls press the red button beside the ATM to talk to our customer care agent')
    elif(complnt == 2):
        print('Pls call this line 080321321321 or go to the banking hall')
    elif(complnt == 3):
        print('Pls go to the banking hall to resolve all issues related to bank card')
    else:
        print('Thank you for banking with us.')
    
    
user_info()
print('Thank you for banking with us' )
now =datetime.datetime.now()
date = now.strftime('%x')
print(now.strftime('%y/%m/%d %H:%M:%S'))
        

