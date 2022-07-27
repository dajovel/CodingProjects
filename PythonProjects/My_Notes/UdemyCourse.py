print("First Section\n")
print(1+2) #simple addition
print(2*2) #simple multiplication
print(3/2) #simple devision
print(7%4) #percentage of
print(23%2) #Modulo or "Mod"
print(2**3) #example of 2 to the power of 3
print(2+10*10+3) #order of operation does Multiplication first then addition
print((2+10)*(10+3))
print(type(10)) #int
print(type(322.2))
print(type(0o10))
print(0o10) #Equalls  8 Type interger Ocatal, will look it up

#this will show how we can reassign the values of "a" with dynamic typing
a = 5
print(a)
a = 10
print(a)
print(a+a)

a  =  a + a
print(a)     #at this point "a" is an interger
print(type(a))
a = 30.1    #then we  change it to a "float" type
print(type(a))


my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print(my_taxes)
print(type(my_income))
print(type(tax_rate))

print('Hello')
print("hello")
print("Hello World")
print('This is also a long string')
#using correct "quotes" vs 'quotes' due to the phrase
print("I'm going on a run")


#adding a new line
print("hello \n world")
#notice space  ^ between new line when printing. Can be corrected like this:
print("hello \nworld")
#TAB over
print("Hello \tworld")

#len Function can tell you the lenght of a string, shown below
print(len("i am"))
print(type("hello world"))

#Strings and Indexing
mystring = "Hello World"
print(mystring)
print(len(mystring))
print(mystring[0]) #this will grab the "0" letter in the string
print(mystring[8]) #this will grba the "8" letter in the string, notice the space is also counted as a number.
print(mystring[-2])

#slicing
mystring = "abcdefghijk"
#slicing Legend
#abcdefghijk
#012345678910
print(mystring)
print(mystring[2:])
print(mystring[0:]) #remember we start at 0
print(mystring[:3]) #this one goes up to 3 position but does not include it.
print(mystring[3:5]) #output should be "de" since "abcdefghijk" "d" is in the first position and it grabbed UPTO "5" position
print(mystring[2:7:2]) 
#[start:stop:step]
#[start2:stop7:stepx2]

print(mystring[2:6:2])
print(mystring[0:6:2])
print("String Properties\nand Methods Section\n\n")

#Immutability
#example of it below

# name = "sam"
# name[0] = "P" When attempting to change the "S" to a "P" we cannot change  it because 'str' object does not support item assignment. we cannot grab a character 
#and attempt to assign it that way.

# Traceback (most recent call last):
#   File "/Users/david.jovel/PythonProjects/UdemyCourse.py", line 84, in <module>
#     name[0] = "P"
# TypeError: 'str' object does not support item assignment

print("Making Sam Pam")

name = "Sam"
print(name[1:]) #we are now using slicing to cut  out the "S"
last_letters = name[1:]
print("P" + last_letters)

x = "Hello World,"
print (x + " it is beutiful outside.")

letter = "z"
print(letter * 10) 

x = 'Hello World'
#hit Letter "x" add "." = "x." and a list appears. This is a list of all the attributes and methods availible for this string. 

print(x.upper()) # make sure we use () at the end of the command "x.upper()" is correct 
print(x.lower())
print(x.split()) #['Hello', 'World'] is the output, life a dictionary
print("Using Split")
x = "Hi this is a string" #['Hi', 'this', 'is', 'a', 'string']
print(x.split())

st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word [0]== 's':
        print(word)

st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word)%2 == 0:
        print(word+" <-- has an even length!")

print("Using .format()") #learn how to use .format() "{}" Section here.

print('this is a string {}'.format('INSERTED'))
print("the {} {} {}".format('fox','brown','quick'))
print("the {2} {1} {0}".format('fox','brown','quick')) #with indexed positions is correcting the positions of the words.
print("the {0} {0} {0}".format('fox','brown','quick')) #this one will return {0} {0} {0} fox fox fox Working off of index position
print("the {q} {b} {f}".format(f='fox',b= 'brown',q= 'quick')) #assigned f,b,q so i can position them later
print("the {f} {f} {f}".format(f='fox',q= 'quick',b= 'brown')) #this one prints out the fox fox fox because i have placed the f in the place holder 3 times.

