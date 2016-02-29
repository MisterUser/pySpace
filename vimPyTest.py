# @TODO start project
# @TODO NerdTree
# @TODO SuperTab or Python Mode
import pudb; pudb.set_trace()  # XXX BREAKPOINT

def main():
        print("neat")
        x = 1
        for i in range(1, 100):
            print ('x={}'.format(x))
            x += 1

if __name__ == "__main__":
    print('Starting script...\n')
    main()
