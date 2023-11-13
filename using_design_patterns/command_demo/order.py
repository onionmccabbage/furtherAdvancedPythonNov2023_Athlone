from abc import ABCMeta, abstractmethod

class Order(metaclass = ABCMeta):
    '''Architecture without any implementation'''
    @abstractmethod
    def execute(self):
        pass