print("Float Formatting follows")
result = 100/777
print(result)
print("the result equals {r}".format(r=result))
print("The result equals {r:1.3f}".format(r=result)) #this brings the the 3rd value and rounds to the nearest (.3f) "_ _ _ = 0.129"

name  = 'Jose'
print("His name is {}".format('jose'))
print("Halo, his name is {n}".format(n = 'Jose'))
print(f'Heello, his name is {name}')

print("Floating format with Mulitple Variables") #Injecting the variable into the string itsself
name = "Sam"
age = 3
print(f"{name} is {age} years old.")
print("{p} {r}!".format(p= 'Python',r= 'Rules' ))

print("Lists")

my_list = [1,2,3]
my_list = ['STRING',100,23.2]
print(len(my_list)) #how many elements or items are in this list 

mylist = ['one','two','three']
print(mylist[0])
print(mylist[1:])

anotherlist = ['four', 'five']
print(mylist + anotherlist)

newlist = mylist + anotherlist
print(newlist)
print(mylist)

newlist[0] = 'ONE ALL CAPS'

print(newlist)
#adding append added another number to list.
newlist.append('six')
print(newlist)
newlist.append('seven')
print(newlist)
#['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six', 'seven']
newlist.pop()
print(newlist)
#['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six'] Should be the output as it has "popped off" the  last thing on the list which was 
popped_item = newlist.pop()
print(popped_item)
newlist.pop(0)
print(newlist) # ['two', 'three', 'four', 'five'] is the output since we have popped the position 0.
#Pop removes items from the list on whateever index location you provide
#pop index location by default begins at location -1. Example: newlist.pop(-1) = newlist.pop()
newlist.pop(-2)
print(newlist) #should remove four and print ['two', 'three', 'five']

print('Sort and Reverse') #New Method Sort and reverse.
new_list = ['a','e','x','b','c']
num_list = [4,1,8,3]
#sorting the new list
new_list.sort() #this command sorts the list, then when we print we will see ['a', 'b', 'c', 'e', 'x']
print(new_list)
#['a', 'b', 'c', 'e', 'x'] output after sorted.

my_sorted_list = new_list.sort()
print(new_list.sort()) #prints none 
print(type(my_sorted_list)) #prints <class 'NoneType'>

None #geets used as a place holder, but should be the return value of a function method that has no value.

print(new_list)
my_sorted_list = new_list
print(my_sorted_list)

print(num_list)
num_list.sort()
print(num_list)
num_list.reverse() #this will reverse then numbers list.
print(num_list)

lst=[0,1,2]
lst.pop()
print(lst)

lst=['a','b','c']
print(lst[1:])

#dictionary section
print('Dictionary Section Begins\n')
my_dict = {'key1':'value1','key2':'value2'}
print(my_dict)
print(my_dict['key1']) #this will print 'value1' because this was what key 1 had.

prices_lookup = {'apple':2.99,'oranges':1.99,'milk':5.80}
print(prices_lookup['apple'])

#  #DICTIONARY AT TESLA!
# prices_lookup = {
#     'apple':2.99,
#     'oranges':1.99,
#     'milk':580
# }

# print(prices_lookup['milk']) #this will print 580 because the value was changed

d = {'k1':123,'k2':[0,1,2],'k3':{'inside Key':100}}
print(d['k2']) #value equals [0,1,2] 
print(d['k3']['inside Key']) #output =  100 because  it is the inside key

d = {'key1':['a','b','c']}
print(d)
mylist = d['key1']
print(mylist)
letters = mylist[2]
print(letters) #this prints the position [2] from mylist (remember we start at 0) "0,1,2".
print(letters.upper()) #requeted for the output to be uppercase with .upper()
#Calling it all at once
print(d['key1'][2].upper()) #in this method we performed all the last 6 steps at once.

print('Adding New Key Values\n')

d = {'k1':100,'k2':200}
print(d)
d['k3'] = 300
print(d)
d['k1'] = 'NEW VALUE' #reassigning/overiding a VALUE
print(d)
d = {'k1': 100, 'k2': 200, 'k3': 300}
#returning all keys
print(d.keys()) #dict_keys(['k1', 'k2', 'k3'])
#want to return all of the values
print(d.values()) #dict_values([100, 200, 300])
#everything together now
print(d.items()) #dict_items([('k1', 100), ('k2', 200), ('k3', 300)])

