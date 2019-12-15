# code non nettoyé #
####################

class Moon():

    def __init__(self, name, position):
        self.position = position
        self.name = name
        self.velocity = (0, 0, 0)
        self.initial_state = tuple((self.position[i], self.velocity[i]) for i in range(3))
        

    def update_position(self):
        self.position = tuple(x + v for x, v in zip(self.position, self.velocity))

    def update_velocity(self, moons):
        for moon in moons:
            self.velocity = tuple(
                v + (x < y) - (x > y) for x, v, y in zip(self.position, self.velocity, moon.position)
            )

    def __repr__(self):
        return f"{self.name} : position = {self.position}, velocity = {self.velocity}"

    def get_energy(self):
        return sum(abs(x) for x in self.position) * sum(abs(v) for v in self.velocity)


    

def update_system(moons):
    for moon in moons:
        moon.update_velocity(moons)
    for moon in moons:
        moon.update_position()


# part 1

moons = []
moons.append(Moon('Io', (-10, -10, -13)))
moons.append(Moon('Europa', (5, 5, -9)))
moons.append(Moon('Ganymede', (3, 8, -16)))
moons.append(Moon('Callisto', (1, 3, -3)))

for t in range(1000):
    update_system(moons)
print(sum(moon.get_energy() for moon in moons))


# Part 2

moons = []
moons.append(Moon('Io', (-10, -10, -13)))
moons.append(Moon('Europa', (5, 5, -9)))
moons.append(Moon('Ganymede', (3, 8, -16)))
moons.append(Moon('Callisto', (1, 3, -3)))

revolution = [False, False, False]
revolution_time = [0, 0, 0]
t = 1
while True:
    update_system(moons)
    for i in range(3):
        if not revolution[i] and sum(moon.initial_state[i] == (moon.position[i], moon.velocity[i]) for moon in moons) == 4:
            for moon in moons:
                print(moon)
            print(t)
            revolution[i] = True
            revolution_time[i] = t
    
    #if t % 100000 == 0:
    #    print(t)
    if revolution == [True, True, True]:
        break
    t += 1 

def ppcm(a,b):
    p=a*b
    while(a!=b):
        if (a<b): b-=a
        else: a-=b
    return p//a

result = ppcm(ppcm(revolution_time[2], revolution_time[1]), revolution_time[0])


print(result)



"""
Test sets

moons = []
moons.append(Moon('Io', (-1, 0, 2)))
moons.append(Moon('Europa', (2, -10, -7)))
moons.append(Moon('Ganymede', (4, -8, 8)))
moons.append(Moon('Callisto', (3, 5, -1)))


moons = []
moons.append(Moon('Io', (-8, -10, 0)))
moons.append(Moon('Europa', (5, 5, 10)))
moons.append(Moon('Ganymede', (2, -7, 3)))
moons.append(Moon('Callisto', (9, -8, -3)))





for t in range(1000):
    update_system(moons)
print(sum(moon.get_energy() for moon in moons))

"""




