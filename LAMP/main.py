
from lamp import Lamp

def main():
    lamp = Lamp(is_turned_on=False)

    while True:
        command = str(input('''
            What do dou wanna do?
            
            [ON]  Turn on
            [OFF] Turn off
            [E]  Exit
            
            Enter your selection: ''')).upper()

        if command == 'ON':
            lamp.turn_on()
        elif command == 'OFF':
            lamp.turn_off()
        elif command == 'E':
            break
        else:
            print('\n    INVALID OPTION!    \n')


if __name__ == '__main__':
    main()