# d={'k1':[1,2,3]}
# print(d['k1'][1])

print('Tuples Section\n')

t = (1,2,3) #tuple uses '()'
mylist = [1,2,3] #list use '[]'

print(type(t)) #<class 'tuple'>
print(type(mylist)) #<class 'list'>
print(len(t))
print(t)
t = ('one',2)
print(t[0])
print(t[-1])
print('Count Method\n')
t = ('a','a','b')
print(t.count('a'))
print(t.count('b'))

mylist[0] = 'NEW' #reassigning 1st Element of the list
print(mylist) #['NEW', 2, 3]

# #tuple we cannot do this. Does not have the flexability of the list
# t[0] = 'NEW' Outputs
#     t[0] = 'NEW'
# TypeError: 'tuple' object does not support item assignment
print("Using sets\n")
myset = set()
print(myset)
print(type(myset)) #printed type, returned <class 'set'>
myset.add(1) #added to the 'myset'
print(myset)
myset.add(2)
print(myset)
myset.add(2) #the VALUE (2) has already been added previously. In a SET this cannot add a value that has already been added. 
print(myset) # output will still be {1, 2}. ONLY ACCEPTS UNIQUE VALUES!!

mylist =[1,1,1,1,1,1,2,2,2,2,3,3,3,3,3]
set(mylist)
print (set(mylist)) #this only outputs "{1, 2, 3}" because it will only accept unique values.
#sets also do not have an order.

set('Mississippi')
print(set('Mississippi')) # returns "{'s', 'p', 'i', 'M'}"
print("\n")
print("Booleans Section\n")

print(True)
# print(true) We need to make sure we capililize the word 'True' or will get this error message
#     print(true)
# NameError: name 'true' is not defined
#print(false) NameError: name 'false' is not defined Same with 'False'
print(False)
print(type(True))
print(type(False))
print(1 > 2) #This is a 'Bool' Also  False 1 is not greater than 2
print(1==1)
print(type(1==1))
b = None
print(type(b))


print("\nUsing FILES")
myfile = open('myfile.txt') #Created a file in the same directory as the script
#myfile = open('whoops_wrongfile.txt') #this file will result in a error because there is no file named this in the directory
#FileNotFoundError: [Errno 2] No such file or directory: 'whoops_wrongfile.txt' With incorrect file in directory or PATH
print("1")
print(myfile.read()) #this  reads the file created  in the directory.
print(myfile.read())
#this  only  printed out once, even though i  asked for it twice.
myfile.seek(0)
#print(myfile.seek(0))
#start over
print(myfile.read()) #<--First read the file
myfile.seek(0)
#print(myfile.seek(0)) #<-Then seek(0) to get back to the beginning of the file line.
print(myfile.read())  #<--Then request the file once again

contents = myfile.read()
print (contents + "Otherwords here")
myfile.seek(0)
print(myfile.readlines()) #one line in a string form ['Hello this is a txt file.\n', 'This is the second line\n', 'This is the third line \n', '#myfile = open(test.txt)\n', '#myfile = open(whoops_wrongfile.txt)']

#if you want to open a file from another location on the Computer simply pass the entire path to the file:
#myfile = open("Users/YourNameHere/Folder/myfile.txt")
#myfile = open("/Users/david.jovel/PythonProjects/")

#if file is open we will need to run myfile.close()
myfile.close()
print("Make sure to run myfile.close() after") # ensuring file is closed
print("Using 'with' and 'as'\n")

with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()
print(contents)
print(contents)
with open('myfile.txt',mode='r') as myfile:
    contents = myfile.read()
    print(contents)
# with open('myfile.txt',mode= 'w') as myfile:
#     contents = myfile.read()
# print(contents)  #error output io.UnsupportedOperation: not readable when changing to 'w'
#permissions only to read to a file THE 'w' WILL OVERWRITE FILES!!! BE CAREFUL WITH THIS.

# with open('myfile.txt',mode= 'a') as myfile:
#     contents = myfile.read()
# print(contents)
#this will .append to a file
print('Mode Types\n')
# mode= 'r'  is read only 
# mode= 'w' is write only will overwrite files or create new ones
# mode= 'a' is append only will add on to files 
# mode= 'r+' is read and write
# mode= 'w+' is writing and reading, will overwrite existing files or create a new one.

