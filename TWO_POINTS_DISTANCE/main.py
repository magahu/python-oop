from coordinate import Coordinate

def _first_screen():
    deco = '*'
    title ='{} FIND THE DISTANCE BETWEEN TWO POINS IN THE SPACE {}'.format(deco*3, deco*3)
    print('\n{}'.format(deco*len(title)))
    print(title)
    print('{}\n'.format(deco*len(title)))
    
def _get_value(message):
    value = None
    while not value:
        value = int(input(message))
    return value

def main():
    _first_screen()
    
    x1 = _get_value('X FOR THE FIRST POINT: ')
    y1 = _get_value('Y FOR THE FIRS POINT: ')
    
    x2 = _get_value('X FOR THE SECOND POINT: ')
    y2 = _get_value('Y FOR THE SECOND POINT: ')
    
    p1 = Coordinate(x1, y1)
    p2 = Coordinate(x2, y2)

    d = p1.find_distance(p2)
    

    print('\nThe distance between p1({}, {}) and p2({}, {}) is {}\n'.format(x1,
    y1, x2, y2, d))

    #print(isinstance(p1, Coordinate))
    #print(isinstance(1, Coordinate))

if __name__ == '__main__':
    main()
