#OOP Part 4

#SPECIAL METHODS ALLOW USTO USE BUILT IN OPERATIONS IN PYTHON WITH "len" "print" functions with own created user options

mylist = [1,2,3]

print(len(mylist))

#check length on own objects

class Sample():
    pass
#when attempting to perform the check on this, Output = #TypeError: object of type 'Sample' has no len()
mysample = Sample()
# len(mysample)
#TypeError: object of type 'Sample' has no len()
#print(mysample)
#<__main__.Sample object at 0x106df2550>
print(mylist)

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

b = Book('Python rocks', 'Jose', 200)

#print(b)
#when printing 'b' we get = <__main__.Book object at 0x102b39fa0>
#when calling the print function we are asking what is the string representation of 'b'.
#print(str(b))
#<__main__.Book object at 0x10961dfa0>

#Instead we can use special method related to string call __str__(self)

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    #here we will add the __str__(self) command
    def __str__(self):
        return f"{self.title} by {self.author}"
#now when using thie command 

b = Book('Python rocks', 'Jose', 200)

print(str(b))
#OUTPUT = Python rocks by Jose
#print(len(b))
#TypeError: object of type 'Book' has no len() 
#THIS SPECIAL METHOD CAN ALSO BE USED FOR "len"

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author 
        self.pages = pages

    #correcting for string
    def __str__(self):
        return f"{self.title} bye {self.author}"
    
    def __len__(self):
        return self.pages

    def __del__(self):
        print("!!!A Book object has been deleted!!!")

cee = Book('Python rocks', 'Jose', 200)

print(str(cee))
print(len(cee))
print(str(cee))
del cee             #we deleted the book here #!!!A Book object has been deleted!!! was printed out 
# print(str(cee))     #NameError: name 'cee' is not defined when we try to call to print 'cee'