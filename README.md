# ATM Management System (Python Console App)

## Project Overview

This is a simple ATM Management System built using Python. It runs in the console and provides basic ATM functionalities such as:

- Account Login (with custom name and PIN)
- Check Balance
- Deposit Money
- Withdraw Money
- Logout

This project is suitable for beginners and demonstrates the use of:
- Input and Output
- Conditional Statements
- Loops
- Basic user authentication

## Features

### 1. Account Creation and Login
- Create an account with a name and PIN
- Login using the same credentials to access services

### 2. Check Balance
- Displays the current balance of the account

### 3. Deposit Money
- Accepts user input to deposit money
- Adds the amount to the account balance if the amount is valid

### 4. Withdraw Money
- Allows withdrawal if the requested amount is less than or equal to the balance
- Prevents withdrawal when funds are insufficient

### 5. Logout
- Ends the current session safely

## How to Run

1. Save the code in a file named `atm_system.py`
2. Open your terminal or command prompt
3. Run the program using the command:

```bash
python atm_system.py
```

## Sample Execution

```
Create Account Name : John123
Create Account PIN : 5678
==================================================
Enter Current Account Name : John123
Enter Current Account PIN : 5678
Account Credentials Are Authenticated!
Login Successful

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 Welcome To  ATM (Automated Teller Machine) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Check Balance
--------------------------------------------------
2. Deposit
--------------------------------------------------
3. Withdraw
--------------------------------------------------
4. Logout
--------------------------------------------------
```

## Notes

- This project does not store data permanently
- Account data and balance are lost after the program ends
- Can be enhanced with:
  - File or database storage
  - Multiple user support
  - GUI interface using tkinter or customtkinter

## License

This project is open for educational and personal use.
s
