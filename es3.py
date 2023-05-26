class MyComplex:
    def __init__(self, rea, ima = None):
        if isinstance(rea, complex):
            self._x = rea.real
            self._y = rea.imag
        else:
            self._x = rea
            self._y = ima
        
    def real(self):
        return self._x
    def imag(self):
        return self._y
    def conjugate(self):
        return MyComplex(self._x, -self._y)

    def __str__(self):
        if self.imag()<0:
            return f'({self._x}{self._y}j)'
        else:
            return f'({self._x}+{self._y}j)'
        
    def __add__ (self, other):
        if isinstance(other, (int,float)):
            return MyComplex(self._x+other,self._y)
        if isinstance(other, MyComplex):
            x = self._x + other.real()
            y = self._y + other.imag()
        return MyComplex(x,y)
    def __radd__(self, other):
        if isinstance(other, MyComplex):
            return other + self
        elif isinstance(other, (int,float)):
            return MyComplex(self._x+other,self._y)
    
    def __sub__(self, other):
        if isinstance(other, (int,float)):
            return MyComplex(self._x-other,self._y)
        if isinstance(other, MyComplex):
            x = self._x - other.real()
            y = self._y - other.imag()
        return MyComplex(x,y)
    def __rsub__(self, other):
        if isinstance(other, (int,float)):
            return MyComplex(other-self._x,-self._y)
        if isinstance(other, MyComplex):
            return other - self

    def __mul__(self, other):
        if isinstance(other, (int,float)):
            return MyComplex(self._x*other,self._y)
        if isinstance(other, MyComplex):
            x = self.real()*other.real() - self.imag()*other.imag()
            y = self.real()*other.imag() + self.imag()*other.real()
            return MyComplex(x,y)
    def __rmul__(self, other):
        pass

    def __truediv__(self, other):
        pass
    def __rtruediv__(self, other):
        pass


if __name__ == '__main__':
    c = complex(3.3,2)
    print('\n\n\nnormal boring complex: \t\t',c)
    ee = MyComplex(3.3,-2)
    print('very fun and special Mycomplex:\t',ee)
    print('MyCx.real(): \t',ee.real())
    print('MyCx.imag(): \t',ee.imag())
    print('MyCx.conj(): \t',ee.conjugate())

    cx = MyComplex(c)
    print(f"""
    try to Mycomplex a boring complex...
    Cx = MyComplex(c)
    Cx:\t\t {cx}
    Cx.real():\t {cx.real()}
    Cx.imag():\t {cx.imag()}
    Cx.conj():\t {cx.conjugate()}

    """)

    a = MyComplex(5,2)
    b = MyComplex(7,1)
    c = a + b 
    print(f"""Operation With Complex numbers:
    \taddition:
    a = {a}
    b = {b}
    c = a+b = {c}
    a + b = {a+b}
    b + a = {b+a}
    a + 2 = {a+2}
    2 + a = {2+a}
    \tsubtraction:
    a = {a}
    b = {b}
    a - b = {a - b}
    b - a = {b - a}
    a - 2 = {a - 2}
    2 - a = {2 - a}
    \tmultiplication:
    a * 2 = {a * 2}
    a * b = {a * b}
    """)
   

