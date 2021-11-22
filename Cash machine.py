pin = "1324"

for i in range (3, 0, -1):
    attempt = input("Enter password ")
    if attempt == pin:
        break
    else:
        print("Incorrect - try again! ")

if i == 1:
    print("You have been denied ")
else:
    print("Password has beeen accepted ")

num1 = "£2400"

print("Your balance is £2400")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

print ("Would you like to deposite or withdraw ")
print ("1. Deposite")
print ("2. Withdraw")

while True:
    choice = input("Enter choice(1/2): ")

    if choice in ("1", "2"):
        num2 = float(input("Enter what you are looking to deposite or withdraw: "))

        if choice == "1":
            print(2400, "+", num2, "=" , add(2400, num2))

        elif choice == "2":
            print(2400, "-", num2, "=", subtract(2400, num2))
        if 2400 < num2:
            print("Insufficent funds") 
            


