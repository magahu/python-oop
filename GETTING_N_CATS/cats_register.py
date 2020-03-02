class Cat:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

class CatsList:

    def __init__(self):
        self.cats_list = []

    def add_cat(self, name, age, color):
        cat = Cat(name, age, color)
        self.cats_list.append(cat)

    def show_cats(self):
        for cat in self.cats_list:
            self.print_cat_data(cat)

    def print_cat_data(self, cat):
        print('................................')
        print('Cat name: {}'.format(cat.name))
        print("{}'s age: {}".format(cat.name, cat.age))
        print("{}'s color".format(cat.name, cat.color))
        print('................................')

def run():
    cats_list = CatsList()

    n_cats = int(input('How many cats do you wanna store?'
    '\nEnter an integer number: '))

    for i in range(n_cats):
        print('CAT N°{} DATA'.format(i+1))
        cat_name = str(input('Cat name: '))
        cat_age = str(input("{}'s age: ".format(cat_name)))
        cat_color = str(input("{}'s color: ".format(cat_name)))

        cats_list.add_cat( name = cat_name, age = cat_age, color = cat_color)

    print('\nThe cats registered are: ')
    cats_list.show_cats()


if __name__ == '__main__':
    run()
