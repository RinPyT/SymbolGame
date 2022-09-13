from random import randint
import math
object_ = {'walls': '##',
           'void': '  ',
           'player': '▣',
           'enemy': '*'}

room_level = 1


def generate_room(x: str, y: str) -> list:
    #room_level += 1
    room_obj = {'wall': object_['walls']*(x+2),
                'void': object_['walls'] + object_['void']*x + object_['walls']}
    secsefel_room = []
    i = 0
    while i != y:
        secsefel_room.append(room_obj['void'])
        i += 1
    secsefel_room.insert(0, room_obj['wall'])
    secsefel_room.append(room_obj['wall'])
    entery = randint(3, 10)
    sec_room = add_entery(secsefel_room, entery)
    return sec_room


def add_entery(room_list, entery):
    room = room_list
    count = 0
    while count != entery:
        i = randint(1, 3)
        if i == 1:
            sum_elements = (len(room[0]) - 4)/2
            if sum_elements <= 5:
                wall_list = list(room[0])
                numb_element = len(wall_list)//2
                wall_list[numb_element] = '·'
                wall_list[numb_element - 1] = '·'
                room[0] = ''.join(wall_list)
            elif 5 < sum_elements < 7:
                wall_list = list(room[0])
                numb_elements = [3, 4, -4, -5]
                for n_e in numb_elements:
                    wall_list[n_e] = '·'
                room[0] = ''.join(wall_list)
            elif sum_elements > 7:
                ent = randint(1, 4)
                wall_list = list(room[0])
                numb_elements = [
                    3, 4, len(wall_list)//2 - 1, len(wall_list)//2, -4, -5]
                if ent == 1:
                    wall_list[numb_elements[2]] = '·'
                    wall_list[numb_elements[3]] = '·'
                    room[0] = ''.join(wall_list)
                elif ent == 2:
                    wall_list[numb_elements[0]] = '·'
                    wall_list[numb_elements[1]] = '·'
                    room[0] = ''.join(wall_list)
                elif ent == 3:
                    for n_e in numb_elements:
                        wall_list[n_e] = '·'
                    room[0] = ''.join(wall_list)
            count += 1
        elif i == 2:
            sum_elements = len(room) - 2
            if sum_elements <= 3:
                wall_list = list(room[len(room)//2])
                wall_list[-1] = '·'
                wall_list[-2] = '·'
                room[len(room)//2] = ''.join(wall_list)
            elif 4 <= sum_elements <= 7:
                wall_list_one = list(room[2])
                wall_list_two = list(room[-3])
                wall_list_one[-1] = '·'
                wall_list_one[-2] = '·'
                wall_list_two[-1] = '·'
                wall_list_two[-2] = '·'
                room[2] = ''.join(wall_list_one)
                room[-3] = ''.join(wall_list_two)
            elif 8 < sum_elements:
                wall_list_one = list(room[2])
                wall_list_two = list(room[len(room)//2])
                wall_list_three = list(room[-3])
                wall_list_one[-1] = '·'
                wall_list_one[-2] = '·'
                wall_list_two[-1] = '·'
                wall_list_two[-2] = '·'
                wall_list_three[-1] = '·'
                wall_list_three[-2] = '·'
                room[2] = ''.join(wall_list_one)
                room[len(room)//2] = ''.join(wall_list_two)
                room[-3] = ''.join(wall_list_three)
            count += 1
        elif i == 3:
            sum_elements = (len(room[-1]) - 4)/2
            if sum_elements <= 5:
                wall_list = list(room[-1])
                numb_element = len(wall_list)//2
                wall_list[numb_element] = '·'
                wall_list[numb_element - 1] = '·'
                room[-1] = ''.join(wall_list)
            elif 5 < sum_elements < 7:
                wall_list = list(room[-1])
                numb_elements = [3, 4, -4, -5]
                for n_e in numb_elements:
                    wall_list[n_e] = '·'
                room[-1] = ''.join(wall_list)
            elif sum_elements >= 7:
                ent = randint(1, 4)
                wall_list = list(room[-1])
                numb_elements = [
                    3, 4, len(wall_list)//2 - 1, len(wall_list)//2, -4, -5]
                if ent == 1:
                    wall_list[numb_elements[2]] = '·'
                    wall_list[numb_elements[3]] = '·'
                    room[-1] = ''.join(wall_list)
                elif ent == 2:
                    wall_list[numb_elements[0]] = '·'
                    wall_list[numb_elements[1]] = '·'
                    room[-1] = ''.join(wall_list)
                elif ent == 3:
                    for n_e in numb_elements:
                        wall_list[n_e] = '·'
                    room[-1] = ''.join(wall_list)
            count += 1

    return set_player(room)


def add_enemy(room_list):
    room = room_list
    enemy_coef = room_level / 100
    count_enemy = math.ceil(len(room) * len(room[0])*enemy_coef)
    for i in range(count_enemy):
        position_set = {'x': randint(2, len(room[0])-2),
                        'y': randint(2, len(room)-1)}
        y_position = list(room[position_set['y']])
        y_position[position_set['x']] = object_['enemy']
        room[position_set['y']] = ''.join(y_position)

    return room


def set_player(room_list):
    room = room_list
    numb_position = len(room)//2
    position = list(room[numb_position])
    position[2] = object_['player']
    position[0] = ' '
    position[1] = '·'
    room[numb_position] = ''.join(position)
    cordinate_player = {'x': 2, 'y': numb_position}
    return add_enemy(room), cordinate_player
