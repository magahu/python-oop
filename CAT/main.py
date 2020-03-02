from cat import Cat

def main():
    cat_name = str(input('Enter the name of your cat: '))
    cat1 = Cat(cat_name)

    while True:
        op = input('''
        What should {}  do?

        a) sleep
        b) eat something tasty
        c) watch a tv show
        E) EXIT

        Choose an option: '''.format(cat1.name)).lower()

        if op == 'a' :
            cat1.sleep()
        elif op == 'b' :
            cat1.eat()
        elif op == 'c' :
            cat1.watch_tv()
        elif op == 'e' :
            break
        else:
            print("That option does'nt appear on the menu, try again")

if __name__ == '__main__':
    main()
