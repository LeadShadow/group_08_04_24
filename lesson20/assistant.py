from handlers import *

COMMANDS = {'hello': hello, 'add': add_contact, 'change': change_contact,
            'show all': show_all, 'phone': show_phone, 'exit': goodbye, 'close': goodbye,
            '.': goodbye, 'stop': goodbye, 'help': help_me, '?': help_me}


def main():
    contacts = {}
    while True:
        user_input = input('Enter command: ')
        for key in COMMANDS:
            if user_input.lower().startswith(key):
                args = user_input[len(key):].split()
                result = COMMANDS.get(key)(contacts, *args)
                if result is None:
                    print('Good bye!')
                    exit(0)
                print(result, '\n')
                break
        else:
            print('Unknown command! Enter again')


if __name__ == "__main__":
    main()
