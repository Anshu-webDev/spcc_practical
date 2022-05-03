def lex(code):
  keyword=["int","char","float","string","cout","cin"]
  op=["+","-","*","/","(",")","[","]","{","}",">>","<<",",",";","="]
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
    print("--------------------------------------------------------------------")
co=int(input("ENTER NUMBER OF LINES:"))
code=[]
for u in range(co):
  c=input("ENTER LINE:")
  code.append(c)
print("--------------------------------------------------------------------")
lex(code)

'''
Input:
ENTER NUMBER OF LINES:1
ENTER LINE:int a = hello + 3.2 ;

--------------------------------------------------------------------
output:-

YOUR CODE IS:
int a = hello + 3.2 ;
----------------------------------------------------------------
Keyword: int
Identifier: a
Operator: =
Identifier: hello
Operator: +
Identifier: 3.2
Operator: ;
'''
