
from numbers import Complex

# Note: some methods are already implemented as template methods in
# numbers.Complex, specifically: __bool__, __sub__, __rsub__
# Therefore they do not need to be implemented explicitely in MyComplex, they
# will work automagically as soon as the other methods are implemented

# Note: the methods real() and imag() are defined as @properties in Complex
# We keep this approach and use the @property decorator for these methods.
# This means that when you use them on a MyComplex object z, you just write
# z.real or z.imag, without the ()
# Pretty much as you were referring to attributes rather than methods

# Note: ABCs Real, Rational, Integral in the numbers module (defining real,
# rational, and integer numbers, respectively) are all subclasses of Complex.
# Thus, operations like eq, add, etc. can be defined on any operands that are
# instances of Complex, and will work also with reals, rationals, or integers

# Note: for the power methods (__pow__, __rpow__), we only consider the cases
# where either the base or the exponent of the power are real (because a
# complex number power to another complex number is a bad beast...)
# Since the implementation is quite tedious, you may skip these methods and
# implement them with a simple "return NotImplemented" statement

class MyComplex(Complex):
    def __init__(self, x, y):       #x,y real/imaginary part, respectively
        super().__init__()
        self._x= x
        self._y =y

    def __str__(self):          return f'({self.real:.3g}{self.imag:+.3g}j)'
    def __complex__(self):              #conversion to complex: complex(z)
        return MyComplex(self.real,self.imag)
    def __eq__(self, other):            #equality check, with any Complex
        if isinstance(other, (MyComplex, complex)):
            if self.real == other.real and self.imag == other.imag:
                return True 
        return False  
    def __ne__(self, other):    return not self == other
    def __neg__(self):          return self * -1             #returns number negated: -z
    def __pos__(self):          return self             #returns number positive: +z
    def __abs__(self):          return (self.real**2+self.imag**2)**(1/2)             #returns modulus: |z|
    def __add__(self, other):      #arithm. operations, with any Complex
        if isinstance(other, (complex,MyComplex)):
            return MyComplex(self.real+other.real,self.imag+other.imag)
        elif isinstance(other, (int,float)):
            return MyComplex(self.real+other,self.imag)
        else:
            return NotImplemented
    def __radd__(self, other):
        #if isinstance(other, (int,float)):
        return self +other
        #elif isinstance(other, (complex,MyComplex)):
        #    return other + self
        #else:
         #   return NotImplemented     
    def __mul__(self, other):
        if isinstance(other, (int,float)):
            return MyComplex(self.real*other,self.imag*other)
        elif isinstance(other, (complex, MyComplex)):
            x = self.real*other.real - self.imag*other.imag
            y = self.real*other.imag + self.imag*other.real
            return MyComplex(x,y)
        else:
            return NotImplemented      
    def __rmul__(self,other): return self * other      
    def __truediv__(self, other): pass  
    def __rtruediv__(self, other): pass 
    def __pow__(self, other): pass      # with Real numbers (not any Complex)  
    def __rpow__(self, other): pass     # with Real numbers (not any Complex) 
    @property
    def real(self): return self._x
    @property
    def imag(self): return self._y
    def conjugate(self): return MyComplex(self.real,-self.imag)



if __name__ == '__main__':
    z = MyComplex(1,4)
    z2 = MyComplex(2,6)
    c = complex(1,4)
    z3 = MyComplex(1,4)
    print(f'z = z3 = {z}, z2 = {z2}, c = {c}')
    print(f"""Comparison Operators:
    \tFalse:
    z == z2 :\t{z == z2}
     z != c :\t{z != c}
    z != z3 :\t{z!= z3}
    \tTrue:
    z == c  :\t{z == c}
    z == z3 :\t{z == z3}
    z != z2 :\t{z != z2}
    """)
    print(f"""Neg and Pos:
    -z = {-z}
    +z = {+z}""")
    a = MyComplex(2,4)
    b = MyComplex(3,1)
    print(f"""Operation With Complex numbers:
    a = {a}, b = {b}
    \taddition:
    a + b = {a+b}
    b + a = {b+a}
    a + 2 = {a +2}
    2 + a = {2+a}""")
    print(f"""\tsubtraction:
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


