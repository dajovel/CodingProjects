 #Methods and Objects
#Built in objects in Python have a Variety of Methods you can use.
print("Methods and Objects\n")
mylist = [1,2,3]
print(mylist) #pre append
mylist.append(4) 
print(mylist) #post append
mylist.pop()
print(mylist) #popped the last thing on the list "4"

#help (mylist.insert)
#this will print the help doc for .insert
print('Using  the def Keyword')
#Creating a function in python requres a specific syntax including the 'def' keyword correct indentation and proper structure.
def name_of_function(name):
    '''
    Hovering over name of function will show this information 
    This is how this function works
    '''
# def add_function(num1,num2):
#     return num1+num2

def say_hello():
    print("hello")
    print("how")
    print("are")
    print("you?")

print(say_hello())
print(say_hello)
def  say_hello(name):
    print(f"hello {name}")
print(say_hello('Jose'))
#print(say_hello()) #TypeError: say_hello() missing 1 required positional argument: 'name'
#this error is provided because we missed one argument, 'namne'
def  say_hello(name='Default'):
    print(f"hello {name}")
print(say_hello())    #we added a default name so we will not get the argument from before.
def add_num(num1,num2):
    return num1+num2
#return will allow you to save it as a  variable
print(add_num(10,20)) #this will return 30 because we used the function add num
result = (add_num(10,21)) # with return we assigned it a variable.
print(result)

def print_result(a,b):
    print(a+b)

def return_result(a,b):
    return a+b 

print(print_result(10,20))
result = print_result(10,20)
print(type(result)) #<class 'NoneType'>

result =  return_result(10,23) 
#this does not print anything or return anything. But we can then use that result later, it was used in a print function in next line
print(result) #33
#if we would like to perform both at the same time, although not common
def myfunc(a,b):
    print(a+b)
    return a+b
myfunc(30,12) #returns 42 because we  asked it to print something as well as  return something we can now use the returned information somewhere else if needed.

def sum_numbers(num1,num2):
    return num1+num2
print(sum_numbers(10,20))
print(sum_numbers('10','20')) #this concatinated the information and output 1020. This would be incorrect

print("Function with logic\n")

print(2%2) #=0
print(3%2)#<--Using mod operator returns back the remainder
print(41%40) #return will be 1
#any number we can devide by 2 would be even so we can use this as a check point
print(20%2 == 0) #returns True
print(21%2 ==0) #returns False

def even_check(number):
    result = number % 2 == 0
    return result
print(even_check(21)) #returns False
print(even_check(20)) #returns True

def even_check_zero(number):
    return number % 2 == 0
print(even_check_zero(23)) #returns false This is the same as the function previously made

#returns true if any number is even inside of a list
def check_even_list(num_list):
    for number in num_list:
        if number % 2 ==0:
            return True
        else:
            pass
            #return False here would be incorrect, because it would not check everything in the list.
    #The False statement should be in line with the 'for' statement so it does not break out of the 'for' loop
    return False        
print(check_even_list([3,5,7])) #this returned nothing
print(check_even_list([2,4,5]))
print(check_even_list([2,1,1,1]))
print(check_even_list([3,1,5,7]))

def give_even_list(num_list):
    #Returns all of the even numbers in a list
    even_numbers = []
    for number in num_list:
        if number % 2 ==0:
            even_numbers.append(number)    
        else:
            pass
    return even_numbers

print(give_even_list([2,3,4,5,6,7,8,9,0,222]))

print('Tuple Unpacking with Functions\n')

stock_prices = [('APPL',200),('GOOG',400),('MSFT',100)]
for item in stock_prices:
    print(item)

for ticker,price in stock_prices:
    print(ticker)
for ticker,price in stock_prices:
    print(price+(0.1*price))

#employee of the month
work_hours = [('Abby',100),('Billy',400),('Cassie',800)]

def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''
    for employee,hours in work_hours:#tuple unpacking
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

        



    #Return
    return (employee_of_month,current_max)
