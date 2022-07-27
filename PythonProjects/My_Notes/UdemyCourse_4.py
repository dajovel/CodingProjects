#UdemyCourse_4.py
#starting with the test
#Write a function that computes the volume of a sphere given its radius
rad = 2
def vol(rad):
    return (4/3)*(3.14)*(rad**3)
print(rad)
print(vol(rad))

#write a function that checs if a number is in a given range(Inclusive of high and low)
def ran_check(num,low,high):
    return num in range(low,high+1)
print(ran_check(5,2,7))
def ran_check(num,low,high):
    if num in range(low,high+1):
        print(f"{num} in range of high and low")
    else:
        print(f"{num} not in range")
#print(ran_check(5,2,7))
ran_check(5,2,7)
#check how many upper case
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'

def up_low(s):
    lowercase = 0
    uppercase = 0
    for char in s:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase =+ 1
        else:
            pass
    print(f"Origional String: {s}")
    print(f"Lowercase count: {lowercase}")
    print(f"Uppercase countL {uppercase}")
up_low(s)
#unique list
sample = [1,1,1,1,2,2,3,3,3,3,4,5]

def unique_list(lst):
    seen_numbers = []
    for number in lst:
        if number not in seen_numbers:  
            seen_numbers.append(number)
    return seen_numbers

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))
#returns [1, 2, 3, 4, 5]

def multiply(numbers):
    total = 1
    for num in numbers:
        total = total * num
    return total
print(multiply([1,2,3,-4,10]))
#returns -240

def palindrome(s):
    #remove spaces string
    s = s.replace(' ','')
     #check is string == reversed version of the string
    return s == s[::-1]

print(palindrome('nurses run'))
#this returns True

import string
def ispangram(str1,alphabet=string.ascii_lowercase):
    #create a set of the alphabet
    alphaset = set(alphabet)
    #remove any spaces from the input string
    str1 = str1.replace(' ','')
    #convert into all lowercase 
    str1 = str1.lower()
    #grab all unique letters from the string set()
    str1 = set(str1)
    #alphabet set == string set input
    return str1 == alphaset

print(ispangram("the quick brown fox jumps over the lazy dog"))