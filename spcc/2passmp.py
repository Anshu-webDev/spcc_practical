def loader(ins):
  mdt=[]
  mnt=[]
  ala=[]
  esource=[]
  i=0
  temp=0
  mindex=[]
  mi=0
  while(i<len(ins)):
   if ins[i]=="MACRO":
      dummy=[]
      i=i+1
      mnt.append(ins[i][:ins[i].index(" ")])
      mindex.append(mi)
      mi=mi+1
      kj=[]
      kj=ins[i][ins[i].index(" ")+1:].split(",")
      ala.append(kj)
      i=i+1
      while(ins[i]!="MEND"):
        kj1=ins[i].split(" ")
        for ff in kj1[1].split(","):
         # print(ff)
          if(ff in kj):
            #print(ff)
            ins[i]=ins[i].replace(ff,str(kj.index(ff)+1))
           # print(ins[i])
        dummy.append(ins[i])
        i=i+1
      dummy.append("MEND")
      mdt.append(dummy)
      i=i+1
      temp=i
   else:
      i=i+1
  print("-- PASS 1 RESULTS ---")
  print("-- MDT --")
  for a in mdt:
    print(a)
  print("-- MNT --")
  for b in zip(mnt,mindex):
    print(b)
  print("--- ALA ---")
  print(ala)
  print("-- PASS 2--")
  j=0
  ''' for com in ins[:temp]:
    esource.append(com)'''
  for com in ins[temp:]:
    com1=com.split(" ")
    if com1[0] in mnt: 
          cc=com1[1].split(",")        
          j=mnt.index(com1[0])
          for f in mdt[j]:
             f1=f.split(" ")
             if(len(f1)>1):
               f2=f1[1].split(",")
               for ii in f2:
                    f=f.replace(ii,str(cc[int(ii)-1]))
             
             esource.append(f)
    else:
        esource.append(com)
  for res in esource:
      print(res)

n=int(input("Enter no of ins:"))
ins=[]
i=0
while(i<n):
  ins.append(input("Enter ins:"))
  i=i+1
loader(ins)

