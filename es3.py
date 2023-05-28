class MyComplex:
    def __init__(self, rea, ima = None):
        if isinstance(rea, complex):
            self._x = rea.real
            self._y = rea.imag
        else:
            self._x = rea
            self._y = ima
    @property
    def real(self):
        return self._x
    @property
    def imag(self):
        return self._y
    def conjugate(self):
        return MyComplex(self.real, -self.imag)

    def __str__(self):
            return f'({self.real:.3g}{self.imag:+.3g}j)'
        
    def __add__ (self, other):
        if isinstance(other, (int,float)):
            return MyComplex(self.real+other,self.imag)
        if isinstance(other, MyComplex):
            x = self.real + other.real
            y = self.imag + other.imag
        return MyComplex(x,y)
    def __radd__(self, other):
        if isinstance(other, MyComplex):
            return other + self
        elif isinstance(other, (int,float)):
            return MyComplex(self.real+other,self.imag)
    
    def __sub__(self, other):
        if isinstance(other, (int,float)):
            return MyComplex(self.real-other,self.imag)
        if isinstance(other, MyComplex):
            x = self.real - other.real
            y = self.imag - other.imag
        return MyComplex(x,y)
    def __rsub__(self, other):
        if isinstance(other, (int,float)):
            return MyComplex(other-self.real,-self.imag)
        if isinstance(other, MyComplex):
            return other - self

    def __mul__(self, other):
        if isinstance(other, (int,float)):
            return MyComplex(self.real*other,self.imag*other)
        if isinstance(other, MyComplex):
            x = self.real*other.real - self.imag*other.imag
            y = self.real*other.imag + self.imag*other.real
            return MyComplex(x,y)
    def __rmul__(self, other):
        if isinstance(other,(int,float)):   return MyComplex(self.real*other, self.imag*other)
        return MyComplex(other, self)

    def __truediv__(self, other):
        if isinstance(other, MyComplex):    return self * other.reciprocal()
        return self * (1/other)
    def __rtruediv__(self, other):
        if isinstance(other, (int,float)):  return other*self.reciprocal()
    
    def reciprocal(self):
        return MyComplex(self.real/(self.real**2+self.imag**2),-(self.imag/(self.real**2+self.imag**2)))

if __name__ == '__main__':
    print('\n\t---WELCOME---')
    c = complex(3.3,2)
    print('\nnormal boring complex:\t\t c = complex(3.3,2)\t\t',c)
    ee = MyComplex(3.3,-2)
    print('very fun and special Mycomplex:  MyCx = MyComplex(3.3,-2)\t',ee)
    print('MyCx.real: \t',ee.real)
    print('MyCx.imag: \t',ee.imag)
    print('MyCx.conj: \t',ee.conjugate())

    cx = MyComplex(c)
    print(f"""
    try to Mycomplex a boring complex...
    Cx = MyComplex(c)
    Cx:\t\t {cx}
    Cx.real:\t {cx.real}
    Cx.imag:\t {cx.imag}
    Cx.conj():\t {cx.conjugate()}
    """)

    a = MyComplex(2,4)
    b = MyComplex(3,1)
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
    2 - a = {2 - a}""")
    print(f"""\tmultiplication:
    a * 2 = {a * 2}
    2 * a = {2 * a}
    a * b = {a * b}
    b * a = {b * a}""")
    print(f"""\tdivision:
    a / b = {a / b}
    b / a = {b / a}
    a / 2 = {a / 2}
    2 / a = {2 / a}
    """)


