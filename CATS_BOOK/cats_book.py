import uuid


class Cat:
    def __init__(self, uid, name, age, color):
        self.uid = uid
        self.name = name
        self.age = age
        self.color = color


class Book:
    def __init__(self):
        self.cats = []


    def get_field(self, field_name):
        field = None
        while not field:
            field = input('\nEnter cat {}: '.format(field_name))
        return field


    def add_cat(self):
        uid = uuid.uuid4()

        name = self.get_field('NAME')
        age = self.get_field('AGE')
        color = self.get_field('COLOR')

        cat = Cat(uid, name, age, color)

        self.cats.append(cat)


    def show_cats(self):
        if len(self.cats) == 0:
            print('*'*50)
            print('There are no cats registered yet')
            print('*'*50)
        else:
            for cat in self.cats:
                print('*'*50)
                print('Cat ID: {}'.format(cat.uid))
                print('Cat name: {}'.format(cat.name))
                print('Cat age: {}'.format(cat.age))
                print('Cat color: {}'.format(cat.color))
                print('*'*50)


    def update_cat(self, uid_to_update):
        for i, cat in enumerate(self.cats):
            try:
                if cat.uid == uuid.UUID(uid_to_update):
                    self.cats[i].name = self.get_field('NEW NAME')
                    self.cats[i].age = self.get_field('NEW AGE')
                    self.cats[i].color = self.get_field('NEW COLOR')
            except ValueError:
                #ValueError: badly formed hexadecimal UUID string:
                print('{} NOT FOUND!'.format(uid_to_update))

        #for i in range(len(self.cats)):
            #print('cat id: {}'.format(self.cats[i].uid))
            #if str(self.cats[i].uid) == uid_to_update:
                #self.cats[i].name = self.get_field('NEW NAME')
                #self.cats[i].age = self.get_field('NEW AGE')
                #self.cats[i].color = self.get_field('NEW COLOR')
        #else:
            #print('{} NOT FOUND!'.format(uid_to_update))


    def delete_cat(self):
        uid_to_delete = self.get_field('ID TO DELETE')
        for cat in self.cats:
            if str(cat.uid) == uid_to_delete:
                self.cats.remove(cat)
                #del(cat) NO BORRA EL GATO
                print('CAT DELETED!')
        else:
            print('CAT NOT FOUND!')


