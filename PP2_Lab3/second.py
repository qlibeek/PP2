import math
     

def to_ounces(grams: int | float):
    return f"{grams} g. = {(28.3495231 * grams):.2f} oz."

print(to_ounces(50))
     

def to_celcius(fahrenheit: int | float):
    return f"{fahrenheit} F° = {((5 / 9) * (fahrenheit - 32)):.2f} C°"

print(to_celcius(50))
     

def solve(numheads, numlegs):
    for rabbits in range(numheads + 1): 
        chickens = numheads - rabbits
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
     

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def filt(list):
    for x in list:
        if is_prime(x):
            print(x)
     

def permutations(s, current=""):
    if len(s) == 0:
        print(current) 
        return
    for i in range(len(s)):
        ch = s[i]  
        remaining = s[:i] + s[i+1:]  
        permutations(remaining, current + ch)  
a = 'abcd'
permutations(a)
     

def reverse_words(sentence):
    reversed_sentence = ' '.join(sentence.split()[::-1])
    return reversed_sentence
     

def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
     


def spy_game(nums):
    for i in range(len(nums)-2):
        if nums[i]==0 and nums[i+1]==0 and nums[i+2]==7:
            return True
     

def volume(rad: int | float):
    return f"Vs (R = {rad}) = {(4/3 * 3.14 * rad**3):.2f} cubic units"

print(volume(10))
     

def new_list(_list: list[int]) -> list[int]:
    return list(dict.fromkeys(_list))

print(new_list([1, 1, 2, 3, 5, 3, 2, 4, 8]))
     

def is_palindrome(phr):
    for x in range(len(phr)//2):
        if phr[x]!=phr[len(phr)-x-1]:
            return False
    return True
     

def histogram(lst):
    for x in lst:
        print("*" * x)  
     


import random

def guessnum():
    rand_num = random.randint(1, 20)  
    name = input("Hello! What is your name? ")  
    a = int(input(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess: "))  
    count = 1  
    
    while a != rand_num:  
        if a < rand_num: 
            a = int(input("Your guess is too low.\nTake a guess: "))
        elif a > rand_num:  
            a = int(input("Your guess is too high.\nTake a guess: "))
        count += 1 
    
    print(f"Good job, {name}! You guessed my number in {count} guesses!") 

guessnum()  