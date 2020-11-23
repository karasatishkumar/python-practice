f1 = open("data.txt","w")
f1.write("ravi-blr-10,20,30\n")
f1.write("hari-chn-40,50,60\n")
f1.write("kala-hyd-43,65,34\n")
f1.write("manu-mys-43,23,76")
f1.close()

f1 = open("data.txt","r")
etab = {}
for cursor in f1:
    data = cursor.strip("\n").split("-")
    mark = sum([int(e) for e in data[-1].split(",")])
    etab[data[0]] = mark
print(etab)
