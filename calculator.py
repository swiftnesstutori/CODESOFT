# Python program for calculator
def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
print("Please select operation - \n "\
    "1.Add\n"\
    "2.Subtract\n"\
    "3.Multiply\n"\
    "4.Divide\n"\
    "5.Quit\n")
while True:
    select = int(input("select operation 1,2,3,4,5 : "))
    if select == 5:
        print("Calculator Exiting")
        break
    number_1 = float(input("Enter first number : "))
    number_2 = float(input("Enter second number : "))
    if select == 1:
        print(number_1,"+",number_2,"=",add(number_1,number_2))
    elif select == 2:
        print(number_1,"-",number_2,"=",subtract(number_1,number_2))
    elif select == 3:
        print(number_1,"*",number_2,"=",multiply(number_1,number_2))
    elif select == 4:
        if number_2 == 0:
            print("Cannot divide by zero")
        else:
            print(number_1,"/",number_2,"=",divide)