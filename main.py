import sys
p=m=l=instr=sinstr=sp=0;ts=[];s1=[];s2=[];os=[];ins=[];i="";s=[s1,s2];c="""'Hi'@#"""
arg=sys.argv[0::];d=0
while arg[0][0]!="-":
 arg.pop(0)
 if arg==[]:break
while arg!=[]:
 if arg[0]=="-d":d=1
 elif arg[0]=="-i":i=arg[1];arg.pop(0)
 arg.pop(0)
if i!="":
 for inp in i:ins.append(inp)
while p<len(c):
 if c[p]=="#":instr+=1;break
 elif c[p]=="'":m=1;instr+=1
 elif m==1:
  while c[p]!="'":ts.append(c[p]);p+=1
  if c[p]=="'":
   ts.reverse()
   while len(ts)>1:ts.append(str(ts.pop())+str(ts.pop()))
  s[sp].append(ts[0]);ts.pop();m=0;instr+=1
 elif c[p]=="@":s[sp].reverse();print(s[sp][0],end="");s[sp].reverse();instr+=1
 elif c[p]=="!":s.pop();instr+=1
 elif c[p]=="_":
  if len(ins)>0:s[sp].append(ins[0]);ins.pop(0);instr+=1
  else:print("\nEOI reached",end="");break
 elif c[p]=="|":
  instr+=1
  while c[p]!="|":p+=1
 elif c[p]=="i":
  instr+=1
  if c[p+1]=="[":
   p+=2
   while c[p]!="]":
    if c[p]=="_":s[sp].append(int(ins[0]));ins.pop(0);instr+=1;p+=1
    else:s[sp].append(int(c[p]));p+=1
 elif c[p]=="*":
  if sp==0:sp=1
  elif sp==1:sp=0
 elif c[p]=="?":
  if c[p+1]=="b":
   if s1==s2:p+=3
   else:
    while c[p]!="]":p+=1
 p+=1
 if p==len(c):
  p=0;sinstr=instr
  if l==0:instr=0
if instr!=0:sinstr=instr
if d==1:print("\n"+c,s1,s2,i,sinstr,arg,"instructions",end="")
else:pass