import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = []
        numbers = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        suits = ['S','H','C','D']
        for suit in suits:
            for number in numbers:
                self.cards.append(Card(number, suit))
    
    def validate(self):
        numbers = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        suits = ['S','H','C','D']
        for suit in suits:
            for number in numbers:
                count = 0
                for card in self.cards:
                    if card.number == number and card.suit == suit:
                        count += 1
                if count != 1:
                    return False
        return True
    
    def shuffle(self):
        random.shuffle(self.cards)
        if not self.validate():
            self.shuffle()

    
    def draw(self):
        if len(self.cards) == 0:
            return None
        else:
            return self.cards.pop(0)
