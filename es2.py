from es1 import SortedSet


#qui la consegna è un po' confusa mettiamo il caso di non voler contare il valore degli item ma solo il numero

class SortedSet2(SortedSet):
    def __init__(self, iterable):
        super().__init__(iterable)

    def __le__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        if len(self) <= len(other):
            for k in self:
                for j in other:
                    if k == j:
                        break
                else:
                    return False
            return True
        return False

    def __lt__(self, other):
        return self <= other and not self == other


    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        if len(self) == len(other):
            return self <= other
        return False
    
    def __gt__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self >= other and not self == other
    

    def __ge__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        if len(self)>=len(other):
            return other <= self
        return False
    
    def __ne__(self, other):
        return not self == other


if __name__ == '__main__':

    s1 = SortedSet2([3,1,2])
    s2 = SortedSet2([1,2,3,4])
    s3 = SortedSet2([2,3,4])
    s4 = SortedSet2([1,2,5])
    s5 = SortedSet2([1,2,3])
  
    print(f'\ns1 = {s1}\ts2 = {s2}\ns3 = {s3}\ts4 = {s4}\ns5 = {s5}\n')
    
    print('s1 <= s2:\t t',s1 <= s2)
    print('s1 < s2:\t t',s1 < s2)
    print('s2 > s1:\t t',s2 > s1)
    print('s1 >= s5:\t t', s1 >= s5)
    print('s1 != s4:\t t', s1 != s4)
    print('s2 >= s4:\t f', s2 >= s4)
    print('s1 != s5:\t f', s1 != s5)
    print('s2 > s4:\t f', s2 > s4)
    print('s1 == s2:\t f',s1 == s2)
    print('s2 == s1:\t f',s2 == s1)
    print('s1 < s5:\t f',s1 < s5)    
    print('s4 <= s2:\t f',s4 <= s2)