asm = []
with open("sample.asm") as f:
    asm = f.readlines()

MDT = []
MNT = []
ALA = []

for line in range(len(asm)):
    if "macro" in asm[line]:
        MNT.append((str(len(MNT)), asm[line].split()[1], str(len(MDT))))
        for i in asm[line].split()[2:]: 
            ALA.append((str(len(ALA)), i))
        temp = "" + asm[line][6:]
        while True:
            line+=1
            if "endm" in asm[line]:
                temp += asm[line]
                break
            temp += asm[line]
        MDT.append((str(len(MDT)), temp))

print("Pass1: ")
print(MDT)
print(MNT)
print(ALA)

print()
MNTList = [i[1] for i in MNT]
print("Pass 2: ")
for i in asm:
  if len(i.split()) > 0:
    # print(i.split()[0])
    if i.split()[0] in MNTList:
      print(i)
      defination : str = MDT[ int(MNT[MNTList.index(i.split()[0])][2]) ][1] 
      argNum = 0
      arg = dict()
      for a in i.split()[1:]:
        arg[defination.split()[argNum+1]] =  a
        argNum += 1
      for j in defination.splitlines()[1:]:
        for k in j.split():
          if k in arg:
            j = j.replace(k, arg[k])
        print(j)
    else:
      print(i, end="")
