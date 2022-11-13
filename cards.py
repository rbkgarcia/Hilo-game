import random


class Cards:
    # Deck of cards that includes cards from 1 to 13
    # The value of the card will be used in the main function of the game.
    # The value is an int related to the number of the card drawn.

    def __init__(self):
        #Constructs instances of cards.
        #self (card) is an instance of a card. 
        self.value = random.randint(1, 13)

    def getValue(self):
        #Returns The value of the card.
        return self.value