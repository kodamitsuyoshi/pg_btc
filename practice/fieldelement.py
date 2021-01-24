def FPrime(prime):
    def __func(num) :
        return FieldElement(num,prime)
    return __func


class FieldElement:
    
    def __init__(self,num,prime):
        if num>=prime or num <0:
            error = 'Num {} not in field range 0 to {}' .format(num,prime-1)
            raise ValueError(error)
            
        self.num = num
        self.prime=prime
    def __is_same_prime(self,other):
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in diffrent prime')
    def __repr__(self):
        return 'FR_{}({})'.format(self.prime , self.num)
    def __eq__(self,other):
        if other is None:
            return False
        return self.prime == other.prime  and self.num == other.num
    
    def __add__(self,other):
        self.__is_same_prime(other)
        num = (self.num +other.num)%self.prime
        return self.__class__(num,self.prime)
    
    def __sub__(self,other):
        self.__is_same_prime(other)
        num = (self.num - other.num)%self.prime
        return self.__class__(num,self.prime)
    
    def __mul__(self,other):
        self.__is_same_prime(other)
        num = (self.num * other.num)%self.prime
        return self.__class__(num,self.prime)
    def __pow__(self, exponent):
        n = exponent % (self.prime -1 )
        num = pow(self.num ,n ,self.prime)
        return self.__class__(num,self.prime)
    def __truediv__(self,other):
        return self * (other ** (self.prime - 2))

    def __rmul__(self, coefficient):
        num = (self.num * coefficient) % self.prime
        return self.__class__(num=num, prime=self.prime)

P = 2**256 - 2**32 - 977

class S256Field(FieldElement):
    def __init__(self,num,prime = None):
        super().__init__(num=num , prime=P)

    def __repr__(self):
        return '{:x}'.format(self.num).zfill(64)
