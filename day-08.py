with open("input-08.txt") as f:
    input_code = f.readline()

row_length = 25
col_length = 6
image_length = row_length * col_length
number_of_layers = len(input_code) // (image_length)

layers = []
for i in range(number_of_layers):
    layers.append(input_code[i * image_length : (i+1) * image_length])


# Part 1


min_number_of_0 = image_length
for layer in layers:
    number_of_0 = layer.count('0')
    if number_of_0 <= min_number_of_0:
        min_number_of_0 = number_of_0
        test_result = layer.count('1') * layer.count('2')

print("Part 1 :")
print("--------")
print(f"Test result : {test_result}")
print()



# Part 2

final_image = ['2'] * image_length


for layer in reversed(layers):
    for i in range(image_length):
        if layer[i] != '2':
            final_image[i] = layer[i]

decoded_image = final_image

for i in range(image_length):
    decoded_image[i] = '▍' if final_image[i] == '1' else ' '

decoded_image = ''.join(decoded_image)


print("Part 2 :")
print("--------")


for row in range(col_length):
    start = row * row_length
    print(decoded_image[start : start + row_length])

print()

"""
Part 1 :
--------
Test result : 2080

Part 2 :
--------
 ▍▍  ▍  ▍ ▍▍▍   ▍▍  ▍   ▍
▍  ▍ ▍  ▍ ▍  ▍ ▍  ▍ ▍   ▍
▍  ▍ ▍  ▍ ▍  ▍ ▍     ▍ ▍ 
▍▍▍▍ ▍  ▍ ▍▍▍  ▍      ▍  
▍  ▍ ▍  ▍ ▍ ▍  ▍  ▍   ▍  
▍  ▍  ▍▍  ▍  ▍  ▍▍    ▍ 
"""



