from es1 import SortedSet


#qui la consegna è un po' confusa mettiamo il caso di non voler contare il valore degli item ma solo il numero

class SortedSet2(SortedSet):
    def __init__(self, iterable):
        super().__init__(iterable)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return len(self._items) == len(other._items)
    def __gt__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return len(self) > len(other)
    
    def __lt__(self, other):
        return not (self > other or self == other)
    def __ge__(self, other):
        return not self < other
    def __le__(self, other):
        return not self > other
    def __ne__(self, other):
        return not self == other


if __name__ == '__main__':

    s1 = SortedSet2([3,1,2])
    s2 = SortedSet2([1,2,3,4])
    s3 = SortedSet2([2,3,4])
    s4 = SortedSet2([1,2,3])
    prnt = f"""
    s1: {s1}
    s2: {s2}
    s3: {s3}
    s4: {s4}

    True Statements:

    s1 < s2:\t {s1 < s2}
    s2 > s1:\t {s2 > s1}
    s1 <= s2:\t {s1 <= s2}
    s2 >= s1:\t {s2 >= s1}
    s4 == s1:\t {s4 == s1}
    s3 <= s2:\t {s3 <= s2}
    s1 == s3:\t {s1 == s3}

    False Statements:

    s1 < s3:\t {s1 < s3}
    s1 < s4:\t {s1 < s4}
    s2 < s1:\t {s2 < s1}
    s2 == s1:\t {s2 == s1}
    s1 != s3:\t {s1 != s3}
    
    """

    print(prnt)
