def cg(code):
    c=code[0]
    d={}
    c1=c.split("=")
    op={'+':'ADD','-':'SUB'}
    j=1
    f=""
    for i in c1[1]:
        if i in op.keys():
            f=i
            continue
        print("MOV"+ " " + "R"+str(j) + "," + i)
        j=j+1
    print(op[f]+" "+"R1"+","+"R2")
    d[c1[0]]="R1"
    for w in code[1:]:
        ch=0
        mm=0
        r=[]
        r=w.split("=")
        if len(r[1])==1:
            print("MOV"+" "+r[1]+","+d[r[1]])
        else:
          for t in r[1]:
            if(r[1][0] in d.keys() and r[1][2] in d.keys()):
              f=r[1][1]
              m="R1"
              ch=1
              mm=1
              break
            if(t in op.keys()):
                f=t
                continue
            if(t in d.keys()):
                ch=1
                if(r[1].index(t)==0):
                  ind=2
                else:
                  ind=0
                print("MOV"+" "+" "+"R2"+","+r[1][ind])
                m=d[t]
          if(ch==0 and mm!=1):
            print("MOV"+" "+"R1"+","+r[1][0])
            print("MOV"+" "+"R2"+","+r[1][2])
            m="R1"
          print(op[f]+" "+m+","+"R2")
        d[r[0]]="R1"
code=[]
n=int(input("ENTER NUMBER OF LINES:"))
for y in range(n):
    cc=input('ENTER LINE:')
    code.append(cc)
cg(code)

'''
i/p:
ENTER NUMBER OF LINES:1
ENTER LINE:a=b+c

o/p:
MOV R1,b
MOV R2,c
ADD R1,R2
'''
