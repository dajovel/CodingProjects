#udemycourse_3.py

print('nested statements and scope\n')
#name space has a scope *this variable is not defined.
x = 25
def printer():
    x = 50
    return x
print(x)
print(printer())
#legb rule
#local - names assigned in any way within a function (def or lambda), and not declared global in that function.
#lambda num:num *2

#enclosing function locals-names in the local scope of any and all enclosing functions(def or lambda), from inner to outer.
#global
name = 'this is a global string'

def greet():
    #enclosing
    name = 'sammy'
    def hello():
        print('hello '+name)
    hello()

print(greet())

# ####this one grabs name from global### because the enclosing one is commented out.
name = 'this is a global string'

def greet():
    #enclosing
#    name = 'sammy'

    def hello():
        print('hello '+name)
    hello()

print(greet())

####this one grabs name from local, because there is a 'name' in the function inside of the function.
name = 'this is a global string'
def greet():
    #enclosing
    name = 'sammy'
    def hello():
    #sammy
    #local
        name = 'im a local'    
        print('hello '+name)
    hello()
print(greet())
#on this one we grabbed "x" and placed it into the function
x = 50
def func(x):
    print(f"x is {x}")
print(func(x))

# #
x = 500
def func(x):
    print(f"x is {x}")
    #local reassignment
    x = 200
    print(f"i just locally change 'x' to {x}")
print(func(x))
print(x)
#although we reassigned x to be 200 in the function it was not changed outside of the function. this is why x can be 500 still
#the scope is only local to the function.
x = 50
def func():
    global x
    print(f"x is {x}")
    #local reassignment on a global variable
    x = 'new value'
    print(f"i just locally change 'x' to {x}")
print(func())
print(x) #since we reached out globally we changed x to 'new value' 
#output is not "new value"
x = 50
def func(x):
    #global x
    print(f"x is {x}")
    #local reassignment on a global variable
    x = 'new value'
    print(f"i just locally change 'x' to {x}")
    return x
print(x) #'x' will print 50 here
x = func(x) # we ran the function and it changed it to:
print(x) #now this is what 'x' is. x now = new value
#this is cleaner in the code and safer