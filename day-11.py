from intcode import run_intcode


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


def get_new_position(coords, direction, turn):

    turn = 1 if turn == 1 else -1
    direction = (direction + turn) % 4
    
    dir_coords = {
        UP : (0, 1),
        RIGHT : (1, 0),
        DOWN : (0, -1),
        LEFT : (-1, 0)
    }

    coords = tuple(coords[i] + dir_coords[direction][i] for i in range(2))

    return coords, direction


def run_bot(program, start_colors = {}):

    position = (0,0)
    direction = UP
    colors = start_colors

    bot = run_intcode(program)    
    next(bot)

    while True:

        color = bot.send(colors.get(position, 0))
        colors[position] = color

        turn = next(bot)
        position, direction = get_new_position(position, direction, turn)

        try:        
            next(bot)
        except StopIteration:
            break

    return colors



with open("input-11.txt") as f:
    input_code = [int(code) for code in f.readline().split(',')]

# test code
#input_code = "103,0,104,1,104,0,103,0,104,0,104,0, 103,0,104,1,104,0, 103,0,104,1,104,0, 103,0,104,0,104,1, 103,0,104,1,104,0, 103,0,104,1,104,0,99".split(",")
#input_code = [int(code) for code in input_code]


# Part 1
print("Part 1 :")
print("--------")
print(f"Number of painted positions : {len(run_bot(input_code))}")
print()

# Part 2

colors = run_bot(input_code, start_colors= {(0, 0) : 1})

x_list = sorted(list(set(key[0] for key in colors.keys())))
y_list = sorted(list(set(key[1] for key in colors.keys())))


print("Part 2 :")
print("--------")
for j in reversed(y_list):
    line = ""
    for i in x_list:
        line += '▍' if colors.get((i, j), 0) == 1 else ' '
    print(line)

"""
Part 1 :
--------
Number of painted positions : 1747

Part 2 :
--------
 ▍▍▍▍  ▍▍   ▍▍  ▍▍▍  ▍  ▍ ▍  ▍ ▍    ▍▍▍    
    ▍ ▍  ▍ ▍  ▍ ▍  ▍ ▍  ▍ ▍ ▍  ▍    ▍  ▍   
   ▍  ▍    ▍    ▍  ▍ ▍▍▍▍ ▍▍   ▍    ▍▍▍    
  ▍   ▍    ▍ ▍▍ ▍▍▍  ▍  ▍ ▍ ▍  ▍    ▍  ▍   
 ▍    ▍  ▍ ▍  ▍ ▍ ▍  ▍  ▍ ▍ ▍  ▍    ▍  ▍   
 ▍▍▍▍  ▍▍   ▍▍▍ ▍  ▍ ▍  ▍ ▍  ▍ ▍▍▍▍ ▍▍▍ 
"""