with open('my_new_file.txt',mode='r') as f: #once again read  a file
    print(f.read())
with open('my_new_file.txt',mode='a') as f: #write/append a  fourth line to filee
     print(f.write('\nFOUR ON FOURTH'))
with open('my_new_file.txt',mode='r') as f:  #read the file once again
    print(f.read())
    print(f.read())
with open('sad.txt',mode='w') as f: #write a new file
    print(f.write("I CREATED THIS FILE2")) #insert txt into the file.
with open('sad.txt',mode='r') as f: 
    print(f.read()) #read the file


# list4 = [5,3,4,6,1]
# list4.sort()
# list4_sorted = list4
# print(list4_sorted)

print('failed test portion')
# s ='hello'
# # Reverse the string using slicing
# s[::-1]

# list3 = [1,2,[3,4,'hello']]
#list3[2][2] = 'goodbye'
#go 0-1-2  then 0-1-2  rename goodbye

#build a list using [0,0,0]
#newlist = [0]*3
#print(newlist)

#sort a  list
#list4 = [5,3,4,6,1]
#sorted(list4) also works  and will actually return the list. along with list4.sort() which we will need to call the list once again


# d = {'k1':{'k2':'hello'}}
# # Grab 'hello'
# print(d['k1'])

# # Getting a little tricker
# d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#d['k1'][0]['nest_key'][1][0]
# #Grab hello

# This will be hard and annoying!
#d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
#d['k1'][2]['k2'][1]['tough'][2][0]

#Can you sort a Dictionary
#**Answer: No! Because normal dictionaries are *mappings* not a sequence. **

#list5 = [1,2,2,33,4,4,11,22,3,3,2]
# set(list5)
# print(set(list5))

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
# True or False?
print(l_one[2][0] >= l_two[2]['k1'])
#False
print('True or False Section\n')

print(2==2)
print(2 == 1)
print('hello' == 'bye')
print('bye' == 'Bye') #capitalization counts
print('bye' == 'bye')
print('2' == 2) #string 2 is not equal to  integer/number '2'
print(2.0 == 2) #for  floating points this will be true
print(3 != 3) #this will return False because 3 is  equal to 3
print(4 != 5) # True, 4  not equal to 5
print(2 > 1) # True, 2 is greater than 1
print(1 > 2) #False
print(1 < 2) #True
print(2 <  5) #True
print(2 >= 2) #True
print(2 <= 2) #True
print(4 <= 1) #False 

print("Chaining Comparison Operatiors")
print("We can use comparison operators to combine comparisons:\nand\nor\nnot\n")

print(1<2)
print(2<3)
print(1<2<3) #this is the  outcome of the last 2 

print(1<2)
print(2>3)
print(1<2>3) #also the outcome of the last 2 problems 
print("and function making sure both are true\n")
print(1<2 and 2>3) #using a logical operator returning False
print(1<2 and 2<3) #returning True
print("Using or function to ensure one or the other is true or false\n")
print(1==1 or 2==2)
print(100==1 or 2==2)
print(100==1 or 200==2) #returns false
print((100 == 1) or (200==2)) #returns false also, notice we are able to use () to enclose each formula.
print("using the not function\n")
print(not (1==1)) #this returns false because 1 does =  1
print(not 1==1)
print(1==1)
print(not 1==1)
#not is asking for the opposite boolian of what  was previously returned.
print(400>5000)
print(not  400>5000)
print(2<4)

a= 12
b = a-10
print(a > b)

print(2 < 3 > 10)
print(2 <= 3 >= 1)

print("Control Flow\n *if\n*elif\n*else\n")

#often oly want code to execute when a condition is met. Example: if my dog is hungry(Some condition), Then i will feed the dog(Some Action).
#control flow syntax makes use of colons and indentation(whitespace)
#This indentation system is crutial to Python and is what sets it apart from other languages.

#syntax of an if statement:
    # if some_condition:
    #     execute some code

print("syntax of if/else statement\n")
# #syntax of an if/else statement:
# if some_condition:
#     #execute some code
# elif some_other_condition:
#     #do something diffrent
# else
#     #do someting else

if True:
    print("Its true!")

