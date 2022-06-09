def add(a, z):
    return a + z 
 
    # This function takes two numbers and subtracts them. 
def subtract(a, z):
    return a - z 
 
    # This function takes two numbers and multiplies them. 
def multiply(a, z):
    return a * z 
 
# This function takes two numbers and divides them. 
def divide(a, z):
    return a / z 
 
    # This function takes two numbers, divides them and return the remainder. 
def modulas(a, z):
    return a / z 

print("Select operation.") 
print("1.Addition") 
print("2.Subtraction") 
print("3.Multiplication") 
print("4.Division") 
print("5.Modulus")
 
while True: 
    
 # Take input from the user 
    choice = input("Enter choice(1/2/3/4/5): ") 
 
# Check to see if your choice is one of the five options 
    if choice in ('1', '2', '3', '4', '5'): 
        numb1 = float(input("Enter first number: ")) 
        numb2 = float(input("Enter second number: ")) 
 
        if choice == '1':
            print(numb1, "+", numb2, "=", add(numb1, numb2)) 
        elif choice == '2': 
            print(numb1, "-", numb2, "=", subtract(numb1, numb2)) 
        elif choice == '3':
            print(numb1, "*", numb2, "=", multiply(numb1, numb2)) 
        elif choice == '4':
            print(numb1, "/", numb2, "=", divide(numb1, numb2))
        elif choice == '5':
            print(numb1, "//", numb2, "=", modulas(numb1, numb2))
        break 
    else: 
        print("Invalid Input") 