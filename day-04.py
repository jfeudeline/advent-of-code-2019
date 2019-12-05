puzzle_input = "359282-820401"
pwd_interval = [int(a) for a in puzzle_input.split('-')]
pwd_range = range(pwd_interval[0] , pwd_interval[1]+1)

# Part 1

def is_valid_pwd(code):
    str_code = str(code)
    double = False
    increase = True
    for i in range(5):
        if str_code[i] == str_code[i+1]:
            double = True
        elif str_code[i] > str_code[i+1]:
            increase = False
            break
    return double and increase



valid_passwords_1 = []
for code in pwd_range:
    if is_valid_pwd(code):
        valid_passwords_1.append(code)

print(len(valid_passwords_1))

# Part 2

def is_only_two_adjacents_digits(code):
    str_code = str(code)
    adjacent = 1
    for i in range(5):
        if str_code[i] == str_code[i+1]:
            adjacent += 1
        elif adjacent == 2:
                return True
        else:
            adjacent = 1
    return adjacent == 2

valid_passwords_2 = []
for code in valid_passwords_1:
    if is_only_two_adjacents_digits(code):
        valid_passwords_2.append(code)

print(len(valid_passwords_2))

