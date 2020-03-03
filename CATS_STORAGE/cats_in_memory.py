#import uuid
###########
import csv
###########

class Cat:
    kind = 'feline'

    def __init__(self, uid, name, age, color):
        self.uid = uid
        self.name = name
        self.age = age
        self.color = color


class Cats:
    def __init__(self):
        self.cats = []


    def add_cat(self, uid, name, age, color):
        cat = Cat(uid, name, age, color)
        self.cats.append(cat)
        ############
        self._save()
        ############


    def check_cats(self):
        if len(self.cats) == 0:
            print('\nTHERE ARE NO CATS YET!\n')
            return False
        else:
            return True


    def show_cats(self, cat_obj):
            for cat in self.cats:
                self.print_cat(cat)


    def print_cat(self, cat):
        print('--------------------------------------------------------')
        print('ID: {}'.format(cat.uid))
        print('Name: {}'.format(cat.name))
        print("{}'s age: {}".format(cat.name, cat.age))
        print("{}'s color: {}".format(cat.name, cat.color))
        print('--------------------------------------------------------')


    def delete_cat(self, cat_uid):
        for i, cat in enumerate(self.cats):
            if str(cat.uid) == cat_uid:
                del self.cats[i]
                ############
                self._save()
                ############
                print('CAT DELETED!')
                break


    def search_cat(self, cat_uid):
        for cat in self.cats:
            if str(cat.uid) == cat_uid:
                print('This is the cat register:')
                self.print_cat(cat)
                break
        else:
            self._not_found()


    def _not_found(self):
        print('CAT NOT FOUND!')


    def act_data(self, cat_uid):
        for i, cat in enumerate(self.cats):
            if str(cat.uid) == cat_uid:
                self.change_data(i)
                break


    def change_data(self, index):
        cat_name = input('Enter the new name: ')
        cat_age = input("Enter the {}'s new age in years: ".format(cat_name))
        cat_color = input("Enter the new {}'s color: ".format(cat_name))

        self.cats[index].name = cat_name
        self.cats[index].age = cat_age
        self.cats[index].color = cat_color


    def _valid_id(self, user_id):
        for cat in self.cats:
            if str(cat.uid) == user_id:
                return True
        else:
            return False


    ###########################################################
    def _save(self):
        with open('cats.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('ID', 'name', 'age', 'color'))

            for cat in self.cats:
                writer.writerow((cat.uid, cat.name, cat.age, cat.color))

        #csv: coma separated values
    ##########################################################


def run():
    cats_list = Cats()


    ##########################################################
    with open('cats.csv', 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                continue

            cats_list.add_cat(row[0], row[1], row[2], row[3])
    ##########################################################


    deco = '-'*5
    print('\n{} C A T S   S T O R E D   I N   C S V   F I L E {}\n'.format(deco, deco))
    cats_list.show_cats(cats_list)

    while True:
        op = str(input('''
        Select one option:
        C) Create cat
        R) Read cats list
        U) Update cat
        D) Delete cat
        S) Search cat
        
        E) Exit
        
        Type your selection:
        ''')).lower()

        if op == 'c':
            cat_uid = uuid.uuid4()
            cat_name = input('Enter the cat name: ')
            cat_age = input("Enter the {}'s age in years: ".format(cat_name))
            cat_color = input("Enter the {}'s color: ".format(cat_name))

            cats_list.add_cat(uid = cat_uid, name = cat_name, age = cat_age, color = cat_color)


        elif op == 'r':
            if cats_list.check_cats():
                cats_list.show_cats(cats_list)


        if op == 'u':
            cat_uid = input('Enter the ID of the cat you wanna change: ')
            if cats_list._valid_id(cat_uid):
                cats_list.act_data(cat_uid)
            else:
                cats_list._not_found()


        elif op == 'd':
                cat_uid = input('Enter the ID of the cat you wanna delete: ')
                if  cats_list._valid_id(cat_uid):
                    cats_list.delete_cat(cat_uid)
                else:
                    cats_list._not_found()

        elif op == 's':
                cat_uid = input('Enter the ID of the cat: ')
                if cats_list._valid_id(cat_uid):
                    cats_list.search_cat(cat_uid)
                else:
                    cats_list._not_found()

        elif op == 'e':
            break



if __name__ == '__main__':
    run()

