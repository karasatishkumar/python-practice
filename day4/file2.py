f1 = open("new.txt", "w")
f1.write("hello world of unix\n")
f1.write("lookz simple but not as it is\n")
f1.write("now the new way is there\n")
f1.write("bye for now")
f1.close()

f1 = open("new.txt", "r")
total = 0
for cursor in f1:
    cursor = cursor.strip("\n")
    print("%s = %s" %(cursor, len(cursor.strip())))
    total += len(cursor.strip())
print("%s = %s" %("Total", total))
f1.close();