import math

def get_polar_coords(x, y):
    r = math.sqrt(x**2 + y**2)
    if y == 0:
        theta = math.pi / 2 if x > 0 else 3 * math.pi / 2
    else:            
        theta = -math.atan(x / y)
        theta = math.pi + theta if y > 0 else theta
    if x < 0 and y < 0:
        theta += 2 * math.pi
    return (r, round(theta, 15))

def get_vectorial_coords(rayon, angle):
    return (round(rayon * math.sin(angle)), -round(rayon * math.cos(angle)))

def get_relative_positions(orig, map):
    map = list(map)
    map.remove(orig)
    polar_positions = {}
    for dest in map:
        vec_x, vec_y = (dest[i] - orig[i] for i in range(2))
        polar_pos = get_polar_coords(vec_x, vec_y)
        polar_positions[polar_pos[1]] = sorted(polar_positions.get(polar_pos[1], []) + [polar_pos[0]])
    
    return polar_positions


with open("input-10.txt") as f:
    input_map = [line[:-1] for line in f]

map = []
for j, line in enumerate(input_map):
    for i in range(len(line)):
        if line[i] == "#":
            map.append((i,j))


relative_distances = {element : get_relative_positions(element, map) for element in map}


# Part 1

max_visible_asteroids = max(len(relative_distances[element]) for element in relative_distances)
best_position_coords = [element for element in relative_distances if len(relative_distances[element]) == max_visible_asteroids][0]
print(f"Best position : {best_position_coords} with {max_visible_asteroids} visible asteroides")


# Part 2


best_position = relative_distances[best_position_coords]
angle = sorted(best_position.keys())[199]
rayon = best_position[angle][0]

x_0, y_0 = best_position_coords
x_1, y_1 = get_vectorial_coords(rayon, angle)

print(f"The 200th asteroid to be vaporized is at ({x_0 + x_1},{y_0 + y_1})")

"""
Best position : (22, 25) with 286 visible asteroides
The 200th asteroid to be vaporized is at (5,4)
"""

