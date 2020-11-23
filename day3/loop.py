datlst = [
          "10-nov-2020",
          "15-dec-2010",
          "5-apr-1998",
          "31-dec-1990"
         ]

for cursor in datlst:
    print("%s - %s" %(cursor.split("-")[1], cursor.split("-")[1][0].upper()))

res = [cursor.split("-")[1] + " - " + cursor.split("-")[1][0].upper() for cursor in datlst]
print(res)