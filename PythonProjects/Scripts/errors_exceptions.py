#errors  and exceptions 

try:
    result= 10 + "10"

except:
    print("Hey they arent adding correctly!!!")

else:
    print("addition went well")
    
try:

    f = open('testfile','w')
    f.write("write a test line")

#except:  #here   we can specify  the type of error we would like to except USAGE = except TypeError: <--we can add information before colon
#except TypeError:
except:
    print("Hey you have OS error")

finally:
    print("I always run")

def ask_for_int():
        
    while  True:
        try:
            result =  int(input("Please provide a number: "))
        except:
            print("Whoops! Thats not a number")
            continue
        else:
            print("Yes, Thank  you")
            break
        finally:
            print("END of try/except/finally")
            print("I will run at the end")
#ask_for_int()

#Test
try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("general error watch out")

#test#2
try:
    x =  5
    y =  0
    z =  x/y
except:
    print("did not work")
finally:
    print("all done")

def ask():
    
    while True:
        try:
            n  = int(input("enter a number:"))
        except:
            print("Please try again \n")
            continue
        else:
            break
    print("your number  squared is:  ")
    print(n**2)

ask()