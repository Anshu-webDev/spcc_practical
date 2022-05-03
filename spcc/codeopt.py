def cpo(code):
  print("YOUR CODE WAS:")
  print("------------------------")
  for m in code:
    print(m)
  d={}
  for i in code:
      i=i.split("=")
      if(i[1].isnumeric() or i[1].replace('.', '', 1).isdigit()):
             d[i[0]]=i[1]
  ans=[]
  for i in code:
      i=i.split("=")
      for j in i[1].split(" "):
        if(j in d.keys()):
          i[1]=i[1].replace(j,d[j])
      s=""
      s=str(i[0])+"="+str(eval(i[1]))
      ans.append(s)
  print("OPTIMIZED CODE:")
  print("------------------")
  for c in ans:
    print(c)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def cf(code):
  print("YOUR CODE WAS:")
  print("------------------------")
  print(code)
  o=["=","*","+","-","/","**"]
  a=[]
  ans=code.split(" ")
  for i in ans:
    if not i.isalpha() and i not in o:
      a.append(eval(i))
    else:
      a.append(i)
  a=list(map(str,a))
  print("OPTIMIZED CODE:")
  print("------------------")
  print("".join(a))
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def spcc(code):
  print("YOUR CODE WAS:")
  print("------------------------")
  for m in code:
    print(m)
  s=[]
  e=[]
  k=[]
  j={}
  ans=[]
  for i in code:
    i=i.split("=")
    if(i[1] not in e):
      e.append(i[1])
      s.append(i[0])
    else:
      k.append(i[0])
      rep=e.index(i[1])
      j[i[0]]=s[rep]
  for i in e:
    for u in k:
      if u in i.split(" "):
        i=i.replace(u,j[u])
    ans.append(i)
  z=zip(s,ans)
  print("OPTIMIZED CODE:")
  print("------------------")
  for x,y in z:
    print(str(x)+"="+str(y))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
n=int(input("Number of lines:"))
code=[]
print("-- MENU----")
print("1.CONSTANT FOLDING")
print("2.CONSTANT PROPAGATION")
print("3.COMMON SUBEXPRSSION ELIMINATION")
print("----------------------------------------------")
ch=int(input("Enter your choice:"))
if(ch==1):
  code=input("ENTER A CODE LINE:")
  cf(code)
if(ch==2):
  for t in range(n):
         code.append(input("Enter line:"))
  cpo(code)
if(ch==3):
  for t in range(n):
         code.append(input("Enter line:"))
  spcc(code)


