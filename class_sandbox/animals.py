from functools import wraps
from living import Living


population = 0

def get_futter(vore):  # factory pattern (if-else->object)
    if vore == 'herbivore':
        return lambda: print('I eat plants')
    elif vore == 'carnivore':
        return lambda: print('I eat meat')
    else:
        return lambda: print('I eat shadows')

# def bear_dec(bear_obj):
#
    # @wraps(bear_obj)
    # def choose_bear(*args, bear_type=None):
        # class tempClass(bear_obj):
#
            # def __init__(self, *args):
                # super().__init__(*args)
                # self.subspecies = bear_type
#
        # if bear_type is None:
            # return bear_obj(*args)
        # else:
            # return tempClass(*args)
    # return choose_bear

def animal_dec(cls):
    @wraps(cls)
    def wrapper(*args, **kwargs):
        print('New Animal')
        return cls(*args, **kwargs)
    return wrapper

@animal_dec
class Bear(Living):

    def __init__(self, age):
        super().__init__(age)
        print('Bear.')
        self.eat = get_futter('carnivore')  # composition (strategy pattern)
        # composition is attribute = object.  In this case, these are
        # functions, but in python, functions=objects. :)

    def roar(self):
        print('rar.')

    def reaction(self):
        return self.roar()

    def poop(self):
        print('Stuck to my bum hair.')

    def eat(self):
        return self.eat


def observe_animal(animal):
    animal.poop()
    animal.eat()
    animal.reaction()

    print('Try accessing property')
    animal.age

    print('Try editing property')
    try:
        animal.age = 0
    except ValueError as err:
        print('Caught : {}={}'.format(type(err), err))
        pass
    animal.age = 10
    print('Happy Birthday(s)! -> %d' % animal.age)

if __name__ == "__main__":
    b = Bear(5)
    # c = Bear(6, bear_type='grizzly')
    c = Bear(6)

    observe_animal(b)

    # print(c.subspecies)
    print(type(c))
