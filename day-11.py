def get_index(program, index, mode, base):
        if mode == 0:
            index = program[index]
        elif mode == 2:
            index = base + program[index]
        if index >= len(program) :
            program += [0] *  (index + 1- len(program))
        return index


def run_intcode(intcode):
    program = list(intcode)
    i=0
    base = 0

    while True:

        instruction = program[get_index(program, index=i, mode=1, base=base)]
        opcode = instruction % 100

        if opcode == 99:
            return None
        
        else:
            modes = [(instruction // 10**n) % 10 for n in range(2, 5)]
            indexes = [get_index(program, index=i+j+1, mode= modes[j], base=base) for j in range(3)]
            
            if opcode == 1:
                program[indexes[2]] = program[indexes[0]] + program[indexes[1]]
                i += 4

            elif opcode == 2:
                program[indexes[2]] = program[indexes[0]] * program[indexes[1]]
                i += 4  

            elif opcode == 3:
                program[indexes[0]] = yield
                i += 2

            elif opcode == 4:
                yield  program[indexes[0]]
                i += 2

            elif opcode == 5:
                i = program[indexes[1]] if program[indexes[0]] else i+3

            elif opcode == 6:
                i = i+3 if program[indexes[0]] else program[indexes[1]]

            elif opcode == 7:
                program[indexes[2]] = 1 if program[indexes[0]] < program[indexes[1]] else 0
                i += 4

            elif opcode == 8:
                program[indexes[2]] = 1 if program[indexes[0]] == program[indexes[1]] else 0
                i += 4

            elif opcode == 9:
                base += program[indexes[0]]
                i += 2

with open("input-11.txt") as f:
    input_code = [int(code) for code in f.readline().split(',')]

# test code
input_code = "103,0,104,1,104,0,103,0,104,0,104,0, 103,0,104,1,104,0, 103,0,104,1,104,0, 103,0,104,0,104,1, 103,0,104,1,104,0, 103,0,104,1,104,0,99".split(",")
input_code = [int(code) for code in input_code]

def get_new_position(pos, dir, turn):
    if turn == 0:
        dir += -1
    elif turn == 1:
        dir += 1
    if dir == 5:
        dir = 1
    elif dir == -1:
        dir = 4
    if dir==1:
        pos = (pos[0], pos[1]+1)
    elif dir==2:
        pos = (pos[0]+1, pos[1])
    elif dir==3:
        pos = (pos[0], pos[1]-1)
    elif dir==4:
        pos = (pos[0]-1, pos[1])
    return pos, dir


position = (0,0)
direction = 1
colors = {}

bot = run_intcode(input_code)
next(bot)
while True:
#for _ in range(10):
    #print("Position : {}, direction : {}".format(position, direction))
    color = bot.send(colors.get(position, 0))
    #print(f"Color : {color}")
    colors[position] = color
    turn = next(bot)
    #print(f"Turn : {turn}")
    position, direction = get_new_position(position, direction, turn)
    #print(f"Painted positions {colors}")
    try:        
        next(bot)
    except StopIteration:
        print(len(colors))
        break