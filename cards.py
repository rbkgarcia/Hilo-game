import random


class Cards:
    # Deck of cards that generate one card with an int value from 1 to 13
    # The card'swill be called in the Director class.

    def __init__(self):
        #Constructs instances of cards.
        #The Card is obtained randomly 
        self.value = random.randint(1, 13)

    def getValue(self):
        #Returns The value of the card.
        return self.value