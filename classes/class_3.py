from class_a import Point

class Point3D(Point):
    ''' A point in 3-d space x, y, z'''
    __slots__ = ('__x', '__y', '__z')
    def __init__(self, x, y, z):
        super().__init__(x, y) # call the __init__ of the parent
        self.z = z
    @property
    def z(self):
        return self.__z
    @z.setter
    def z(self, z):
        if type(z) in (int, float):
            self.__z = z
        else:
            raise TypeError('Value of z must be numeric')
    def __str__(self):
        # self.super().__str__()
        return f'Point at {self.x}, {self.y}, {self.z}'

if __name__ == '__main__':
    p3 = Point3D(3,4,5)
    print(p3)