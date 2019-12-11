from intcode import run_intcode

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