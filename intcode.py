def get_index(program, index, mode, base):
        if mode == 0:
            index = program[index]
        elif mode == 2:
            index = base + program[index]
        if index >= len(program) :
            program += [0] *  (index + 1- len(program))
        return index

number_of_parameters = {
    # number of parameters of an opcode
    1 : 3,
    2 : 3,
    3 : 1,
    4 : 1,
    5 : 2,
    6 : 2,
    7 : 3,
    8 : 3,
    9 : 1
}
                

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
            
            indexes = [get_index(program, index=i+j+1, mode= modes[j], base=base) for j in range(number_of_parameters[opcode])]
            
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

# old version without base : sufficient for day 7
"""
def get_index(program, index, mode):
        if mode == 0:
            index = program[index]
        if index >= len(program) :
            program += [0] *  (index + 1- len(program))
        return index


def run_intcode(intcode):
    program = list(intcode)
    i=0

    while True:

        instruction = program[get_index(program, index=i, mode=1)]
        opcode = instruction % 100

        if opcode == 99:
            return None
        
        else:
            modes = [(instruction // 10**n) % 10 for n in range(2, 5)]
            indexes = [get_index(program, index=i+j+1, mode= modes[j]) for j in range(3)]
            
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
"""
