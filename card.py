class Card: # inherits from 'object'
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit
    
    @property
    def rank(self):
        return self._rank
    
    @property
    def suit(self):
        return self._suit
    
    def __repr__(self): # when repr(OBJ) is used
        return f"Card('{self.rank}', '{self.suit}')"
    
    def __str__(self):
        return f"{self.rank}-{self.suit}"
    
if __name__ == "__main__":
    c1 = Card("A", "Clubs")
    c2 = Card("8", "Diamond")
    print(c1)  # str(c1) -> c1.__str__()
    print(c2)
    print(f"{c1 = }")  # repr(c1)  -> c1.__repr__()
    print(c1.rank, c1.suit)