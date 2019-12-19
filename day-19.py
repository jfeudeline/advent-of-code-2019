from intcode import run_intcode

with open("input-19.txt") as f:
    code = [int(x) for x in f.readline().strip().split(',')]


def test_beam(point):
    drone = run_intcode(code)
    next(drone)
    drone.send(point[0])
    return drone.send(point[1])


# Part 1

number_of_beam_points = sum(test_beam((x,y)) for x in range(50) for y in range(50))
print(number_of_beam_points)

# Part 2

x, y = 0, 0
while True:
    if test_beam((x, y+99)):
        if test_beam((x+99, y)):
            break
        else:
            y += 1
    else:
        x += 1
    
print(10000 * x + y)    

