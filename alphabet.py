dec_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
string = ''
count = 1

for dec in dec_array:
    if count % 2 == 0: dec = dec.upper()
    string = f'{string}{dec}[{str(count)}], '
    count = count + 1

print(string)