import itertools

with open("input-07.txt") as f:
    input_code = [int(code) for code in f.readline().split(',')]


def run_intcode(intcode):
    program = list(intcode)
    i=0
    while True:
        instruction = program[i]
        opcode = instruction % 100
        if opcode == 99:
            return None
        elif opcode == 3:
            program[program[i+1]] = yield
            i += 2
        elif opcode == 4:
            yield program[program[i+1]]
            i += 2
        else:
            value_1 = program[i+1] if (instruction // 100) % 10 else program[program[i+1]]
            value_2 = program[i+2] if (instruction // 1000) % 10 else program[program[i+2]]

            if opcode == 1:
                program[program[i+3]] =  value_1 + value_2
                i += 4
            elif opcode == 2:
                program[program[i+3]] =  value_1 * value_2
                i += 4        
            elif opcode == 5:
                i = value_2 if value_1 else i+3
            elif opcode == 6:
                i = i+3 if value_1 else value_2
            elif opcode == 7:
                program[program[i+3]] = 1 if value_1 < value_2 else 0
                i += 4
            elif opcode == 8:
                program[program[i+3]] = 1 if value_1 == value_2 else 0
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
possible_outputs = (run_amps(start_amps(input_code, phases), 0) for phases in phases_permutations)
print(f"Highest signal Part 1 : {max(possible_outputs)}")



#  Part 2

def iterative_run_amps(amps, start_input):
    
    next_input = start_input
    while True:
        try:
            next_input = run_amps(amps, next_input)              
        except StopIteration:
            return next_input


phases_permutations = list(itertools.permutations(range(5,10)))
possible_outputs = (iterative_run_amps(start_amps(input_code, phases), 0) for phases in phases_permutations)
print(f"Highest signal Part 2 : {max(possible_outputs)}")


