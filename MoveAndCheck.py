def move_player(list_room, x, y, keys, cordinate_player):
    room = list_room
    if keys == 'w' and list(room[y-1][x]) != list(room[0][0]):
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
    elif keys == 's' and list(room[y+1][x]) != list(room[0][0]):
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
    elif keys == 'd' and list(room[y][x+1]) != list(room[0][0]):
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
    elif keys == 'a' and list(room[y][x-1]) != list(room[0][0]):
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


def check_environment(list_room : list, cordinate_paler: dict) -> list[int]:
  

  pass