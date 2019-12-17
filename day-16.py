from itertools import cycle, count

with open("input-16.txt") as f:
    signal = f.readline().strip()


# Part 1

def pattern(n):
    for _ in range(n - 1):
        yield 0
    for i in cycle((1, 0, -1, 0)):
        for _ in range(n):
            yield i


def line_output(signal, n):
    p = pattern(n)
    res = 0
    for elem in signal:
        res += next(p) * int(elem)
    return str(res)[-1]

input = signal
for t in range(100): 
    output = ""
    for _, n in zip(input, count(1)):
        output += line_output(input, n)
    input = output

print(output[:8])



# Part 2

position = int(signal[:7])

long_signal = ""
while True:
    long_signal += signal
    if len(long_signal) >= len(signal) * 10000 - position:
        break

signal = long_signal[position % len(signal)  :]
signal = reversed(signal)

for j in range(100):
    output = ""
    somme = 0
    for i in signal:
        somme += int(i)
        output += str(somme)[-1]
    signal = output

signal = ''.join(list(s for s in reversed(signal)))
print(signal[:8])




