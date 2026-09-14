def add(p, q):
    return p + q

def substract(p, q):
    return p - q

def divide(p,q):
    return p / q

def multiply(p,q):
    return p * q

print("Please enter any operation")
print("a.Add")
print("b.substract")
print("c.divide")
print("d.multiply")


choice = input("please enter choice (a/b/c/d)")


number1 = int(input("Enter your first number"))
number2 = int(input("enter your second number"))

if choice == "a":
    print (number1,"+",number2,"=",add(number1,number2))
elif choice == "b":
    print (number1,"-",number2,"=",substract(number1,number2))
elif choice == "c":
    print (number1,"/",number2,"=",divide(number1,number2))
elif choice == "d":
    print (number1,"*",number2,"=",multiply(number1,number2))
else:
    print("This is invalid input")