if 3>2:
    print("It's True!")

hungry = True
if hungry:
    print("FEED ME!")
    print(type(hungry))

hungry = False
if  hungry:
    print("FEED ME!")
else:
    print("Im not hungry")

#example  1 with if and else
loc = 'Bank'
if loc == 'Auto Shop':
    print("Cars are cool!")
else:
    print("I do not know much.")
#example 2 with if elif and else:
loc = 'Bank'
if loc == 'Auto Shop':
    print("Cars are cool!")
elif loc == 'Bank':
    print("Money is cool.")
else:
    print("I do not know much.")
#example  3  showis multiple elif
loc = 'Store'
if loc == 'Auto Shop':
    print("Cars are cool!")
elif loc == 'Bank':
    print("Money is cool.")
elif loc == 'Store':
    print("Welcome to the store!")
else:
    print("I do not know much.")
#Example 4 Names
name = 'Sammy'
if name == 'Frankie':
    print("Hello Frankie")
elif name == 'Sammy':
    print("Hello Sammy")
else:
    print("What is your name?")
#Example:
name = 'Frankie'
if name == 'Frankie':
    print("Hello Frankie")
elif name == 'Sammy':
    print("Hello Sammy")
else:
    print("What is your name?")
#Example3:
name = 'Susie Q'
if name == 'Frankie':
    print("Hello Frankie")
elif name == 'Sammy':
    print("Hello Sammy")
else:
    print("What is your name?\n")

print("Discussing 'for loops'\n")
#Syntax of a for loop
my_iritable  = [1,2,3]
for item_name in my_iritable:
    print(item_name)
 #   print(type(item_name))

print("for loop Examples")

mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print(num)
#this output will print out 1-10

mylist =  [1,2,3,4,5,6,7,8,9,10] #self  test here. This prints 4 because  i am asking it to print 2**2
for  num  in mylist: #num is  
    print(2**2) 

mylist = [1,2,3,4,5,6,7,8,9,10]
for jelly in mylist:
    print(jelly) #the key word does not need to be 'num' it can be anything, for example 'jelly'
    #the veriable name can be anything we want

mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print("Hello") #this example i am printing "Hello" for every item in mylist, There are 10 items. Hello X 10 is the output

for num in mylist:
    #check for even numbers
    if num % 2 == 0: #this is the remainder if you /devide by 2. so we know its even. Visit % mod section modulo
        print(num)# this will only print even numbers, output 2,4,6,8,10
    else:
        print(f'Odd Number: {num}')
        #f string added for {num} 

list_sum = 0
for num in mylist:
    list_sum = list_sum + num 
    print(list_sum)#output below and the MATH!!!

# 1  0 + 1  = 1
# 3  1 + 2  = 3
# 6  3 + 3 = 6
# 10 4 + 6 = 10
# 15 5 + 10 = 15
# 21 6 + 15 = 21
# 28 7 + 21 = 28
# 36 8 + 28 = 36
# 45 9 + 36 = 45
# 55 10 + 45 =  55

print(list_sum) # equals 55. because we did not place it on the same indentation we got the total sum. unlike line before that counted everything  during...


mystring = 'Hello World'

for letter in mystring:
    print(letter)

for word in mystring:
    print(word)

#We can also just add what we we want and not make a string for it. Example below

for letter in 'What is this':
    print(letter)

for _ in "Hello World!": #we used an '_' to which is also exeptable This prints out 12 Cool! because of the amount of letters in 'Hello World!'
    print("Cool!")

tup = (1,2,3)
for item in tup:
    print(item)

print(type(tup)) #<class 'tuple'>

mylist = [(1,2),(3,4),(5,6),(7,8)] #made a list with Tuple pairs inside
print(len(mylist)) #4 because we have 4 tuple pairs
print(type(mylist)) #<class 'list'>

for item in mylist:
    print(item) #prints
# (1, 2)
# (3, 4)
# (5, 6)
# (7, 8)

for (a,b) in mylist:
    print(a)
    print(b)
#this prints:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
for (a,b) in mylist:
    print(a)
# 1
# 3
# 5
# 7
for a,b in mylist:
    print(b)
# 2
# 4
# 6
# 8

mylist = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in mylist:
    print(b)
# 2
# 5
# 8

print("for loops with Dictionary\n")

