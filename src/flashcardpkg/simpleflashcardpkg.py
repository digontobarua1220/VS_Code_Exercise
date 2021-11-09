import random

class flashcard():
    def __init__(self):
        self.flashcards = {}

    def create_deck(self):
        n = int(input("How many cards will this deck hold?: " ))
        deck = {}
        for i in range(n):
            card = input("Enter Words and Definiton separated by a comma: ").split(",")
            deck[card[0]] = card[1]
        #print(deck)
        self.flashcards = deck
        return self.flashcards
    
    def add_cards_deck(self, n):
        for i in range(n):
            card = int(input("Enter Words and Definiton separated by a comma: ").split(","))
            self.flashcards[card[0]] = card[1]
        return self.flashcards

    def del_cards_deck(self, word):
        self.flashcards.pop(word)
        return self.flashcards

    def quiz(self):
        score = 0
        for i, j in self.flashcards.items():
            if input(i) == j:
                score += 1
                print ("Correct!")
            else:
                print(f"Sorry, correct answer is {j}.")
                return score
