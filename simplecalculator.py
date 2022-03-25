def add(a, y):
    return a + y

def subtract(a, y):
    return a - y

def multiply(a, y):
    return a * y

def divide(a, y):
    return a / y

print("Select Operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.divepe")

while True:

    choice = input ("Enter Operation: ")

    if choice in ('1', '2', '3', '4'):
        n1 = float(input("Enter First number: "))
        n2 = float(input("Enter Second number: "))

        if choice == '1':
            print(n1, "+ ", n2, "=", add(n1, n2))

        elif choice == '2':
            print(n1,"-", n2, "=", subtract(n1, n2) )

        elif choice == '3':
            print(n1,"*", n2, "=", multiply(n1, n2) )

        elif choice == '4':
            print(n1,"/", n2, "=", divide(n1, n2) )

        nextcalculation = input("Want another calculation? (yes/no): ")
        if nextcalculation == "no":
            break

    else:
        print("invalid input")
        
