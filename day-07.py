import itertools

from intcode import run_intcode


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



with open("input-07.txt") as f:
    input_code = [int(code) for code in f.readline().split(',')]
        

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


