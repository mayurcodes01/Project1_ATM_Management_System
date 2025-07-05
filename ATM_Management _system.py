#Project 1 : ATM Management System ( Required Functionalities : Check balance, Deposit Money & Withdraw)

AcName=input("Create Account Name : ") #we can create our own account and password
AcPin=input("Create Account PIN : ")
print('='*50)
AcBalance=0
                  
Name=input("Enter Current Account Name : ")  #input like user301,Mayur123 . 
Pin=input("Enter Current Account PIN : ")    #input like 1234 or anything.

if AcName==Name and AcPin==Pin:
    print("Account Credentials Are Authenticated!")
    print("Login Successful\n")
    while AcName==Name and AcPin==Pin:  #while True : is also applicable here
        
        print("~"*50)
        print(" Welcome To  ATM (Automated Teller Machine) ")
        print("~"*50)
        
        print("\n1. Check Balance")            
        print("-"*50)
        print("2. Deposit")
        print("-"*50)
        print("3. Withdraw")
        print("-"*50)
        print("4. Logout")
        print("-"*50)
        
        ch=input("\n Select a service to proceed from(1 to 4) :")
        
        if ch == '1':                  #Check Balance
            print(f"Balance : Rs. {AcBalance}/-\n")    
            
        elif ch == '2':                   #Deposit
            Amount=float(input("Enter Deposit Amount : Rs."))   
            if Amount>0:
                AcBalance+=Amount
                print(f"Deposited Rs.{Amount},\nCurrent Balance : Rs.{AcBalance}/-\n")
            else :
                print("Amount not valid.")   
                    
        elif ch == '3':                        # Withdraw
            Amount=float(input("Enter Withdrawl Amount : Rs."))    
            if 0<Amount<=AcBalance:
                AcBalance=AcBalance-Amount
                print(f"Withdraw Rs.{Amount},\nCurrent Balance : Rs.{AcBalance}/-\n")
            else :
                print("Insufficient account balance.\n")  
                           
        elif ch == '4':                     #Logout/exit
            print("\nLogged Out Securely,Hope you liked our Services, Visit Again!\n")
            break
        else :
            print("Unsupported Choice\nEnter correct one\n")
            
else :
    print("Login Failed!\nUnauthorized Access Denied")
    print("Account details are Wrong")
















