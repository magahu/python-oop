import csv
import uuid
from cats_in_memory import Cat
from cats_in_memory import Cats

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

