#object Oriented Programming OOP

#class keyword is what we use in OOP
# class NameOfClass(): #camelcasing
#     def__init__(self,param1,param2):  <<--Method when inside of class ()
#     self.param1 = param1
#     self.param2 = param2

#     def some_method(self)
#     #perform some action
#     print(self.param1)
#hit Control + Space to see all Objects and Attributes on VS-Code

mylist = [1,2,3]
myset = set()

print(type(myset)) #<class 'set'>
print(type(mylist)) #<class 'list'>

class Sample(): #creating first class
    pass
#used a keyword classs

my_sample = Sample()
print(type(my_sample)) #<class '__main__.Sample'> What is main?
print("attributes")
class Dog():

    def __init__(self,breed):

        self.breed = breed

my_dog = Dog(breed='Lab')
print(type(my_dog)) #<class '__main__.Dog'>
print(my_dog.breed) #= Lab this is printed out because the type >>>>(my_dog = Dog(breed='Lab')<<<<



#Breaking this down a bit
#class Dog():

#     def __init__(self,breed): #__init__ can be thought of as the constructor for a class. It will be called automatically when you create an instace for a class.
                                #self represents the instance of the object itsself <<Always use self so every other programmer can know what is going on.                            
                                #breed - 3Xs breed, self.breed, breed  
                                #Attributes 
                                #we take in the argument
                                #assign it using self.attribute_name
#         self.breed = breed
#to make more sense will change somethings up
class Dog():

    def __init__(self,mybreed):

        self.breed = mybreed
my_dog =Dog(mybreed='Husky')
print(type(my_dog))
print(my_dog.breed)
#This prints out Husky by renaming to 'my_breed' the change to my_breed does not matter, 
# as if we changed self.myattribute = mybreed it is just easier to name them all the same thing insteam of renaming them all diffrent. Convention
#no real reason to have multiple names

print("Adding more attributes to the class\n")

class Dog():

    def __init__(self,breed,name,spots): #adding more attributes

        self.breed = breed #expect this to be a string
        self.name = name #expect this to be a string
        
        #expect this to boolean True/False
        self.spots = spots

#this also means we can make a class any other data type we would like.

my_dog = Dog(breed='Lab',name='Sammy',spots=False)
print(type(my_dog))
my_dog.name #now we can see the options for "my_dog.______" This is because 
print(my_dog.breed)
print(my_dog.spots)
print(my_dog.name)
#Here we can print out everything for my_dog. When we create classes later we should ensure we request the type that they
#should all be.
#Things we learned
#class
#__init__
#Attributes
# 
print("class object attributes\nObject Oriented Programming Part2")


class Dog():
    
    #CLASS OBJECT ATTRIBUTE
    #SAME FOR ANY INSTANCE OF A CLASS
    #ASSIGN AN ATTRIBUTE BEFORE INIT
    species = 'mammal'

    def __init__(self,breed,name,spots):

        self.breed = breed
        self.name = name

        #expect this to be boolean True/False
        self.spots = spots

my_dog = Dog(breed='Lab',name='Sam',spots=False)

print(my_dog.species) #this now populates because we have added the class object attribute and gave it a mammal name. Output of this is 'mammal'
#we did not need to assign it to self because it was 
# Species, even though we did not define it will always be availible to us
# Regardless of instance of my dog, it will always be a mammal#
#Methods are functions inside defined the body of the class and are used to perform operations that sometimes utilize the attirbutes of the object we created
#functions acting on the object
print("Methods Section\n")
class Dog():
    
    #CLASS OBJECT ATTRIBUTE
    #SAME FOR ANY INSTANCE OF A CLASS
    #ASSIGN AN ATTRIBUTE BEFORE INIT
    species = 'mammal'

    def __init__(self,breed,name):

        self.breed = breed
        self.name = name

        #expect this to be boolean True/False
        #removed Spots attribute on this one
    #OPERATIONS/ACTIONS -------> METHODS
    def bark(self):
        print("Woof!")