d = {'k1':1,'k2':2,'k3':3}
for item in d:
    print(item) #notice when printing this we only  get the "Key" Value back
# k1
# k2
# k3

for item in d.items():
    print(item) #if we would like  the value of the 'Key' back we need to use .items() function.
# ('k1', 1)
# ('k2', 2)
# ('k3', 3)
for key,value in d.items():
    print(value) #in this we assigned key as  the "key" and "value" as the Value in the key
# 1
# 2
# 3
for key,value in  d.items():
    print(key) #since we called the key (key,value) == (k1:1) "k1" we  printed

# k1
# k2
# k3

print("while Loops\n")

#while loops will continue to execute a block of code while some condition remains True.

#Syntax of a while loop:
#while some_boolean_condition:
    #do something
    #esle
    #so something diffrent

x = 0
while x < 5:
    print(f"The current Value of X is {x}")
    x = x + 1
# output added + 1 every time until = 5 output

# The current Value of X is 0
# The current Value of X is 1
# The current Value of X is 2
# The current Value of X is 3
# The current Value of X is 4
# while x < 5:
#     print(f"The current Value of X is {x}")
#     x = x + 1 <----Without this formula we would get an infinate while loop, breaking our python/ I closed the python terminal and fixed it.
x = 0
while x < 5:
    print(f"The current Value of x = {x}")
    x+=1

x = 0
while x < 5:
    print(f"The current Value of X is {x}")
    x = x + 1
else:
    print("X is not less than 5!")    

print("Break Continue and Pass\n")

#we can break continue and pass statements in our loops to add additional functionality for various cases. The three statements are defined by:

#break: Breaks out of the current closes enclosing loop
#Contine: Goes to the top of the closest enclosing loop
#pass: does nothing at all
print("Using pass\n")
x = [1,2,3]
for item in x:
    #comment Just adding comment to this will result in
    # IndentationError: expected an indented block
    #what we need to do is add a pass keyword which states, do nothing at all
    pass
    #If we comment out  the pass Keyword and attempt to run the script we still get an error. Because it is expecting something to happen after the colon.  
    #    print("end of my script")
# IndentationError: expected an indented block
print("end of my script")
#ofteen we will create a holder for our function but do not want to test it right away. The "pass" function will allow for this. This will also help avoid sintax errors. And we are safe because we know pass does not do anything.
print('\n')
print("Using Continue\n")
#Continue goes to the top of the closes enclosing loop
#using a for loop for example:
mystring = 'Sammy'
for letter in mystring:
    print(letter)
#this prints out each letter in individual line
#
for letter in mystring:
    if letter == 'a':
        continue
    print(letter)
#this prints out  
#S
#m
#m
#y
#
print('Using Break\n')

for letter in mystring:
    if letter == 'a':
        break
    print(letter)
#this prints "S"
# we can see the code broke out of the loop but did print the letter 'S'. This is because it broke out of the closest enclosing loop only allowing it to print letter 'S'
print("Using while\n")
x = 0
while x < 5:
    print(x)
    x += 1
# Output =
# 0
# 1
# 2
# 3
# 4

x = 0
while x  < 5:
    if x == 2:
        break
    print(x)
    x += 1
#this prints
# 0
# 1
#because we asked it ==2 break out of the loop
print("\n")
print("Useful Operators")
print("range()")
mylist = [1,2,3]
#Using range has an optional [start,stop,step size]
for num in range(10):
    print(num)
# prints:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
#all the way up to, but not including 10
for num in range(0,11,2):
    print(num)
list(range(0,11,2))
#prints range in 2 diffrent ways.
# print('This prints from starting range 3-10\n')
print('This prints from starting range 3-10\n')
for num in range(3,10):
    print(num)
#this is using our starting integer as 3 and going up to but not including 1-
print("Adding a step size (-,-,-)")
for num in range(0,10,2):
    print(num)
# output =
# 0
# 2
# 4
# 6
# 8    
#taking jumps in steps of 2 including '0' going to, but not including '10'

print('Useful operators\nGenerators\n')

#range function
mylist = [1,2,3]

for num in range(10): #range  also has a [start,stop,step]
   print(num)
#this prints out all the way up to but not including 10
#mylist = [1,2,3]
for num in range(3,10):
    print(num)
