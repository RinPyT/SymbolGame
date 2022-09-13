from generate import generate_room
from random import randint


room_size = {'x': randint(3, 18),
             'y': randint(3, 18)}
room_list = generate_room(room_size['x'], room_size['y'])
room = room_list[0]


def move_player(list_room, x, y, keys):
    room = list_room
    if key == 'w' and list(room[y-1][x]) != list(room[0][0]):
        if list(room[y-1][x]) == list(room[len(room)//2][1]):
            new_room = 1
            return new_room
        else:
            first_position = list(room[y])
            second_position = list(room[y-1])
            first_position[x] = ' '
            room[y] = ''.join(first_position)
            second_position[x] = '▣'
            room[y-1] = ''.join(second_position)
            cordinate_player['y'] -= 1
            return room
    elif key == 's' and list(room[y+1][x]) != list(room[0][0]):
        if list(room[y+1][x]) == list(room[len(room)//2][1]):
            new_room = 1
            return new_room
        else:
            first_position = list(room[y])
            second_position = list(room[y+1])
            first_position[x] = ' '
            room[y] = ''.join(first_position)
            second_position[x] = '▣'
            room[y+1] = ''.join(second_position)
            cordinate_player['y'] += 1
            return room
    elif key == 'd' and list(room[y][x+1]) != list(room[0][0]):
        if list(room[y][x+1]) == list(room[len(room)//2][1]):
            new_room = 1
            return new_room
        else:
            position = list(room[y])
            second_position = x
            position[x] = ' '
            position[second_position + 1] = '▣'
            room[y] = ''.join(position)
            cordinate_player['x'] += 1
            return room
    elif key == 'a' and list(room[y][x-1]) != list(room[0][0]):
        if list(room[y][x-1]) == list(room[len(room)//2][1]):

            return room
        else:
            position = list(room[y])
            second_position = x
            position[x] = ' '
            position[second_position - 1] = '▣'
            room[y] = ''.join(position)
            cordinate_player['x'] -= 1
            return room
    else:
        return room


hp_player = 5
atk_player = 33
room_num = 0
cordinate_player = room_list[1]
key = ''
print('\n'.join(room))
while key != 'q':
    key = input()
    if move_player(room, cordinate_player['x'], cordinate_player['y'], key) == room:
        print("\n" * 40)
        print(f'Room {room_num}  HP:{hp_player}  Power:{atk_player}')
        print('\n'.join(room))
    elif move_player(room, cordinate_player['x'], cordinate_player['y'], key) == 1:
        room_list = generate_room(randint(3, 18), randint(3, 18))
        room = room_list[0]
        cordinate_player = room_list[1]
        room_num += 1
