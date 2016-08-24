# Illustration of the special methods that allow you to use the comparison operators and mathematical operators on objects

# Table 6-1. Magic methods for comparison
# __eq__( self, other ) self == other
# __ne__( self, other ) self != other
# __lt__( self, other ) self < other
# __gt__( self, other ) self > other
# __le__( self, other ) self <= other
# __ge__( self, other ) self >= other

# Table 6-2. Magic methods for math
# __add__( self, other ) self + other
# __sub__( self, other ) self - other
# __mul__( self, other ) self * other
# __floordiv__( self, other ) self // other
# __truediv__( self, other ) self / other
# __mod__( self, other ) self % other
# __pow__( self, other ) self ** other

class Word():
    def __init__(self, word):
        self.text = word

    def __eq__(self, other):
        return self.text.lower() == other.text.lower()

    def __add__(self, other):
        return len(self.text) + len(other.text)

    def __str__(self):
        return "WORD: " + self.text


abra = Word("aBra")
dabra = Word("abRA")

print(abra == dabra)
print(abra + dabra)

print(abra)