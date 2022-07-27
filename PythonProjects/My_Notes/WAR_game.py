#OOP WAR

#CARD CLASS SHOULD BE ABLE TO UNDERSTAND
#SUIT,RANK,VALUE

#Global Variable
#Dictionary for our Cards

import random

values  = {
    'Two':      2,
    'Three':    3,
    'Four':     4,
    'Five':     5,
    'Six':      6,
    'Seven':    7,
    'Eight':    8,
    'Nine':     9,
    'Ten':     10,
    'Jack':    11,
    'Queen':   12,
    'King':    13,
    'Ace':     14,
}

#Tuples
ranks = (
    'Two',
    'Three',
    'Four',
    'Five',
    'Six',
    'Seven',
    'Eight',
    'Nine',
    'Ten',
    'Jack',
    'Queen',
    'King',
    'Ace',
)

suits  = (
    'Hearts',
    'Diamonds',
    'Spades',
    'Clubs'
)


class Card:
    
    def __init__(self,suit,rank):
        
        self.suit =     suit
        self.rank =     rank
        self.values =   values[rank]
    
    def __str__(self):
        
        return self.rank + " of " +  self.suit

two_hearts  = Card("Hearts","Two")

two_hearts

print(two_hearts)
print(two_hearts.suit)
print(two_hearts.rank)


three_of_clubs = Card("Clubs","Three")

print(three_of_clubs)
print(three_of_clubs.suit)
print(three_of_clubs.values)
print(three_of_clubs.rank)

print(two_hearts.values < three_of_clubs.values)
print(2<3) #this is  essentially what we are asking

#DECK CLASS
#We will see that  the deck class holds a  list of card objects
#This means that the deck class will return Card class object instances
#Not just normal Python  data types
print(suits)
print(ranks)

class  Deck:
    '''
    Instanciates a new  deck
    Creates all 52 Card Object
    Hold a  list of Card Objects
    Shuffle a deck through a method  called
    Random library shuffle() function
    Deal Cards from the deck function
    Pop  Method from Card list
    '''
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for  rank in  ranks:
                #create the card object
                
                created_card  =  Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        
        return self.all_cards.pop()

new_deck  = Deck()
bottom_card =  new_deck.all_cards[-1]
print(bottom_card)
new_deck.shuffle()
print(bottom_card)
print(new_deck.all_cards[-1])

my_card = new_deck.deal_one()
print(my_card)
print(len(new_deck.all_cards))
#print(new_deck.all_cards)

#PLAYER
class  Player():
    
    '''
    We will want a player to add a single card or multiple cards to their list, So we will also explore how to do this all in one method
    '''
    