# The factory pattern lets us manufacture required entities
class Animal(): # this could be abstract
    '''All the creatures will inherit from thsi class'''
    def makeNoise(self):
        pass

# here are some concrete creature classes (might be better if they wwre all in their own modules)
class Dog(Animal):
    def makeNoise(self):
        return 'woof'
class Cat(Animal):
    def makeNoise(self):
        return 'miaow'
class Bat(Animal):
    def makeNoise(self):
        return '____'
class Lion(Animal):
    def makeNoise(self):
        return 'roar'

# here is our creature factory - we can call this one class to get any of the other classes
class CreatureFactory():
    '''this is a single point of access for any of the creatures'''
    def makSound(self, obj): # obj will be the creature we need
        '''we evaluate which creature to manufacture'''
        if obj in ('Dog', 'Cat', 'Bat', 'Lion'):
            return eval(obj)().makeNoise()
        else:
            raise TypeError(f'No known creature {obj}')

if __name__ == '__main__':
    cf = CreatureFactory()
    c = input('which creature? ') # remember every user inout is a string
    noise = cf.makSound(c)
    print(f'The {c} says {noise}')
