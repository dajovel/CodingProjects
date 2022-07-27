#prep for tic tac toe and game
#things i need
#Visual Representation
#Grab user input.
#manipuilate a variable based on input
#return back result
# Most programs that uare interactive work on this very simple idea:
# Display something Visual to the user
# Let the user update through an interaction
# Update variables in the program
# Display updated visual
#Displaying information.

print([1,2,3])
print([4,5,6])
print([7,8,9])

#We can perform all of this with a custom function
def display(row1,row2,row3):
     print(row1)
     print(row2)
     print(row3)
      
example_row = [1,2,3]

display(example_row,example_row,example_row)
#instead of calling print 3 times we called display once and we can also change the variables in it
#1
row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']
display(row1,row2,row3)
row2[1] = 'X'
display(row1,row2,row3)
print("Accepting User Input\n")

#This is how we add an input, this will output a line for the user to input information. we can then use the information provided by the user
#input('Please enter a value:')
#result = input('Please enter a value: ')
#print(type(result))     #<class 'str'>

#result = input("enter value: ")
#result_int = int(result)
#print(type(result_int))
#float('3.14)
#we can also add the user input type while user inputs information
#position_index = int(input("Choose an index position: "))  
#print(type(position_index))
#row2[position_index]
#if we are converting something into an int type
print('Validating user input\n')

def user_choice():
    choice = 'Wrong'
    while choice.isdigit() == False:

         choice = input("Please enter a number (0-10): ")
    return int(choice)
     #we need to make sure the numbers are within 0 and 10
     #we also need to make sure the type in a data type
     #USE is.digit
some_value = '100'
print(some_value.isdigit())
#user_choice()
#in this version we will add an error message to the output
def user_choice():
    choice = 'Wrong'
    while choice.isdigit() == False:
         
         choice = input("Please enter a number (0-10): ")
          
         if choice.isdigit() == False:
             print('Sorry that is not a digit!')

    return int(choice)
#user_choice()


# on this run we will add logic to make sure there was an excepatable value input by the user.
def user_choice():
    #variables
    #initial
    choice = 'Wrong'
    acceptable_range = range(0,10)
    within_range = False

    #Two conditions to check
    #Digit or within_range ==  False
    while choice.isdigit() == False or within_range==False:
         
        choice = input("Please enter a number (0-10): ")
         #digit check 
        if choice.isdigit() == False:
            print('Sorry that is not a digit!')
         #range check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry you are out of acceptable range (0-10)")
                within_range = False
            
    return int(choice)
#user_choice()

print("Simple User Interactions Section\n")
# This program will:
# Display a list
# Have users choose an index position & an input value
# Replace Value at index position with users chosen input value

# #display the game
game_list = [0,1,2]

def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)
display_game(game_list)
# choose a position
def position_choice():

    choice = "wrong"
    while choice not in ['0','1','2']:
        choice = input("Pick a position (0,1,2): ")
        if choice not in ['0','1','2']:
            print("Sorry, Invalid choice!")
    return int(choice)
# choose position
def replacement_choice(game_list,position):

    user_placement = input("Type a string to place at position: ")

    game_list[position] = user_placement

    return game_list
     
# do you want to keep playing

def gameon_choice():
    choice = 'wrong'

    while choice not in ['Y','N']:
        choice = input("Keep playing? (Y or N)")
        if choice not in ['Y','N']:
            print("Sorry, i Dont understand, Please choose Y or N ")
    if choice == "Y":
        return True
    else:
        return False

game_on = True
game_list = [0,1,2]
while game_on:

    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list,position)

    display_game(game_list)

    game_on = gameon_choice()
