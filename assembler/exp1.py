asm = []

with open('sample.asm') as f:
  for i in f.readlines():
    asm.append(i.split())

oprands = ["START", "USING", "DC", "DS", "END", "A", "L", "ST"]
Poprands = ["START", "USING", "L", "END"]

mot = []
pot = []
st = []
lt = []
bt = []
lc = 0


def newLC(op, opc):
  if op in Poprands:
    return 0
  else:
    return 2 if opc[0] == "H" else 4

def updateTables(label, oprand, opcode, lc):
  if oprand not in Poprands or oprand == "L":
    mot.append((oprand, "", "01", "RX"))
  else:
    pot.append((oprand, ""))
  
  if "'" in opcode:
    lt.append((opcode[1:], str(lc), str(newLC(oprand, opcode))))
  if label != " ":
    st.append((label+"b"*(8-len(label)), str(lc), str(len(label))))

  if oprand == "USING":
    _,num = opcode.split(",")
    for i in range(16):
      if int(num) == i:
        bt.append((str(i), "Y", "00"))
      else:
        bt.append((str(i), "N", "00"))



for i in asm:
  if i[0] in oprands:
    oprand = i[0]
    label = " "
  else:
    label = i[0]
    oprand = i[1]
  opcode = i[-1]
  if oprand == "END" or oprand == "START":
    opcode = " "

  lc += newLC(oprand, opcode)

  updateTables(label, oprand, opcode, lc)

  print(label, oprand, opcode, lc)
print()

print("_" * 20)
print("Pass1:")
print("="*10) 
print("MOT:")
for i in mot:
  if i[0] in "DS DC":
    continue
  print(" ".join(i))
print("_"*10)

print("POT:") 
for i in pot:
  print(" ".join(i))
print("_"*10)

print("LT:")
for i in lt:
  print(" ".join(i))
print("_"*10)

print("ST:")
for i in st:
  print(" ".join(i))


print("_" * 20)
print("Pass2:")
print("="*10) 
print("MOT:")
for i in mot:
  print(" ".join(i))
print("_"*10)

print("POT:") 
for i in pot:
  print(" ".join(i))
print("_"*10)

print("LT:")
for i in lt:
  print(" ".join(i))
print("_"*10)

print("ST:")
for i in st:
  print(" ".join(i))
print("_"*10)

print("BT:")
for i in bt:
  print(" ".join(i))
