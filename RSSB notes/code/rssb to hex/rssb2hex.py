import binascii

with open('input.txt') as f, open('output.txt', 'wb') as fout:
    for line in f:
        fout.write(
            chr(int(line))
        )