print(employee_check(work_hours))
result = employee_check(work_hours) #created result as a <class 'tuple'>
print(result)
print(type(result))
name,hours = employee_check(work_hours) #here we broke down the name and hours by splitting the tuple
print(name)
print(hours)

#Here we added 'location' as a value, and there was not a third tuple present, This was the output error.
#name,hours,location = employee_check(work_hours) 
#ValueError: not enough values to unpack (expected 3, got 2) #this is telling us, we expected 3 and got back 2.
# if we were to assign it an item like this 
#item = employee_check(work_hours)
#print(item) = the tuple information. Then we can determine what/how we need to break it down.

print('Interactions Between Functions/n')

#typically a python script or notebook will contain several functions/interactions with each other, Taking results of one function and using them for the results of another.

example = [1,2,3,4,5,6,7]
from random import shuffle
shuffle(example)
print(example)

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example)
print(result)
result = shuffle_list(example) #once shuffled agin we can see the result is something else
print(result) 
print(result) #if we print result without running shuffle_list once again we get the same printed result

# #making a quick game
# # mylist = [' ','O',' '] #capital 'O' and two empty strings The user will  try to guess where the 'O' is
# # shuffle_list(mylist)

# def player_guess(): 
#     guess=''
#     while guess not in ['0','1','2']:
#         guess  = input('Pick a number: 0, 1 or 2:')
#     return int(guess)

# #player_guess()

# myindex = player_guess()
# #print(myindex)

# def check_guess(mylist,guess):
#     if mylist[guess] == 'O':
#         print('Correct!')
#     else:
#         print("Wrong Answer!")
#         print(mylist)

# #INITIAL LIST
# mylist = [' ','O',' ']
# #SHUFFLE LIST
# mixedup_list = shuffle_list(mylist)
# #USER GUESS
# guess = player_guess()
# #CHECK GUESS
# check_guess = (mixedup_list,guess)

#quiz section

print('*args and **kwargs in Python\n')

def myfunc(a,b):
    #returns 5% of sum of a and b
    return sum((a,b)) * 0.05

print(myfunc(40,60))
#returns 5.0
#a and b are positional arguments. 40=a 60=b because of the argumets position.
#if we want to work with more numbers
def myfunc(a,b,c=0,d=0,e=0):
    return sum((a,b,c,d,e)) * 0.05
print(myfunc(10,1,2,3,4,))
#output == 1.0 We have filled all space in the amount of addition we can do
#Performing this:
# print(myfunc(10,1,2,3,4,4))
#returns:
#TypeError: myfunc() takes from 2 to 5 positional arguments but 6 were given <<<Because we only placed 5 spots on the function (a,b,c,d,e)
def myfunc(*args):
    return sum (args) * 0.05
print(myfunc(1,2,3,4,5,6,7,8,9,10)) #this function will take in as many functions as i would like to put in.
def myfunc(*args):
    for item in args:
        print(item)
print(1,2,3,4,5,6,7,8)

def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here.')

myfunc(fruit='apple')
myfunc(fruit='apple',veggie='lettuce')
 
#we can see here that **kwargs is a dictionary, we can pass as many thing as we need to and create a larger one.
def myfunc(*args,**kwargs):

    print("I would like {} {}".format(args[0],kwargs['food']))
myfunc(10,20,30,fruit='Orange',food='eggs',animal='dog')
#this prints 10, and eggs. because 10 is in position 0 and food='eggs', If we changed this to fruit it would be orange and position 2 would be 30

def myfunc2(*args):
    #Returns all of the even numbers in a list
    even_numbers = []
    for number in args:
        if number % 2 ==0:
            even_numbers.append(number)    
        else:
            pass
    return even_numbers

print(myfunc2(2,3,4,5,6,7))
#Prints [2, 4, 6] All even numbers

# #st = 'Print every word in this sentence that has an even number of letters'
# for word in st.split():
#     if len(word)%2 == 0:
#         print(word+" <-- has an even length!")

