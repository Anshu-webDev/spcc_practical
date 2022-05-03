f = open("code.py", "r")
line = f.readlines()

for i in range(len(line)):
    line[i] = line[i][:-1]

print("Code Before Optimization:")
for element in line: 
    print(element)

# Variable replacement
vars = {}
for i in range(len(line)):
    if (line[i][2:].isnumeric()):
        vars[line[i][0]] = line[i].split('=')[1]

for i in range(len(line)-2):
    for key in vars:
        if key in line[i+2]:
            line[i+2] = line[i+2].replace(key, vars[key]) 

for element in list(line):
    if element.split('=')[0] in vars.keys():
        line.remove(element)

# Variable Propagation
newEq = ""
delElem = ""
replaceElem = ""
for element in list(line):
    if (element.split('=')[0].isalpha() and element.split('=')[1].isalpha()):
        line.remove(element)
        delElem = element.split('=')[0]
        replaceElem = element.split('=')[1]

    newEq = list(element.split('=')[1])
    rhs = element.split("=")[0] + '='
    if delElem in newEq:
        newEq[newEq.index(delElem)] = replaceElem
        line.remove(element)
        element = rhs + ''.join([str(e) for e in newEq]) 
        line.append(element)

# Strength Reduction
for element in list(line):
    newEq = ""
    Eq=list(element.split("=")[1])
    rhs=element.split('=')[0]+'='
    if '*' in Eq:
        mulIndex = Eq.index('*')
        for i in range(int(Eq[mulIndex-1])):
            newEq += Eq[int(mulIndex)+1] + "+"
        newEq = newEq[:-1]
        line.remove(element)
        element = rhs + ''.join(newEq)
        line.append(element)

# Dead Code Elimination
value = ''
newEq = []
for element in list(line):
    Eq=element.split()
    if 'if' in Eq:
        value = line[line.index(element) - 1].split('=')[1]
        newEq = Eq[1:]
        OtherValue = line[line.index(element)].split('==')[1]
        if value == OtherValue:
            break
        else:
            line.remove(line[line.index(element) + 1])
            line.remove(element)

line.reverse()

print("\nCode After Optimization")
for element in line:
    print(element)