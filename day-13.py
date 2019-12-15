# code non nettoyé #
####################

import sys

from intcode import run_intcode

def draw_screen(screen):

    draw = {
    0 : ' ',
    1 : '#',
    2 : '*',
    3 : '_',
    4 : '.'
    }

 

    for y in range(24):
        line_elements = []
        for x in range(44):
            line_elements.append(draw[screen[(x,y)]])
        print(''.join(line_elements))


with open("input-13.txt") as f:
    input_code = [int(code) for code in f.readline().split(',')]

# Part 1

game = run_intcode(input_code)
screen = {}
while True:
    try:
        x = next(game)
        y = next(game)
        tile = next(game)
        screen[(x, y)] = tile
    except StopIteration: 
        break

blocks = [tile for tile in screen.values() if tile == 2]

draw_screen(screen)
print(f"Number of blocks : {len(blocks)}" )



# Part 2


input_code[0] = 2
game = run_intcode(input_code)
screen = {}
for _ in range(44 * 24):
        x = next(game)
        y = next(game)
        tile = next(game)
        screen[(x, y)] = tile
        if tile == 4:
            ball_position = x
        elif tile == 3:
            paddle_postion = y




start_game = True
joystick_move = 0



while True:
    try:
        x = game.send(joystick_move)
        y = next(game)
        tile = next(game)
        
    except StopIteration:
        break
    if x == -1:
        score = tile
        #print(f"Score : {score}")
        if start_game:
            start_game = False
            next(game)
    else:    
        if tile == 4:
            next(game)
            ball_position = x
            if paddle_postion < ball_position:
                joystick_move = 1
                paddle_postion += 1
            elif paddle_postion > ball_position:
                joystick_move = -1
                paddle_postion += -1
            else:
                joystick_move = 0    
        #print(f"({x}, {y}) : {tile}")
        screen[(x, y)] = tile
        #draw_screen(screen)

print(f"Score : {score}")   
