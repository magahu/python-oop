#CLASS INSTANTIATION
#class
class say_Hi:
    #attribute
    programmer_name = 'Margarita'
    #method
    def print_Hi(self):
        print('HI, {}'.format(say_Hi.programmer_name))
        #INSIDE THE CLASS WE ACCESS TO THE ATTRIBUTE LIKE THIS:
        #    class.attribute

def run():
    #OBJECT INSTANTIATION
    obj_Hi = say_Hi()
    #creates a new instance of the say_Hi class
    #and assigns this object to the local variable obj_Hi
    obj_Hi.print_Hi()
    #WE ACCESS METHODS LIKE THIS:
    #    instance.method()

if __name__ == '__main__':
    run()
