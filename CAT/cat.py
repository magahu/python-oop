class Cat:
    CATS = [
    '''
     /\_/\     
    ( 0w0 )  ZzZzZ
    (     )   

    ''',
    '''

     /\_/\     o
    ( 0w0 )  (   )
    (     )   \_/

    ''',
    '''
              ___\_/___
      /\_/\   ||     ||
     ( 0w0 )  ||_____||
     (     )  |_______|

    '''
    ]

    def __init__(self, cat_name):
        self.name = cat_name

    def sleep(self):
        print(self.CATS[0])
        print('    {} IS SLEEPING    '.format(self.name.upper()))

    def eat(self):
        print(self.CATS[1])
        print('    {} IS EATING ICE CREAM    '.format(self.name.upper()))

    def watch_tv(self):
        print(self.CATS[2])
        print("    {} IS WATCHING A RANDOM TV SHOW    ".format(self.name.upper()))


