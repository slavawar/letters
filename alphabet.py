dec_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
count = 1
result_array = []

for dec in dec_array:
    if not count & 1: dec = dec.upper()
    result_array.append(f'{dec}[{str(count)}]')
    count = count + 1

print(", ".join(result_array))