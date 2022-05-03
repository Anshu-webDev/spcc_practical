import pandas as pd
f = open("sample4.asm", "r")
f1 = open("OUTPUT_Pass1.asm", "w")
f2 = open("OUTPUT_Pass2.asm", "w")
MDT = {"INDEX": [], "CARD": []}
MNT = {"INDEX": [], "MACRO_NAME": [], "POINTER(MDT)": []}
ALA = {"ARGUMENTS": []}
MDTC = 1
MNTC = 1
flag = False
print("\n\n---------------------------Pass1----------------------------")
for x in f:
    temp = x.strip()
    x = temp.split(" ")
    if x[0] == "MACRO":
        MNT["INDEX"].append(MNTC)
        MNT["MACRO_NAME"].append(x[1])
        MNT["POINTER(MDT)"].append(MDTC)
        MNTC += 1
        Argument_list = []
        if "," in x[2]:
            Argument_list = x[2].split(",")
        else:
            Argument_list.append(x[2])
        ALA["ARGUMENTS"] = Argument_list
        print("\nMACRO {} ALA".format(x[1]))
        print(pd.DataFrame(ALA))
        MDT["INDEX"].append(MDTC)
        MDT["CARD"].append(" ".join(x[1:]))
        MDTC += 1
        flag = True
    elif flag == True:
        for i in range(0, len(Argument_list)):
            if Argument_list[i] in temp:
                temp = temp.replace(Argument_list[i], "#"+str(i))
        MDT["INDEX"].append(MDTC)
        MDT["CARD"].append(temp)
        MDTC += 1
    else:
        if len(temp) > 0:
            f1.write(temp)
            f1.write('\n')
    if x[0] == "ENDM":
        flag = False
print("\nMNT : ")
df = pd.DataFrame(MNT)
print(df.to_string(index=False))
print("\nMDT : ")
df = pd.DataFrame(MDT)
print(df.to_string(index=False))
print("\nPass1 Source Card Copy is Generated Successfully.\n")
f1 = open("OUTPUT_Pass1.asm", "r")
print("Pass1 Source Card Copy:")
for x in f1:
    x = x.strip()
    print(x)

print("\n\n---------------------------Pass2----------------------------\n")
f1 = open("OUTPUT_Pass1.asm", "r")
for x in f1:
    temp = x.strip()
    x = temp.split(" ")
    if x[0] in MNT["MACRO_NAME"]:
        Argument_list = []
        if "," in x[1]:
            Argument_list = x[1].split(",")
        else:
            Argument_list.append(x[1])
        MDTP = MNT["POINTER(MDT)"][MNT["MACRO_NAME"].index(x[0])]
        while MDT["CARD"][MDTP] != "ENDM":
            y = MDT["CARD"][MDTP]
            if "#" in y:
                index = int(y[y.index("#")+1])
                y = y.replace("#"+str(index), Argument_list[index])
            f2.write(y)
            f2.write('\n')
            MDTP += 1
    else:
        if len(temp) > 0:
            f2.write(temp)
            f2.write('\n')
print("Pass2 Expanded Source File is Generated Successfully.\n")
f2 = open("OUTPUT_Pass2.asm", "r")
print("Pass2 Expanded Source File : ")
for x in f2:
    x = x.strip()
    print(x)


# asm = []
# with open("sample4.asm") as f:
#     asm = f.readlines()

# MDT = []
# MNT = []
# ALA = []

# for line in range(len(asm)):
#     if "MACRO" in asm[line]:
#         MNT.append((str(len(MNT)), asm[line].split()[1], str(len(MDT))))
#         for i in asm[line].split()[2:]:
#             ALA.append((str(len(ALA)), i))
#         temp = ""
#         while True:
#             line += 1
#             if "ENDM" in asm[line]:
#                 temp += asm[line]
#                 break
#             temp += asm[line]
#         MDT.append((str(len(MDT)), temp))

# print(MDT)
# print(MNT)
# print(ALA)