# for num in mylist:
#     #check for even numbers
#     if num % 2 == 0: #this is the remainder if you /devide by 2. so we know its even. Visit % mod section modulo
#         print(num)# this will only print even numbers, output 2,4,6,8,10
#     else:
#         print(f'Odd Number: {num}')
# #         #f string added for {num} 
# def myfunc(**kwargs):
#     for letter in kwargs:
#         if letter % 2 ==0:
#             return letter.upper
#         else:
#             return letter.lower

# print(myfunc("dsaonfeuornceerrf"))

# Code along solutions:
# Lesser of 2 even
def lesser_of_two_evens(a,b):
    
    if a%2 ==0 and b%2 ==0:
        #BOTH NUMBERS ARE EVEN!
        if a < b:
            result = a
        else:
            result = b
    else:
        #ONE OR BOTH NUMBERS ARE ODD!
        if a > b:
            result = a
        else:
            result = b
    return result

print(lesser_of_two_evens(6,8))
print(lesser_of_two_evens(7,10))
print(lesser_of_two_evens(7,9))

def lesser_of_two_evens(a,b):
    
    if a%2 ==0 and b%2 ==0:
        #BOTH NUMBERS ARE EVEN!
        result = min(a,b)
    else:
        #ONE OR BOTH NUMBERS ARE ODD!
        result = max(a,b)
    
    return result
#this is the same result condenced
print(lesser_of_two_evens(6,8))
print(lesser_of_two_evens(7,10))
print(lesser_of_two_evens(7,9))

def lesser_of_two_evens(a,b):
    
    if a%2 ==0 and b%2 ==0:
        #BOTH NUMBERS ARE EVEN!
        return min(a,b)
    else:
        #ONE OR BOTH NUMBERS ARE ODD!
        return max(a,b)

#this is also okay
print('Animal Cracker\n')

def animal_cracker(text):
    wordlist = text.split()
    first = wordlist[0]
    second = wordlist[1]

    return first[0] == second[0]
    
print(animal_cracker('Levelheaded Llama'))
print(animal_cracker('Wonder Woman'))
print(animal_cracker('legion woman'))

def animal_cracker(text):
    wordlist = text.lower().split()

    return wordlist[0][0] == wordlist[1][0]

print(animal_cracker('Levelheaded Llama'))
print(animal_cracker('Wonder Woman'))
print(animal_cracker('legion woman'))
print(animal_cracker('legion Loman')) #this one returns true because we added the .lower and .split together. If Upper in previous def this would be fauls 'L'!='l'.
#this is similar to the above example. 

def makes_twenty(n1,n2):
    if n1 + n2 == 20:
        return True
    elif n1 == 20:
        return True
    elif n2 == 20:
        return True
    else:
        return False

print(makes_twenty(2,4))
print(makes_twenty(20,10))
print(makes_twenty(16,4))

def makes_twenty(n1,n2):
    return (n1,n2) == 20 or n1==20 or n2==20
#this is the same as the example before but all in 1 line. 
print(makes_twenty(2,4))
print(makes_twenty(20,10))
print(makes_twenty(16,4))

def old_macdonald(name):

    first_letter = name[0]
    inbetween = name[1:3]
    letter_four  = name[3]
    rest = name[4:]
    
    return first_letter.upper() + inbetween + letter_four.upper() + rest
print(old_macdonald('macdonald'))

def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]

    return first_half.capitalize() +  second_half.capitalize()
print(old_macdonald('macdonald'))
#first example is similar to second. Diffrent slicing

def master_yoda(text):
    wordlist = text.split()
    reversed_wordlist = wordlist[::-1]
    return ' '.join(reversed_wordlist)
print(master_yoda('I am home'))

mylist = ['a','b','c']
print('------'.join(mylist))
print(''.join(mylist))
#''.join() will join the words in the list. abc is the output. uses '_' to concatinate whatever we want in between
print('Almost there\n')
def almost_there(n):
    '''
    using abs. abs returns the absolute number of a value
    '''
    return (abs(100-n) <= 10) or (abs(200-n) <= 10)