#this prints out numbers 3-10 excluding 10
for num in range(0,10,2):
    print(num)
#this  prints out 0-8 skipping 2 because of the step at the end (2)
print(range(0,10,2)) #printing this will only return itsself. because  it is a generator
print(list(range(0,10,2))) #this will return the list [0,2,4,6,8]
#Generator will generate a function without saving it to memory, better way to generate the numbers without having a giant list stored.

print('\nEnumerate Section\n')

index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1

index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1
#output abcde
#using Enumerate
word = 'abcde'
for item in enumerate(word):
    print(item)
#output = reasone is because we used enumerate this assigned a index to  the number. tuple
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')
for index,letter  in enumerate(word):
    print(index)
    print(letter)
    print('\n')
#this example uses tuple unpacking with 'index,letter'
print('Zip function section \n')
mylist1 = [1,2,3]
mylist2  = ['a','b','c']
zip(mylist1,mylist2)
print(type(zip())) #<class 'zip'>
print(zip()) #<zip object at 0x10183cb80>
for item in zip(mylist1,mylist2):
    print(item)
# this function packs both things togerther like a Zipper

mylist1 = [1,2,3,4,5,6]
mylist2  = ['a','b','c']
mylist3 = [100,200,300]
zip(mylist1,mylist2)
print(type(zip())) #<class 'zip'>
print(zip()) #<zip object at 0x10183cb80>
for item in zip(mylist1,mylist2,mylist3):
    print(item) 
# Output, This added all list together.
# (1, 'a', 100)
# (2, 'b', 200)
# (3, 'c', 300)
#notice 'mylist1 is longer than 2&3, This will still only return the length of the shortest list. Adding more elements will only be able to go as far as the list which is the shortest. This will also NOT produce an error.
print(list(zip(mylist1,mylist2)))
#[(1, 'a'), (2, 'b'), (3, 'c')]
print(list(zip(mylist1,mylist2,mylist3)))
#output =[(1, 'a', 100), (2, 'b', 200), (3, 'c', 300)]
#printing this will give us the output of mylist1 and my list2
for a,b,c in zip(mylist1,mylist2,mylist3):
    print(b)
#this returns a,b,c because we only asked for information from 'b' which in mylist2 = 'b' =  ['a','b','c']
print("\n 'in' operator  Section\n")
print('x' in [1,2,3])
#returns  False
print('x' in ['x','y','z'])
#returns True
print('a' in 'a world')
#returns True
#this is an easier way to check if something is in a list.
print(2 in [1,2,3])
#True, because it is present in the list
#'in' key also works on strings
print('a' in 'a world')
#Returns True
#'in' key in a Dictionary
print('mykey' in {'mykey':345})
#True
#Using 'in' key, real world
d  = {'mykey': 345}
print(345 in d.values())
#returns  true
print(345 in d.keys())
#returns false because 345 is only in values not a  key.
print('min max rand section\n')
# min function
mylist = [10,20,30,40,100]
print(min(mylist))
#this grabbed the lowest number of the list  and returned it. In this case '10'
print(max(mylist))
#this one grabbed the 'max' number from the list
 
#importing  functions from a library
from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
print(mylist)
#First we imported the shuffle command. we then used it with shuffle(mylist) then we printed the new list [8, 4, 7, 1, 10, 6, 3, 9, 5, 2] Since this is random it may not return the same order next time it is printed.
random_list = shuffle(mylist)
print(random_list)
#this returns  'none' as it is none type
print(type(random_list))
#Returns <class 'NoneType'>
print('Using randint\n')
from random import randint
print(randint(0,100))
print(randint(0,100))

mynum = randint(1,10)
print(mynum)
#We requested randint assign mynum a number, then we printed the number. This number also changes.

# print('Using Input command\n') #accepting User input
# input('Enter a number here:')
#  #input  then we add the TXT that  wants to show up, Then after input is present from user, we can decide to do something with it or not.50
# result_name =  input('what is yourname:')
# result_age = input('what is your age:')
# print('His name is ' + result_name)
# print('Age ' + result_age)
# #We can Grab the Results of  all of this information and create an output for it all
# #Input always  accepts anything that is passed into it as a 'string'
# print(type(result_age))
# #Even though i have received the number back '36'
# # The output is still class string<class 'str'>
# print(float(result_age))
# print(int(result_age))
# #making it all in 1 line
# result_test = int(input("what is your age?"))
# print(type(result_test)) #<class 'int'>
# print(result_test)
 
