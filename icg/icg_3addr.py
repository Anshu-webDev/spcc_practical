from tabulate import tabulate
def threeaddr(s):
  l=s.split(" ")
  l=l[2:]

  op=['+','-','*','/','^']
  arg1=[]
  arg2=[]
  res=[]
  oper=[]
  n=(len(l))//2
  if(l[n] not in op):
    while(l[n] not in op):
      n=n-1
  p1=l[:n]
  p2=l[n+1:]
  ind=1
 
  if(len(l)==3):
    oper.append(l[n])
    arg1.append(l[0])
    arg2.append(l[2])
    res.append("t"+str(ind))
    oper.append("=")
    arg1.append(s[0])
    arg2.append("t"+str(ind))
    res.append("t"+str(ind+1))
    ans=[]
    z1=zip(oper,arg1,arg2,res)
    for a1,a2,a3,a4 in list(z1):
      aq=[]
      aq.append(a1)
      aq.append(a2)
      aq.append(a3)
      aq.append(a4)
      ans.append(aq)
    print("QUADRAPLE TABLE:")
    print(tabulate(ans, headers=["OPERATORS","ARG 1","ARG 2","RESULT"],tablefmt='orgtbl'))
  else:
    m=0
    for i in p1:
       if(i[0] in op and len(i)>1):
            oper.append("unary"+i[0])
            arg1.append(i[1])
            arg2.append("nill")
            res.append("t"+str(ind))
            ind=ind+1
       if(i in op and len(i)==1):
            
            oper.append(i)
            arg1.append(p1[m-1])
            #print(p1.index(i)+1)
            arg2.append(p1[m+1])
            res.append("t"+str(ind))
            my="t"+str(ind)
            ind=ind+1
       m=m+1
    j=0
    for i in p2:
        if(i[0] in op and len(i)>1):
          
           oper.append("unary"+i[0])
           arg1.append(i[1])
           arg2.append("nill")
           res.append("t"+str(ind))
           ind=ind+1
        if(i in op and len(i)==1):
            
            oper.append(i)
            arg1.append(p2[j-1])
            arg2.append(p2[j+1]) 
            res.append("t"+str(ind))
            you="t"+str(ind)
            ind=ind+1
        j=j+1
    oper.append(l[n])
    arg1.append(my)
    arg2.append(you)
    res.append("t"+str(ind))
    oper.append("=")
    arg1.append(s[0])
    arg2.append("t"+str(ind))
    res.append("t"+str(ind+1))
    z=zip(oper,arg1,arg2,res)
    ans=[]
    for a1,a2,a3,a4 in list(z):
      aq=[]
      aq.append(a1)
      aq.append(a2)
      aq.append(a3)
      aq.append(a4)
      ans.append(aq)
    print("QUADRAPLE TABLE:")
    print(tabulate(ans, headers=["OPERATORS","ARG 1","ARG 2","RESULT"],tablefmt='orgtbl'))
   
    # print(a1,a2,a3,a4)
s=input("Enter code:")
threeaddr(s)

'''
Enter code:a = b + c
QUADRAPLE TABLE:
| OPERATORS   | ARG 1   | ARG 2   | RESULT   |
|-------------+---------+---------+----------|
| +           | b       | c       | t1       |
| =           | a       | t1      | t2       |
'''
