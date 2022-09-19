from generate import generate_room
from random import randint
from MoveAndCheck import move_player

room_size = {'x': randint(3, 18),
             'y': randint(3, 18)}
room_list = generate_room(room_size['x'], room_size['y'])
ROOM = room_list[0]
hp_player = 5
atk_player = 33
room_num = 0
cordinate_player = room_list[1]
key = ''
print('\n'.join(ROOM))


while key != 'q':
    key = input()
    if move_player(ROOM, cordinate_player['x'], cordinate_player['y'], key, cordinate_player) == ROOM:
        print("\n" * 40)
        print(f'Room {room_num}  HP:{hp_player}  Power:{atk_player}')
        print('\n'.join(ROOM))
    elif move_player(ROOM, cordinate_player['x'], cordinate_player['y'], key, cordinate_player) == 1:
        room_list = generate_room(randint(3, 18), randint(3, 18))
        ROOM = room_list[0]
        cordinate_player = room_list[1]
        room_num += 1
