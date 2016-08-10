from abc import ABCMeta, abstractmethod

class Living(metaclass=ABCMeta):

    def __init__(self, age):
        print('In Living __init__')
        self._age = age
        print('Age property: %d' % self.age)

    @property  # this allows age to be read but not written
    def age(self):
        return self._age

    @age.setter  # with this, the age can be set w/ validation
    def age(self, new_age):
        if new_age <= 0:
            raise ValueError('Age indicates unborn.')
        else:
            self._age = new_age

    @abstractmethod
    def poop(self):
        raise NotImplementedError('Living being has no poop mechanism.')

    @abstractmethod
    def eat(self):
        raise NotImplementedError('Living being has to eat.')

    @abstractmethod
    def reaction():
        raise NotImplementedError('So no reaction?')