my_dog = Dog('Lab','Frankie')
print(my_dog.name) #Output Frankie
print(my_dog.bark) #<bound method Dog.bark of <__main__.Dog object at 0x104af7580>>
print(my_dog.bark()) 
my_dog.bark() #output Woof!


#adding a bit more to woof!
class Dog():
    
    #CLASS OBJECT ATTRIBUTE
    #SAME FOR ANY INSTANCE OF A CLASS
    #ASSIGN AN ATTRIBUTE BEFORE INIT
    species = 'mammal'

    def __init__(self,breed,name):

        self.breed = breed
        self.name = name

        #expect this to be boolean True/False
        #removed Spots attribute on this one
    #OPERATIONS/ACTIONS -------> METHODS
    def bark(self):
        print("Woof! My name is {}".format(self.name))

my_dog = Dog('Lab','Frankie')

print(my_dog.name) #Output Frankie
my_dog.bark() #since we have now added bark we input name for my_dog and since we called on .bark this output is the dogs name and the bark output
#my_dog.bark() = Woof! My name is Frankie

class Dog():
    
    #CLASS OBJECT ATTRIBUTE
    #SAME FOR ANY INSTANCE OF A CLASS
    #ASSIGN AN ATTRIBUTE BEFORE INIT
    species = 'mammal'

    def __init__(self,breed,name):

        self.breed = breed
        self.name = name

        #expect this to be boolean True/False
        #removed Spots attribute on this one
    #OPERATIONS/ACTIONS -------> METHODS
    def bark(self,number):
        print("Woof! My name is {} and the number is {}".format(self.name,number))

my_dog = Dog('Lab','Frankie')
print(my_dog.name) #Output Frankie
#my_dog.bark(10) #Now we have added the 'Number section for the print statement'
#TypeError: bark() missing 1 required positional argument: 'number' <--- This is the output if we do not add the positional argument
my_dog.bark(10) #the code is not referancing some particular instance of the number. We have manually input this
#Woof! My name is Frankie and the number is 10  <--- is the output
print("Creating Circle\n")

class Circle():
    
    #CLASS OBJECT ATTRIBUTE, SOMETHING THAT SHOULD BE TRUE ANY INSTANCE OF THE CLASS
    pi = 3.14
    def __init__(self,radius=1):

        self.radius = radius
        
        #METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle()
print(my_circle.pi) #3.14
print(my_circle.radius) #1 this was a default value radius=1):
print(my_circle.get_circumference())
#
your_circle = Circle(30)
print(your_circle.pi) #3.14 This value stays the same because it is pre defined
print(your_circle.radius) # Radius is now 30 
print(your_circle.get_circumference()) #188.4 is the circumference

print("ATTRIBUTE DOES NOT NEED TO BE DEFINED FROM A PARAMETER CALL\n")
class Circle():
    
    #CLASS OBJECT ATTRIBUTE, SOMETHING THAT SHOULD BE TRUE ANY INSTANCE OF THE CLASS
    pi = 3.14
    def __init__(self,radius=1):

        self.radius = radius
        #HERE WE HAVE ADDED THE AREA NOTE WE DID NOT ADD ANYTHING NEXT TO RADIUS
        self.area = radius*radius*Circle.pi #<---WE CAN ALSO RENAME THIS TO 'Circle.pi' from 'self.pi'BECAUSE WE KNOW IT WILL BE THE SAME REGARDLESS OF THE INSTANCE OF THE CLASS.
                                            #REASONING FOR USING 'Circle.pi' IS WE HAVE A LOT OF METHODS IN THE CLASS WE WILL KNOW THIS IS A CLASS OBJECT ATTRIBUTE AND WILL
                                            #KNOW WHERE WE CAN DEFINE THIS AT THE TOP OF THE CLASS OR EVEN KNOW IT WHAT IT IS. REFERENCING A CLASS OBJECT ATTRIBUTE. AT TOP:
                                            #OF CLASS
        
        #METHOD
    def get_circumference(self):
        return self.radius * Circle.pi * 2  

my_circle = Circle(30)
print(my_circle.area) #output is 2826.0 because we created an area "self.area = radius*radius*self.pi"