print('Cool! Lets see if this script works. I am goint to try and upload it')

#Script for making a choice to multiply, divide, add or subtract


x = int(input("Please input a value for x: "))
y = int(input("Please input a value for y: "))



def multiplyValue(x,y):
    answer = x*y
    print("The product of x and y is: ", answer)

def divideValue(x,y):
    answer = x/y
    print("The quotient of x and y is: ", answer)

def addValue(x,y):
    answer = x+y
    print("The sum of x and y is: ", answer)

def subtractValue(x,y):
    answer = x-y
    print("The difference of x and y is: ", answer)
    
def exponentialValue(x,y):
    answer = x**y 
    print("The value of x raised to the y is: ", answer)

functionChoice = input("\nPlease select your function of choice: \nAdd(1) \nSubtract(2) \nMultiply(3) \nDivide(4) \nExponent(5) \nQuit(6)\n")

while functionChoice != '6':
    if functionChoice == "1":
     addValue(x,y)
     break
    elif functionChoice == "2":
     subtractValue(x,y)
     break
    elif functionChoice == "3":
        multiplyValue(x,y)
        break
    elif functionChoice == "4":
        divideValue(x,y)
        break
    elif functionChoice == "5":
        exponentialValue(x,y)
        break
    else:
        print("Please only input a value between 1 and 6")
        functionChoice = input("\nPlease select your function of choice: \nAdd(1) \nSubtract(2) \nMultiply(3) \nDivide(4) \nExponent(5) \nQuit(6)\n")


print("\nThis is the end of the script. Thank you")

print("\nThis is a test from July 21st to see if I can remember how to use Github")
