class Bank:
    #Define variable
    def __init__(self):
        self.accNumber=1000
        self.accHolder=None
        self.accType=None
        self.balance=0
    # Function for Account opening
    def openAccount(self):
        self.accNumber=self.accNumber+1
        self.accHolder=input('Enter customer name :')
        while True:
            self.accType = input('Enter acctype (saving/current):').lower()
            if self.accType=='saving' or self.accType=='current':
                break
            else:
                print('Please Enter Valid accType!')
        balance=float(input('Enter opening balance amount:'))
        print('Account opened successfully...! Data saved..!')
    # function for money deposit  
    def deposit(self):
        print('==== Deposit operation ====')
        amt = float(input('Enter deposited amount :'))
        self.balance = self.balance+amt
        print('Amount deposited successfully...!')
    # function for withdraw
    def withdraw(self):
        print('==== Withdraw operation ====')
        amt = float(input('Enter withraw amount :'))
        if amt>self.balance:
            print('Insufficient funds...!')
        else:
            self.balance = self.balance-amt
            print('Amount withdrawn successfully...')
    #function for view details
    def view(self):
        print(' --- Displaying Account Details ---')
        print('Account Number : ',self.accNumber)
        print('Account Holder : ',self.accHolder)
        print('Account Type   : ',self.accType)
        print('Total Balance  : ',self.balance)
        print('------------------------------------')
        print('*** Thank You ***')
        print('*** Have a nice day ***')
        
# object of Bank class
bank=Bank()
while True:
    print('***** Welcome to ABC Bank *****')
    print('\t 1. Open an Account')
    print('\t 2. Deposit')
    print('\t 3. Withraw')
    print('\t 4. View')
    print('\t 5. Exit')
    print('*******************************')
    choice= int(input('Enter your choice between(1-5):'))
    if choice==1:
        bank.openAccount()
    elif choice==2:
        bank.deposit()
    elif choice==3:
        bank.withdraw()
    elif choice==4:
        bank.view()
    elif choice==5:
        break
    else:
        print('Wrong choice entered.....!Try again...')
                
        
