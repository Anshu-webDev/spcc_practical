def lex(code):
  keyword=["int","char","float","string","cout","cin"]
  op=["+","-","*","/","(",")","[","]","{","}",">>","<<",",",";","="]
  num=["0","1","2","3","4","5","6","7","8","9"]
  print("YOUR CODE IS:")
  for command in code:
    print(command)
  print("----------------------------------------------------------------")
  for command in code:
    command=command.split(" ")
    for j in command:
      if j in keyword:
        print("Keyword:",j)
      elif j in op:
        print("Operator:",j)
      elif j.isdigit():
        print("Number:",j)
      else:
        print("Identifier:",j)
co=int(input("ENTER NUMBER OF LINES:"))
code=[]
for u in range(co):
  c=input("ENTER LINE:")
  code.append(c)
print("--------------------------------------------------------------------")
lex(code)

       
