#Task2:-
studlst = [
           "ravi-blr-10,20,30",
           "hari-mys-40,50,60",
           "guru-gdg-70,80,90",
           "mahi-hub-50,60,30"
          ]
#Expected:-
#newlst =["ravi-60", "hari-150", "guru-240", "mahi-140"]

newlst = []
for cursor in studlst:
    name, city,mark = cursor.split("-")
    mark = sum([int(e) for e in mark.split(",")])
    newlst.append(name + "-" + str(mark) )

print(newlst)


