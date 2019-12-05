def fuel_requirement(mass):
    fuel = mass // 3 - 2
    return fuel if fuel>0 else 0

# Part 1

with open("input-01.txt") as f:
    total_fuel_requirement = sum(fuel_requirement(int(mass)) for mass in f)

print(total_fuel_requirement)


# Part 2

def rec_fuel_requirement(mass):
    if mass <= 0:
        return 0
    else:
        fuel = fuel_requirement(mass)
        return fuel + rec_fuel_requirement(fuel)

with open("input-01.txt") as f:
    total_rec_fuel_requirement = sum(rec_fuel_requirement(int(mass)) for mass in f)

print(total_rec_fuel_requirement)
