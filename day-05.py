with open("input-05.txt") as f:
    input_code = [int(code) for code in f.readline().split(',')]


def run_intcode(intcode, input):
    outputs = []
    program = list(intcode)
    i=0
    while True:
        instruction = program[i]
        opcode = instruction % 100
 
        if opcode == 99:
            break
        elif opcode == 3:
            program[program[i+1]] = input
            i += 2
        elif opcode == 4:
            outputs.append(program[program[i+1]])
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
         
    return outputs
 



# Part 1
print(run_intcode(input_code, 1))

#Part 2
print(run_intcode(input_code, 5))

