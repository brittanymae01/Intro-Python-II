from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['outside'].add_item(Item('Sword', 'Cuts things'))
room['outside'].add_item(Item('Rock', 'Breaks things'))
room['overlook'].add_item(Item('Map', 'Tells you where to go'))
room['narrow'].add_item(Item('Key', 'Opens things'))
room['foyer'].add_item(Item('Potion', 'Renders things inactive'))
room['treasure'].add_item(Item('Gold', 'You win with this'))
#
# Main
#
class colors:
    blink = '\033[5m'
    red = '\033[91m'
    yellow = '\033[93m'
    reset = '\033[0m'

def invalidSelection(sentance = '\nYou cannot go that way!\n'):
    print(f'{colors.red}{colors.blink}{sentance}{colors.reset}')

def commands():
    print('\nPlease choose a command...\n')
    return input("[n] north  [s] south  [e] east [w] west [Get item] [Drop item] [i] Get inventory [q] Quit\n").lower()

def playerInfo():
    print(f"\n{colors.yellow}{name}, You are in the {player.current_room.name} \n {player.current_room.description}{colors.reset} \n")

player = Player(room['outside'])

def item_func():
    print('Items in room:')
    for item in player.current_room.items:
        print(f'{colors.yellow}{item.name} -- {item.description}{colors.reset}')

name = input('What is your name?\n' )
playerInfo()
item_func()
command = commands()

# Make a new player object that is currently in the 'outside' room.

# player = Player(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

splitCommand = command.split(' ')

while not command == 'q':
    splitCommand = command.split(' ')
    if len(splitCommand) == 1:
        if command == 'i':
            player.get_inventory()
        elif command == 'n':
            if player.current_room.n_to == None:
                invalidSelection()
            else:
                player.update_room(player.current_room.n_to)
        elif command == 's':
            if player.current_room.s_to == None:
                invalidSelection()
            else: 
                player.update_room(player.current_room.s_to)
        elif command == 'w':
            if player.current_room.w_to == None:
                invalidSelection()
            else: 
                player.update_room(player.current_room.w_to)
        elif command == 'e':
            if player.current_room.e_to == None:
                invalidSelection()
            else:
                player.update_room(player.current_room.e_to)
        else:
            invalidSelection('Try again, pick a valid direction this time')
    elif len(splitCommand) == 2:
        if splitCommand[0].lower() == 'get':
            for item in player.current_room.items:
                if item.name.lower() == splitCommand[1].lower():
                    player.current_room.items.remove(item)
                    player.inventory.append(item)
                    item.on_take(item.name.lower())
        elif splitCommand[0].lower() == 'drop':
            for item in player.inventory:
                if item.name.lower() == splitCommand[1].lower():
                    player.inventory.remove(item)
                    player.current_room.items.append(item)
                    item.on_drop(item.name.lower())
        else:
            print('That command does not exist')
    else:
        print('Try another command')

    playerInfo()
    item_func()
    command = commands()

    # if player.current_room == room['outside']:
    #     # print('Options: North to the Foyer')
    #     if command == 'n':
    #         player.update_room(room['foyer'])
    #     else:
    #         print("You cannot go that way!\n\n")
    # elif player.current_room == room['foyer']:
    #     if command == 'n':
    #         player.update_room(room['overlook'])
    #     elif command == 'e':
    #         player.update_room(room['narrow'])
    #     elif command == 's':
    #         player.update_room(room['outside'])
    #     else:
    #         print("You cannot go that way!\n\n")
    # elif player.current_room == room['overlook']:
    #     if command == 's':
    #         player.update_room(room['foyer'])
    #     else:
    #         print("You cannot go that way!")
    # elif player.current_room == room['narrow']:
    #     if command == 'w':
    #         player.update_room(room['foyer'])
    #     elif command == 'n':
    #         player.update_room(room['treasure'])
    #     else:
    #         print('You cannot go this way!\n\n')
    # elif player.current_room == room['treasure']:
    #     if command == 's':
    #         player.update_room(room['narrow'])
    #     else:
    #         print('You cannot go that way!\n\n')