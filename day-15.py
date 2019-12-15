# code non nettoyé #
####################
from intcode import run_intcode

with open("input-15.txt") as f:
    input_code = [int(code) for code in f.readline().split(',')]

droid = run_intcode(input_code)
next(droid)

NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4

test_directions = {
    NORTH : (WEST, NORTH, EAST, SOUTH),
    SOUTH : (EAST, SOUTH, WEST, NORTH),
    WEST : (SOUTH, WEST, NORTH, EAST),
    EAST : (NORTH, EAST, SOUTH, WEST)
}

draw = {
    1 : '.',
    0 : '█',
    2 : '*'
}

def get_new_position(coords, direction):
    
    dir_coords = {
        NORTH : (0, 1),
        WEST: (1, 0),
        SOUTH : (0, -1),
        EAST : (-1, 0)
    }

    coords = tuple(coords[i] + dir_coords[direction][i] for i in range(2))

    return coords


# Part 1

current_position = (0, 0)
positions = [current_position]
screen = {(x,y) : ' ' for x in range(-25, 25) for y in range(-25, 25)}

current_direction = NORTH

while True:
    for direction in test_directions[current_direction]:
        test_position = get_new_position(current_position, direction)
        reply = droid.send(direction)
        screen[test_position] = draw[reply]
        next(droid)
        if reply:
            if reply == 2:
                oxygen_position = test_position
            current_direction = direction
            screen[current_position] = '.'
            current_position = test_position
            if current_position in positions:
                positions = positions[: positions.index(current_position)+1]
            else:
                positions.append(current_position)            
            break
        
    if reply == 2:
        break

def draw_screen(screen):

    for y in range(24, -26, -1):
        line_elements = []
        for x in range(-25, 25):
            line_elements.append(screen[(x,y)])
        print(''.join(line_elements))



#draw_screen(screen)
print(len(positions) - 1)


# Part 2

for _ in range(1000):
    for direction in test_directions[current_direction]:
        test_position = get_new_position(current_position, direction)
        reply = droid.send(direction)
        screen[test_position] = draw[reply]
        next(droid)
        if reply:
            if reply == 2:
                oxygen_position = test_position
            current_direction = direction
            screen[current_position] = '.'
            current_position = test_position
            if current_position in positions:
                positions = positions[: positions.index(current_position)+1]
            else:
                positions.append(current_position)            
            break



screen[oxygen_position] = 'O'
draw_screen(screen)

volume = sum(1 for position in screen if screen[position] == '.')


t = 0
oxygen = [oxygen_position]

while volume:
    t += 1
    new_oxygen = []
    for position in oxygen:
        
        for direction in (NORTH, SOUTH, WEST, EAST):
            new_position = get_new_position(position, direction)
            if  screen[new_position] == '.':
                new_oxygen.append(new_position)
                volume -= 1
                screen[new_position] = 'O'
    oxygen = new_oxygen

    #print(f"{t} : {volume}")


print(t)
