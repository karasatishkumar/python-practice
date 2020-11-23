
#f1("manish sharma") - sharma
#f2("manish sharma") - ms
#f3("arun-blr-10,20,30") - ["10", "20", "30"]
#f4("arun-blr-10,20,30") - [10, 20, 30]
#f5("arun-blr-10,20,30") - 60



f = lambda x : x.split()[0]
print("%s" %(f("manish sharma")))

f = lambda x : x.split()[0][0] + x.split()[1][0]
print("%s" %(f("manish sharma")))

f = lambda x : x.split("-")[-1].split(",")
print("%s" %(f("arun-blr-10,20,30")))

f = lambda x : [int(e) for e in x.split("-")[-1].split(",")]
print("%s" %(f("arun-blr-10,20,30")))

f = lambda x : sum([int(e) for e in x.split("-")[-1].split(",")])
print("%s" %(f("arun-blr-10,20,30")))