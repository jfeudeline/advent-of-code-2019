with open("input-02.txt") as f:
    input_code = [int(code) for code in f.readline().split(',')]


# Part 1



def run_intcode(intcode, noun, verb):
    program = list(intcode)
    program[1] = noun
    program[2] = verb
    i=0
    while True:
        if program[i] == 99:
            break
        elif program[i] == 1:
            program[program[i+3]] = program[program[i+1]] + program[program[i+2]]
        elif program[i] == 2:
            program[program[i+3]] = program[program[i+1]] * program[program[i+2]]
        i = i + 4
    return program[0]




print(run_intcode(input_code, 12, 2))


# Part 2


def search_input(program, output):
    for noun in range(99):
        for verb in range(99):
           if run_intcode(program, noun, verb) == output:
               return 100 * noun + verb
    return None


print(search_input(input_code, 19690720))
        
    
    




