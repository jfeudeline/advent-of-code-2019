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


def run_boost(program, start_input = None):

    boost = run_intcode(program)    
    print("Starting...")

    if start_input:
        next(boost)
        print(f"Output : {boost.send(start_input)}")

    while True:
        try :
            print(f"Output : {next(boost)}")
        except StopIteration:
            print("...Ending")
            break





with open("input-09.txt") as f:
    input_code = [int(code) for code in f.readline().split(',')]

test1 = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
test2 = [1102,34915192,34915192,7,4,7,99,0]
test3 = [104,1125899906842624,99]

#run_boost(test1)
#run_boost(test2)
#run_boost(test3)
run_boost(input_code, start_input=1)
run_boost(input_code, start_input=2)