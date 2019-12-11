from intcode import run_intcode

UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

def get_new_position(coords, direction, turn):
    if turn == 0:
        direction += -1
    elif turn == 1:
        direction += 1

    if direction == 5:
        direction = UP
    elif direction == 0:
        direction = LEFT

    if direction == UP:
        coords = (coords[0], coords[1]+1)
    elif direction == RIGHT:
        coords = (coords[0]+1, coords[1])
    elif direction == DOWN:
        coords = (coords[0], coords[1]-1)
    elif direction == LEFT:
        coords = (coords[0]-1, coords[1])

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

print(f"Number of painted positions : {len(run_bot(input_code))}")
print()

# Part 2

colors = run_bot(input_code, start_colors= {(0, 0) : 1})

x_list = sorted(list(set(key[0] for key in colors.keys())))
y_list = sorted(list(set(key[1] for key in colors.keys())))

for j in reversed(y_list):
    line = ""
    for i in x_list:
        line += '▍' if colors.get((i, j), 0) == 1 else ' '
    print(line)
