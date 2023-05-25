import container
import re

while True:
    username = input("Enter username: ")
    if not re.findall(r'\b[A-z]\w+\b', username):
        print('Incorrect name.')
    else:
        container = container.Container(username)
        break

while True:
    command = input('> ').split()

    if (command[0] == 'add'):
        if len(command) == 1:
            print('You entered the wrong command.')
        else:
            container.add(*command[1:])
    elif (command[0] == 'remove'):
        if len(command) != 2:
            print('You entered the wrong command.')
        else:
            container.remove(command[1])
    elif (command[0] == 'find'):
        if len(command) == 1:
            print('You entered the wrong command.')
        else:
            container.find(*command[1:])
    elif (command[0] == 'list'):
        if len(command) != 1:
            print('You entered the wrong command.')
        else:
            container.list()
    elif (command[0] == 'grep'):
        if len(command) == 3 and (command[2].lower() == 'true' or command[2].lower() == 'false'):
            if command[2].lower() == 'true':
                container.grep(command[1], True)
            else:
                container.grep(command[1], False)
        elif len(command) == 2:
            container.grep(command[1])
        else:
            print('You entered the wrong command.')
    elif (command[0] == 'save'):
        if len(command) != 1:
            print('You entered the wrong command.')
        else:
            container.save()
    elif (command[0] == 'load'):
        if len(command) != 1:
            print('You entered the wrong command.')
        else:
            container.load()
    elif (command[0] == 'switch'):
        if len(command) != 2:
            print('You entered the wrong command.')
        else:
            container.switch(command[1])
    elif (command[0] == 'exit'):
        break
    else:
        print('You entered the wrong command.')






    # match command[0]:
    #     case 'add':
    #         if len(command) == 1:
    #             print('You entered the wrong command.')
    #         else:
    #             container.add(*command[1:])
    #     case 'remove':
    #         if len(command) != 2:
    #             print('You entered the wrong command.')
    #         else:
    #             container.remove(command[1])
    #     case 'find':
    #         if len(command) == 1:
    #             print('You entered the wrong command.')
    #         else:
    #             container.find(*command[1:])
    #     case 'list':
    #         if len(command) != 1:
    #             print('You entered the wrong command.')
    #         else:
    #             container.list()
    #     case 'grep':
    #         if len(command) == 3 and (command[2].lower() == 'true' or command[2].lower() == 'false'):
    #             if command[2].lower() == 'true':
    #                 container.grep(command[1], True)
    #             else:
    #                 container.grep(command[1], False)
    #         elif len(command) == 2:
    #             container.grep(command[1])
    #         else:
    #             print('You entered the wrong command.')
    #     case 'save':
    #         if len(command) != 1:
    #             print('You entered the wrong command.')
    #         else:
    #             container.save()
    #     case 'load':
    #         if len(command) != 1:
    #             print('You entered the wrong command.')
    #         else:
    #             container.load()
    #     case 'switch':
    #         if len(command) != 2:
    #             print('You entered the wrong command.')
    #         else:
    #             container.switch(command[1])
    #     case _:
    #         print('You entered the wrong command.')
