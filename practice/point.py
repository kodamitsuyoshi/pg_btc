def daenPoint(a,b):
    def __func(x,y):
        return Point(x,y,a,b)
    return __func
def daenPointI(a,b):
    return Point(None,None,a,b)

from fieldelement import FieldElement ,S256Field
class Point :
    def __init__(self,x,y,a,b):
        self.a=a
        self.b=b
        self.x=x
        self.y=y
        if self.x is None and self.y is None:
            return 
        if self.y ** 2 != self.x**3+self.a*self.x+self.b:
            raise ValueError('({},{}) is not on the curve'.format(x,y))
    
 
    
    def __repr__(self):
        if type(self.x)  == FieldElement:
            return 'Point({},{})_{}_{}_FR({})'.format(self.x.num,self.y.num,self.a.num,self.b.num ,self.x.prime)
        return 'Point({},{})_{}_{}'.format(self.x,self.y,self.a,self.b)
    
    def __is_same_keisu(self,other):
        if self.a!=other.a or self.b !=other.b:
            raise TypeError('Points {} , {} are not on the same curve'.format(self,other))
            
            
    def __eq__(self,other):
        if self.a != other.a:
            return False
        if self.b != other.b:
            return False
        
        if self.x != other.x:
            return False
        if self.y != other.y:
            return False
        
        
        return True
    
    def __ne__(self,other):
        return self.__eq__(other) == False
        
    
    def __add__(self, other):
        self.__is_same_keisu(other)
        if self.x is None:
            return other
        if other.x is None:
            return self
        
        
        
        if self  == other:
            if self.y  == 0 * self.x:
                return self.__class__(None,None,self.a,self.b)
            return self.__add_same_point()
        if self.x == other.x and (self.y!=other.y):
            return self.__class__(None,None,self.a,self.b)
        
        if self.x !=other.x:
            return self.__add_diff_x_case(other)

        

    def __add_diff_x_case(self, other):
        s  = (other.y - self.y)/(other.x - self.x)
        x3 = s*s -self.x -other.x
        y3 = s*(self.x-x3) - self.y
        return self.__class__(x3,y3,self.a,self.b)
    
    def __add_same_point(self):
        s  = (3*self.x*self.x+self.a)/(2*self.y)
        x3 = s*s -2* self.x
        y3 = s*(self.x-x3) - self.y
        return self.__class__(x3,y3,self.a,self.b)


    def __rmul__(self, coefficient):
    
        coef = coefficient
        current =self
        result = self.__class__(None,None,self.a,self.b)
        while coef:
            if coef & 1:
                result = result + current
            current =current + current
            coef >>=1

        return result

A=0
B=7
N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141

S256x=0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
S256y=0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
class S256Point(Point):

    def __init__(self, x, y, a=None, b=None):
        a,b = S256Field(A) ,S256Field(B)
        if type(x) == int:
            super().__init__(x=S256Field(x),y=S256Field(y),a=a,b=b)
        else:
            super().__init__(x=x,y=y,a=a,b=b)

    def __rmul__(self, coefficient):
        coef = coefficient % N
        return super().__rmul__(coef)
        
    def __repr__(self):
        if self.x is None:
            return 'S256Point(infinity)'
        else:
            return 'S256Point({}, {})'.format(self.x, self.y)

G = S256Point(S256x,S256y) 