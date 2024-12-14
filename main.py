import sys # reqierd for arguments
print("#mark")
args=list(sys.argv[0:]) # put the arguments into a list
if args[0][0]!="-":args.pop(0)
while args: # the argument loop
 #if args[0]=="-p":print("placeholder")
 args.pop(0)
