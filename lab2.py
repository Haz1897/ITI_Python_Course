
# Lab 2
import math
import random
def task1(li):
    nums=[]
    for num in li:
        if num not in nums:
            nums.append(num)
    return nums

def task2(str1,str2):
    front1=str1[:math.ceil(len(str1)/2)]
    end1=str1[math.ceil(len(str1)/2):]

    front2=str2[:math.ceil(len(str2)/2)]
    end2=str2[math.ceil(len(str2)/2):]

    return f"{front1}{front2} {end1}{end2}"

def task3(nums):
    temp = set(nums)
    return len(nums) == len(temp)

def task4(nums):
    for i in range(len(nums)):
        swapped=False
        for j in range (0,len(nums)-i-1):
            if(nums[j]>nums[j+1]):
                nums[j],nums[j+1] = nums[j+1],nums[j]
                swapped=True
        if(not swapped):
            break
    return nums

def task5():
    attempts=10
    guessed=[]
    answer=-1
    notDone=True
    def generateNewAnswer():
        nonlocal answer
        answer = random.randrange(0,101)
    def reset(newGame):
        nonlocal attempts,guessed
        if(newGame):
            attempts=10
        guessed=[]
        generateNewAnswer()
    while(notDone):
        reset(True)
        while(attempts>0):
            validGuess=False
            guess = input(f"Guess a number between 0 and 100 ({attempts} atttempts left): ")
            try:
                guess = int(guess)
                if(guess==answer):
                    print(f"Congratulations! You guessed {answer} correctly!")
                    if(attempts-1>0):
                        validGuess=True
                        print(f"You still have {attempts-1} attempts, try to guess another number!")
                        reset(False)
                elif(guess in guessed):
                    print(f"{guess} was already guessed!")
                elif(guess>100):
                    print(f"{guess} is higher than 100. It will not count.")
                elif(guess<0):
                    print(f"{guess} is less than 0, it will not count.")
                else:
                    validGuess=True
                    print(f"{guess} is incorrect, try again! (Hint: The number is {"larger" if guess < answer else "smaller"} than {guess})")
                    guessed.append(guess)
                if(validGuess):
                    attempts-=1
            except ValueError:
                print("Please enter a valid number.")
        print(f"Game Over! The number was {answer}. Would you like to continue?")
            
        choice=""
        while choice not in ["y","Y","N","n"]:
            choice=input("(Y)es, (N)o: ")
            match choice:
                case "y":
                    break
                case "Y":
                    break
                case "n":
                    notDone=False
                    break
                case "N":
                    notDone=False
                    break
    print("Thank you for playing!")

# Hacker Rank question: https://www.hackerrank.com/challenges/diagonal-difference/problem
def task6(arr):
    diff=0
    for i in range(len(arr)):
        diff+= (arr[i][i] - arr[i][-i-1])
    return int(math.fabs(diff))
        