print(almost_there(104))
print(almost_there(150))
print(almost_there(209)) 

print("\nFunctional Practice Probs Level2\n")

def has_33(nums):
    '''
    Given a list of ints. Return True if the Array contains a 3 next to a 3 somewhere
    '''
    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

print(has_33([1,3,3]))
print(has_33([1,3,1,3]))
print(has_33([3,1,3]))

def has_33(nums):
    '''
    Given a list of ints. Return True if the Array contains a 3 next to a 3 somewhere
    '''
    for i in range(0,len(nums)-1):
        if nums[i:i+2] == [3,3]:
            return True
    return False
#this is also okay and the same as the above function

#paper_doll
def paper_doll(text):
    result = ''
    for char in text:
        result += char*3
        #result += char + char + char <this would also work.
    return result

print(paper_doll("hello")) #prints hhheeellllllooo,

def blackjack(a,b,c):
    '''
    blackjack the game
    '''
    if sum([a,b,c]) <= 21: #can also use a+b+c
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <=31: #also could do sum([a,b,c] - 10 <=21)
        return sum([a,b,c])-10
    else:
        return 'BUST!'

print(blackjack(10,9,3))
print(blackjack(10,9,2))
print(blackjack(11,9,4))

def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

print(summer_69([1,3,5]))
print(summer_69([4,5,6,7,8,9]))

print("\nSpy Game\n")
def spy_game(nums):    

    code = [0,0,7,7]

    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

print(spy_game([1,2,4,0,0,7,3]))
#count primes

def count_primes(num):
    #check for 0 or 1 in input
    if num < 2:
        return 0
    #2 or greater

    #counter going upto input num
    primes = [2]
    x = 3
    #x is going up to every number upto input number.
    while x <= num:
        #check if X is prime
        for y in range(3,x,2):
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
print(count_primes(100))
print(count_primes(100))
print('\n Lambda expressions Map and Filter\n')
#map function-
#map(func, *iterables) --> map object
#Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted.
def square(num):
    return num**2

my_nums = [1,2,3,4,5]
map(square,my_nums)
for item in map(square,my_nums):
    print(item)
print(list(map(square,my_nums)))

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
         return mystring[0]

names = ['Andy','Eve','Sally']

print(list(map(splicer,names)))
#Prints ['EVEN', 'E', 'S']

#filter function-
print('Filter Function\n')
#filter filter(function or None, iterable) --> filter object
#Return an iterator yielding those items of iterable for which function(item) is true. If function is None, return the items that are true.

def check_even(num):
    return num%2 == 0

mynums =[1,2,3,4,5,6,]

print(list(filter(check_even,mynums)))
#[2, 4, 6]
for n in filter(check_even,mynums):
    print(n)
#jesus...

#lambda
def square(num):
    result = num **2
    return result
print(square(3)) #this returns 9 the square function takes a number and returns the square of the number

def square(num):
    return num **2
print(square(3)) #this is also the same as last function

def square(num): return num **2
print(square(3)) #samesies

lambda num: num **2 #lambda expression 
square = lambda num: num **2 #we can assign the expression to square also
print(square(3)) #did not need to completely make a function. Used lambda
#maybe not ready for this one but we can try
#Lambda With MAP function
print(list(map(lambda num:num**2,mynums))) #this took our expressions and made it a one liner. This is useful if this is not being used a lot or often. MAP function
#lambda with filter function
print(list(filter(lambda num:num%2 == 0,mynums)))
#[2, 4, 6] output

print(list(map(lambda name:name[0],names)))
#['A', 'E', 'S'] this grabbed the first letter of the names list 
print(list(map(lambda name:name[::-1],names)))
#['ydnA', 'evE', 'yllaS'] reversed it
#only use lambda expression when its going to be easy to read.