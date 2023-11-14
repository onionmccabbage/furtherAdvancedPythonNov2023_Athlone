from _on import On
from _off import Off
from _sleep import Sleep
from _hybernate import Hybernate
from _laptop import Laptop

def main():
    '''exercise the stateful laptop'''
    c = Laptop()
    c.change(On) # fine
    c.change(Off) # fine
    c.change(On) # fine
    c.change(Sleep) # fine
    c.change(On) # fine
    c.change(Hybernate) # fine
    c.change(Sleep) # nope
    c.change(Off) # nope

if __name__ == '__main__':
    main()