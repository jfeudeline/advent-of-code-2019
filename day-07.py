import itertools

with open("input-07.txt") as f:
    input_code = [int(code) for code in f.readline().split(',')]

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


def start_amp(program, phase):
    amp = run_intcode(program)
    next(amp)
    amp.send(phase)
    return amp
    

def start_amps(program, phases):
    amps = []
    for phase in phases:
        amps.append(start_amp(program, phase))
    return amps


def run_amps(amps, start_input):
    next_input = start_input
    for amp in amps:
            next_input = amp.send(next_input)
            try : 
                next(amp)
            except StopIteration:
                pass
    return next_input
        

# Part 1

phases_permutations = list(itertools.permutations(range(5)))
signals = (run_amps(start_amps(input_code, phases), 0) for phases in phases_permutations)
print(f"Highest signal Part 1 : {max(signals)}")



#  Part 2

def iterative_run_amps(amps, start_input):    
    next_input = start_input
    while True:
        try:
            next_input = run_amps(amps, next_input)              
        except StopIteration:
            return next_input


phases_permutations = list(itertools.permutations(range(5,10)))
signals = (iterative_run_amps(start_amps(input_code, phases), 0) for phases in phases_permutations)
print(f"Highest signal Part 2 : {max(signals)}")


