f = open('data.txt')
lines = f.readlines()
print(lines)
for line in lines:
    print(line,end='')
