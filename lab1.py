# Lab 1
import math
def task1():
    fName = input("Enter first name: ")
    lName = input("Enter last name: ")
    print(f"{lName} {fName}")

def task2():
    number=input("Enter a number: ")
    try:
        number=int(number)
        sum=int(number)+int(f"{number}{number}")+int(f"{number}{number}{number}")
        print(f"{number} + {number}{number} + {number}{number}{number} = {sum}")    
    except ValueError:
        print("Enter a valid number.")

def task3():
    str="""a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
"""
    print(str)
def task4():
    r=6
    volume = (4/3) * math.pi * r**3
    print(volume)

def task5():
    base = input("Enter base: ")
    height = input("Enter height: ")
    try:
        area = float(base)*float(height) *0.5
        print(f"The area is {area}")
    except ValueError:
        print("Enter valid base and height")

def task6():
    for i in range(1,10):
        for j in range(5-abs(5-i)):
            print("*",end="")
        print()

def task7():
    word = input("Enter a word: ").split(" ")[0] # Taking only the first word as input.
    word = word[::-1]
    print(f"Reversal: {word}")
def task8():
    for i in (num for num in range(7) if num not in {3,6}):
        print(i)

def task9():
    num1=0
    num2=1
    temp=1
    print(num1)
    print(num2)
    while(num2<50):
        temp=num2+num1
        num1=num2
        num2=temp
        if(num2<50):
            print(num2)
def task10():
    str = input("Enter a string (containing anything): ")
    letterCount=0
    numberCount=0
    for char in str:
        if char.isnumeric():
            numberCount+=1
        elif char.isalpha():
            letterCount+=1
    print(f"Number of numbers: {numberCount}\nNumber of letters: {letterCount}")
