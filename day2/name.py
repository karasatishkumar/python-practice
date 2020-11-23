name = input("Please enter your name : ") #arvindhan

print("%s" %(name[:-1] + name[-1].upper()))
print("%s" %(name[0].upper() + name[1:-1] + name[-1].upper()))
print("%s" %(name[0:3].upper() + name[3:-3] + name[-3:].upper()))
print("%s" %(name[:5]))
print("%s-%s" %(name[0:4], name[4:].upper()))