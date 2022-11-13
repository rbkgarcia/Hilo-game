from cards import Cards
class Director:
    """A Director who directs the game.
    The responsibility of the Director is to control the game.
    Attributes:
        currenCard (int): The current card value.
        keep_playing (boolean): Whether or not the game is being played.
        total_score (int): The total_score for the game.
    """

    def __init__(self):
        """Constructs a new Director.
        """
        self.currentCard = Cards()
        self.keep_playing = True
        self.total_score = 300

    def start_game(self):
        """Starts the game. All games start with the value of keep_playing equals to True
        Thanks to this the game always start and keep running the main game loop until one of the
        stop scenarios appears.
        """
        while self.keep_playing:
            self.next_card()
            self.show_cards()

    def next_card(self):
        """Ask the user if the next card will be higher or lower than the current card.

        """
        val = self.currentCard.value
        print("The card is: %d" %val)

        #This will keep looping until the Director enters either a valid input (h or l) 
        DirectorIn = ""
        while True:
            DirectorIn = input("Higher or lower? [h/l]: ")
            oldCard = self.currentCard
            newCard = Cards()
            if(DirectorIn == "h"):
                self.select_high(oldCard, newCard)
                break

            elif(DirectorIn == "l"):
                self.select_low(oldCard, newCard)
                break
            else:
                print("Invalid input")
                print()
            if DirectorIn == "h" or DirectorIn == "l":
                break

    def make_evaluation(self, guess, newCard):
        """Updates the Director's total_score.
        Args:
            self (Director): an instance of Director.
        """
        #updating total_score
        self.total_score += guess
        if (self.total_score <= 0):
            self.keep_playing = False
        #updating card
        self.currentCard.value = newCard

        
    def show_cards(self):
        """Displays the cards and the total_score. Asks to the Director the play continue.
        Args:
            self (Director): an instance of Director.
        """
        print(f"Your total_score is: {self.total_score}")
        print(f"The card was: {self.currentCard.value}")

        if(self.total_score <= 0):
            self.keep_playing = False
            print("You run out of points. Thanks for play!")
            return

        #The loops keeps working until the user enters either y or n
        v = ""
        while v != "n" or v != "y":
            v = input("Play again [y/n]: ")
            if(v == "n"):
                self.keep_playing = False
                break
            elif(v == "y"):
                print("")
                break
            else:
                print("Invalid input")


    def select_high(self, c1, c2):
        """If Director chooses High and gets it right we add 100 points
        But if they get it wrong they lose 75 points."""
        
        if c2.value > c1.value:
            self.make_evaluation(100, c2.value)
            
        elif c2.value < c1.value:
            self.make_evaluation(-75, c2.value)


    def select_low(self, c1, c2):
        """If Director chooses Low and gets it right we add 100 points
        But if they get it wrong they lose 75 points."""
        if c2.value < c1.value:
            self.make_evaluation(100, c2.value)
        elif c2.value > c1.value:
            self.make_evaluation(-75, c2.value)
        else:
            print("")
            return