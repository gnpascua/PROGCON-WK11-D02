File Name: wk11d02ex01_compute_average.py 
Short Description: A beginner-friendly average calculator that calculates the average of user-inputted numbers using functions, 
loops, conditional statements, and input validation.  
Author: Pascua, Gaea Nikolaev B. 
Date: 2026-09-27 
 
def toFixed(value, digits): 
    return "%.*f" % (digits, value) 
 
def computeAverage(arr, count): 
    accum = 0 
    sentence = "The average of " 
    for coun in range(0, count - 1 + 1, 1): 
        print("Input the value of the " + str(coun + 1) + ending(coun + 1) + " number.") 
        arr[coun] = float(input()) 
        accum = accum + arr[coun] 
        if count == 2: 
            if coun == 0: 
                sentence = sentence + str(arr[coun]) + " " 
            else: 
                sentence = sentence + "and " + str(arr[coun]) 
        else: 
            if coun == count - 1: 
                sentence = sentence + "and " + str(arr[coun]) + "" 
            else: 
                sentence = sentence + str(arr[coun]) + ", " 
    sentence = "Great job! " + sentence + " is " + toFixed(accum / count,2) + "." 
    print(sentence) 
 
def ending(number): 
    if number > 10 and number < 20 or number % 100 > 10 and number % 100 < 20: 
        end = "th" 
    else: 
        if number % 10 == 1: 
            end = "st" 
        else: 
            if number % 10 == 2: 
                end = "nd" 
            else: 
                if number % 10 == 3: 
                    end = "rd" 
                else: 
                    end = "th" 
     
    return end 
 
# Main 
print("Hello, dear user! I am Flowy, your friendly Mathematics teacher! Today, we'll calculate the average of the numbers you 
input. Oh before that, what's your name?") 
name = input() 
print("Wonderful name! Let's start! How many numbers do you need the program to average?") 
print("Just a reminder, " + name + "! The average will be rounded up to 2 decimal points.") 
number = int(input()) 
while number < 1: 
    print("Oh no, the number you inputted is invalid! Please type in a positive real number.") 
    number = int(input()) 
numbers = [0] * (number) 
 
computeAverage(numbers, number)
