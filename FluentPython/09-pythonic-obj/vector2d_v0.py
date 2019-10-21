
import math
from array import array


class Vector2d:
    typecode = 'd'
    
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    
    def __str__(self):
        return str(tuple(self))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name, *self)
    
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def abs(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))



