from intcode import run_intcode

with open("input-17.txt") as f:
    ASCII = f.readline().strip().split(',')

ASCII = [int(x) for x in ASCII]
scan = run_intcode(ASCII)


map = {}
x = 0
y = 0
while True:    
    try:
        c = next(scan)
    except StopIteration:
        break
    if c == 10:
        x = 0
        y += 1        
    else:
        map[(x,y)] = chr(c)
        x += 1

x_max = max(x for (x,y) in map)
y_max = max(y for (x,y) in map)
print(x_max)
print(y_max)

def draw_map(map):
    output = ""
    for y in range(y_max+1):
        for x in range(x_max+1):
            output += map[(x,y)]
        output += "\n"
    print(output)

    

draw_map(map)

intersections = set()
for x in range(1,x_max):
    for y in range(1, y_max):
        if map[(x,y)] == '#' and map[(x+1,y)] == '#' and map[(x-1,y)] == '#' and map[(x,y+1)] == '#' and map[(x,y-1)] == '#':
            intersections.add((x,y))

print(intersections)
calibration = sum(x*y for (x,y) in intersections)
print(calibration)

# Part 2
# don't work

ASCII[0] = 2
bot = run_intcode(ASCII)
print(next(bot))


main = "A,B,A,B,A,C,A,C,B,C"
a = "R,6,L,10,R,10,R,10"
b = "L,10,L,12,R,10"
c = "R,6,L,12,L,10"

print("main")
for char in main:
    print(bot.send(ord(char)))
print(bot.send(10))
print("A")
print(bot.send(ord(a[0])))
for char in a.split(',')[1:]:
    print(bot.send(ord(',')))
    print(bot.send(char))
print(bot.send(10))
print("C")
print(bot.send(ord(b[0])))
for char in b.split(',')[1:]:
    print(bot.send(ord(',')))
    print(bot.send(char))
print(bot.send(10))
print("C")
print(bot.send(ord(c[0])))
for char in c.split(',')[1:]:
    print(bot.send(ord(',')))
    print(bot.send(char))
output = bot.send(10)

print(output)




