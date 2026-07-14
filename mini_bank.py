Project: Mini Bank System

Version: 1.0

Author: Rozhin

print("===== Mini Bank System =====")

balance = 1000

while True:
print("\n1. Show Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = input("Enter your choice: ")  

if choice == "1":  
    print("Balance:", balance)  

elif choice == "2":  
    amount = int(input("Enter deposit amount: "))  
    balance += amount  
    print("Deposit successful!")  

elif choice == "3":  
    amount = int(input("Enter withdraw amount: "))  

    if amount <= balance:  
        balance -= amount  
        print("Withdraw successful!")  
    else:  
        print("Not enough balance!")  

elif choice == "4":  
    print("Goodbye!")  
    break  

else:  
    print("Invalid choice!")
