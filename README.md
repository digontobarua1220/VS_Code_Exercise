This is a simple package that you can use to create, edit, and quiz yourself on flashcards.

When you import flash_lib.py, you can create an instance of a deck of flashcards by setting a variable (in this README, we will use "fc" to refer to this variable) equal to flash_lib.flashcard()
fc = flash_lib.flashcard()

You can create cards in your deck by using the create_deck() module
fc.create_deck()
You will be prompted to input the amount of cards you would like to create. Split words and definitions by a comma, and be careful with spaces and capitalization as modules in this package are sensitive to those variations. DO NOT put a space after the comma when adding cards to the deck.

You can add cards in your deck by using the add_cards_deck(n) module
Pass n as the number of cards you would like to add, for example 2:
fc.add_cards_deck(2)

You can delete cards from the deck by using the del_cards_deck(word) module and pass the word from the card you would like to delete from the deck
For example to delete the card with word "cells":
fc.del_cards_deck("cells")

You can quiz yourself using the quiz() module
fc.quiz()