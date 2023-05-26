class SortedSet():
    def __init__(self,iterable):
        self._items=sorted(set(iterable))


    def __bool__(self):
        return bool(len(self))
    def __len__(self):
        return len(self._items)
    def __contains__(self, item):
        return item in self._items
    def __iter__(self):
        return iter(self._items)

    def pop(self, index=-1):
        self._items.pop(index)
    def remove(self,value):
        self._items.remove(value)
    def index(self,value):
        return self._items.index(value)
    def insert(self, value):       
        if value not in self._items:
            self._items.insert(self.IndexAfter(value),value)
    def append(self, value):
        return SortedSet.insert(self,value)

    def reverse(self):
        raise RuntimeError

    def IndexAfter(self, value):
        c = 0
        for k in self._items:
            if k > value:
                break
            c = c + 1
        return c
    
    def __getitem__(self, index):
        return self._items[index]
    def __str__(self):
        return str(self._items)

    def extend(self, other):
        for item in other:
            self.insert(item)



if __name__ == '__main__':


    l = SortedSet([1,4,2,5,1])
    
    l.insert(3)
    l.append(2)
    l.insert(0)
    l.append(3)
    l.insert(7)
    l.append(16)
 
    x = 3
    print(l,'contains 3?\t', x in l)
    x = 20
    print(l,'contains 20?\t', x in l)
    print('---iter---')
    for x in l:
        print(x)
    print('---end---')
    print('print(bool(l)):',bool(l))
    print('print(len(l)):',len(l))
          
          
          
    SortedSet.extend(l,[10,20])
    l.extend([100,-29])
    print('extend [10,20,100,-29]: ',l)
    try:
        l.reverse()
    except RuntimeError:
        print('tried to reverse: ',RuntimeError)
    print('dis a bonus, print(l[3]): ',l[3])