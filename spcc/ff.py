import re
firsts = {}
follows = {}
prods = {}
n = int(input("Enter number of production rules: "))
class Prod:
    ter = None
    def __init__(self, p) -> None:
        _, p = p.split("->")
        p = p.split("|") 
        self.rules = p
        self.ter = _ 
    def __str__(self) -> str:
        return f"{self.ter} {self.rules}"
def CheckFirst(prod: Prod):
    first = set()
    for rule in prod.rules:
        if not rule[0].isupper():
            first.add(rule[0])
        elif '@' == rule:
            first.add('@')
        else:
            for idx, Y in enumerate(rule):
                if Y == "'":
                    continue
                if idx+1 < len(rule) and rule[idx+1] == "'":
                    Y+= "'" 
                if Y.isupper():
                    firstY = CheckFirst(prods[Y])
                    for i in firstY:
                        first.add(i) 
                    if not "@" in firstY:
                        break
                if idx != len(rule) - 1:
                    first.remove("@")
    return first               
def checkFollow(prod: Prod):
  
  if prod.ter == 'S':
    return set(["$"])
  
  follow = set()

  regex = r"[A-B]"
  for rule in prod.rules:
    matches = re.finditer(regex, rule, re.MULTILINE)
    
    for i in matches:
      ter = i[0]
      # A -> aBb
      if i.span()[0] != 0 and i.span()[1] != len(rule):
        temp = firsts[ter]
        for f in temp:
          if "@" == f:
            continue 
          follow.add(f)
      # A -> aB || A -> aBb
      elif i.span()[0] != 0:
        temp = checkFollow(prods[ter])
        for f in temp:
          follow.add(f)
  return follow
for i in range(n):
    prod = input("Enter prod rule: ")
    prods[prod.split('->')[0]]=(Prod(prod))
for ter, prod in prods.items():
    firsts[ter] = CheckFirst(prod)
    follows[ter] = checkFollow(prod)
print(f"_"*15)
for ter, rule in firsts.items():
  print(f"{ter} :")
  print(rule)
print(f"_"*15)
for ter, rule in follows.items():
  print(f"{ter} :")
  print(rule)
