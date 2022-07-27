#OOP Section 3

print("\nOOP Section 3 Inheritance/ polymorphism")

#we will use classes that have already been defined. We can reuse code that has previously been defined

class Animal():

    def __init__(self):
        print("ANIMAL CREATED!")

    def who_am_i_(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

myanimal = Animal()
myanimal.eat()
myanimal.who_am_i_()

class Dog(Animal): #<<-- Here dog inherits animal
    
    def __init__(self):
        Animal.__init__(self) #created an instance of the Animal class when creating an instance of the Dog class because inheiting Animal class
                            #this is where we are initializing the previously created animal class.
        print("Dog Created")
    #WE HERE CHANGED/OVERWRITE "who_am_i" IF WE NEED TO
    def who_am_i(self):
        print("I am a Dog")
    def bark(self):
        print("woof!")


mydog = Dog()   #OUTPUT=ANIMAL CREATED 
                        #Dog Created
                #REASON FOR THIS Since we combined both into "Dog" by inheriting Animal it then outputs all of the previous functions from Animal.
                #One of the functions being when we create something we print out "ANIMAL CREATED" and for Dog class "Dog Created"

mydog.who_am_i_()
mydog.eat() #we can now reuse methods that were written for another class.
mydog.bark

print("Polymorphism")

#DIFFRENT OBJECT CLASSES CAN B

class Dog():
    
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says woof!!"

class Cat():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says meow!!"

niko = Dog('niko')
felix = Cat('felix')
print(niko.speak())
print(felix.speak())

for pet in [niko,felix]:
    print(type(pet))
    print((pet.speak()))

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)

class Animal():

    def __init__(self,name):
        self.name = name

    #WE CREATED THIS TO LET SOMEONE KNOW WE SHOULD NOT USE THIS FUNCTION AND THE 'speak' METHOD SHOULD BE USED BY THE SUBCLASS
    def speak(self):
        raise NotImplementedError("Sublass must implement this abstract method")
    #WHEN CREATED, THE OUTPUT IS AS FOLLOWED

# myanimal = Animal('fred')
# myanimal.speak() #Sublass must implement this abstract method
# instead we should individually create this submethod based on class type.

class Dog(Animal):

    def speak(self):
        return self.name+ " says woof!"

class Cat(Animal):

    def speak(self):
        return self.name+ " says meow!"

fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak())
print(isis.speak())

#reasoning for having this in a real word situation (polymorphism) opening diffrent file types named 'Open'. Since there are diffrent types of files .doc .csv .py we should request the class decide what type of file should perform this function.