print('List Comprehension\n')
mystring = 'Hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)
#['H', 'e', 'l', 'l', 'o'] is the output. we have created a list based
# creating the same list in a diffrent way
mylist = [letter for letter in mystring]
#letter for letter in mystring, This does the same thing as the 'for' we  did previously, with less computation.
print(mylist)
#logic = a flattened out for loop, We are going to assume the only action being take in the 'for' loop is appending whatever element we  want to the same list (Element in this case being 'letter')
#Element in some Element for iterable object'
mylist = [x for x in 'word']
print(mylist)
#this example  split the list  ['w', 'o', 'r', 'd']
mylist = [num for num in range(0,11)]
print(mylist)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#this is the output. we created a num for numbers in range 0-11. this Excludes 11 and goes up to 10
mylist = [num**2 for num in range(0,11)]
print(mylist)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100] This is the output
#  we asked for num** squared  for num in range 0-11
mylist = [x for x in range(0,11) if x%2==0]
print(mylist)
#[0, 2, 4, 6, 8, 10] We checked if something is even and. and when mod 2 is equal to 0
mylist = [x**2 for x in range(0,11) if x%2==0]
print(mylist)
#[0, 4, 16, 36, 64, 100]  output is square of the even numbers
celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)
#[32.0, 50.0, 68.0, 94.1]
#for loop version is the same as above. 
fahrenheit = []
for temp in celcius:
    fahrenheit.append(((9/5)*temp + 32))
print(fahrenheit)
#instead of adding append we ((9/5)*temp + 32) grab the conversion/math part and add the "for" (for temp in celcius).
#[((9/5)*temp + 32) for temp in celcius]

#doing a if else statement in list comprehension
result = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(result)
#0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD', 10] = Output
#we asked it x square root of 2 equals 0(mod2)  or else print odd, this is done through the range between 0-11.

print('Nested loops\n')

mylist = []
for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)
print(mylist)
#[200, 400, 600, 400, 800, 1200, 600, 1200, 1800]
#what this is doing is Multuplying  2* everything in  y and moving along to 4  and 6
mylist = [x*y for x in [2,4,6] for y in[100,200,300]]
print(mylist)
#this function is the same as the one before but concensed #same output. Readability over easy


# for num in range(101):
#     if num %3  == 0:
#         print("fizz")
#     else:
#         print(num)
#Prints FIZZ every third

# for num in range(1,101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)
#Fizz Buzz

#st = 'Create a list of the first letters of every word in this string'
#[word[0] for word in st.split()]
#this just grabs the first letter in 'st'

# print('*args and **kwargs in Python\n')

# def myfunc(a,b):
#     #returns 5% of sum of a and b
#     return sum((a,b)) * 0.05

# print(myfunc(40,60))
# #returns 5.0
# #a and b are positional arguments. 40=a 60=b because of the argumets position.
# #if we want to work with more numbers
# def myfunc(a,b,c=0,d=0,e=0):
#     return sum((a,b,c,d,e)) * 0.05
# print(myfunc(10,1,2,3,4,))
# #output == 1.0 We have filled all space in the amount of addition we can do
# #Performing this:
# # print(myfunc(10,1,2,3,4,4))
# #returns:
# #TypeError: myfunc() takes from 2 to 5 positional arguments but 6 were given <<<Because we only placed 5 spots on the function (a,b,c,d,e)
# def myfunc(*args):
#     return sum (args) * 0.05
# print(myfunc(1,2,3,4,5,6,7,8,9,10)) #this function will take in as many functions as i would like to put in.
# def myfunc(*args):
#     for item in args:
#         print(item)
# print(1,2,3,4,5,6,7,8)

# def myfunc(**kwargs):
#     if 'fruit' in kwargs:
#         print('My fruit of choice is {}'.format(kwargs['fruit']))
#     else:
#         print('I did not find any fruit here.')

# myfunc(fruit='apple')
# myfunc(fruit='apple',veggie='lettuce')

# #we can see here that **kwargs is a dictionary, we can passi as many thing as we need to and create a larger one.