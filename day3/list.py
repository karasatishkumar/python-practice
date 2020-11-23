plst = [
    "dvd-  hw  -  20  ",
    "   mon - hw - 40",
    "prn - hw - 50",
    "win - sw-50",
    "office - sw - 10",
    "keb-hw-10"
]
totallist=[]
hwlist=[]
swlist=[]
for cursor in plst:
    cursor = cursor.replace(" ","")
    str1,str2,count=cursor.split("-")
    if str2=="hw":
        hwlist.append(str1)
    else:
        swlist.append(str1)
print(hwlist)
print(swlist)