class Card:

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
    
    def show(self):
        return self.suit + "-" + self.number
    
    def compare(self, other_card):
        numbers = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        if numbers.index(self.number) > numbers.index(other_card.number):
            return '>'
        elif numbers.index(self.number) < numbers.index(other_card.number):
            return '<'
        else:
            return '='


