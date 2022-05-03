
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
print("COMMON SUBEXPRSSION ELIMINATION")
print("----------------------------------------------")

for t in range(n):
    code.append(input("Enter line:"))
spcc(code)

'''
input:-
Number of lines:4
COMMON SUBEXPRSSION ELIMINATION
----------------------------------------------
Enter line:s1=4 * i
Enter line:s2=3 + j
Enter line:s3=4 * i
Enter line:s4=s1 + s3 * 4
'''