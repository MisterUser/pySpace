# @TODO start project
# @TODO NerdTree
# @TODO SuperTab or Python Mode
import numpy as np

class ClassExample:
    def __init__(self, ar):
        self.ar = ar

    def op(self):
        print(self.ar)

    def set_ar(self, ar):
        self.ar = ar

    def yet_another(self):
        print('new function')

def main():
    import pudb; pudb.set_trace()  # XXX BREAKPOINT
    print("neat")

    x = 1
    for i in range(1, 100):
        print('x={}'.format(x))
        x += 1
    obj = ClassExample(np.arange(10).reshape(2, 5))
    print(obj.ar)

    print('\nEnd\n')

if __name__ == "__main__":
    print('Starting script...\n')
    main()
