data = "this is new way to do things"

dataarr = data.split()

print("%s" %(dataarr[0]))
print("%s" %(dataarr[-1]))
print("%s" %(dataarr[0] [-1]))
print("%s" %(dataarr[-1] [:4]))

data = "north-10-south-20-east-30-west-40"

dataarr = data.split("-")

print("%s" %(dataarr[::2]))

data="15-aug-1947 10:30:45"

dataarr = data.split()

print("Date : %s" %(dataarr[0]))
print("Time : %s" %(dataarr[-1]))

dataarr = dataarr[-1].split(":")

print("Hour :%s" %(dataarr[0]))
print("Min : %s" %(dataarr[1]))
print("Sec : %s" %(dataarr[2]))

data="arun-blr-10,20,30,40"

dataarr = data.split("-")

dataarr = dataarr[-1].split(",")

sum = int(dataarr[0]) + int(dataarr[1]) + int(dataarr[2]) + int(dataarr[3])
print("Sum : %s" %(sum))