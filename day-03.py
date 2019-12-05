with open("input-03.txt") as f:
    wires = []
    for line in f:
        wires.append(line.split(','))


# Calcul des coordonnées de passages des deux chemins

def get_coords_line(start, move):
    "Calcule les coordonnées de passage d'une ligne"
    directions = {
        'R' : (0, 1),
        'L' : (0, -1),
        'U' : (1, 1),
        'D' : (1, -1)
    }
    dir = directions[move[0]]
    line = []
    now = list(start)
    for step in range(int(move[1:])):
        now[dir[0]] += dir[1]
        line.append(tuple(now))
    return line


def get_coords_path(wire):
    "Calcule les coordonnées de passage d'un chemin"
    path = [(0,0)]
    for step in wire:
        path += get_coords_line(path[-1], step)
    return path

# Coordonnées des points de passages des chemins
paths=[]
for wire in wires:
    paths.append(get_coords_path(wire))

# Coordonnées des intersections des chemins
intersections = set(paths[0][1:]).intersection(set(paths[1][1:]))


# Part 1

intersections_distances = (abs(x) + abs(y) for x, y in intersections)

print(min(intersections_distances))

# Part 2

intersections_lengths = (paths[0].index(coord) + paths[1].index(coord) for coord in intersections)

print(min(intersections_lengths))


