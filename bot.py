def do_calculation():
    print("Let's " + command + " some numbers")
    input1 = input("Number 1> ")
    input2 = input("Number 2> ")
    number1 = int(input1)
    number2 = int(input2)
    if command == "add":
        result = number1 + number2
        operator = " + "
        output = str(result)
        print(input1 + operator + input2 + " = " + output)
    elif command == "subtract":
        result = number1 - number2
        operator = " - "
        output = str(result)
        print(input1 + operator + input2 + " = " + output)
    elif command == "multiply":
        result = number1 * number2
        operator = " x "
        output = str(result)
        print(input1 + operator + input2 + " = " + output)
    elif command == "divide":
        result = number1 / number2
        operator = " / "
        output = str(result)
        print(input1 + operator + input2 + " = " + output)

#Main Part of Program
finished = False
print("Hi, I am Kendy, your personal bot.")
UserName = input("Please enter your name : ")
print("Hello, " + UserName + ", nice to meet you.")
print("Please enter one of the following choices: < add, subtract,multiply, divide, bye >")
command = input("How can I help? ")
if command == "add" or command == "subtract" or command == "multiply" or command == "divide":
    do_calculation()
elif command =="bye":
    print("Thank you for visiting me.")
    print("Goodbye.")
    finished = True
else:
    print("Sorry, I don't understand '" + command + "'.")


#These are my comments and whatever I had before I did the Def do_calculation()
#print("OK tested that and it works!")
#print("Please enter: < bye >")
#print("Please enter one of the following choices: < add, subtract,multiply, divide, bye >")
#command = input("How can I help? ")
#    if command == "add":
#        print("lets add some numbers")
#        input1 = input("Number 1> ")
#        input2 = input("Number 2> ")
#        number1 = int(input1)
#        number2 = int(input2)
#        result = number1 + number2
#        output = str(result)
#        print(input1 + " + " + input2 + " = " + output)
#    elif command == "subtract":
#        print("lets subtract some numbers")
#        input1 = input("Number 1> ")
#        input2 = input("Number 2> ")
#        number1 = int(input1)
#        number2 = int(input2)
#        result = number1 - number2
#        output = str(result)
#        print(input1 + " - " + input2 + " = " + output)