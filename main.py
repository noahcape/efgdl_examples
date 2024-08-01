import sys
import io

args = sys.argv

if len(args) != 2:
    raise Exception("Expected a directory as a second argument")


dir = args[1]
f = io.open("{}/barcode_1_map.txt".format(dir), "r")

oligo = [0]*48
hexamer = [0]*48

i = 0

for line in f.readlines():
    if i < 48:
        oligo[i] = line.strip()[2:]
    else:
        hexamer[i - 48] = line.strip()

    i+=1

f = io.open("{}/barcode_1_map.txt".format(dir), "w")
i = 0

while i < 48:
    f.write("{o}\t{h}\n".format(o=oligo[i], h=hexamer[i]))

    i += 1