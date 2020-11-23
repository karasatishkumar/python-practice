
f1 = open("data.txt", "w")
f1.write("arun works around this\n")
f1.write("data and also fine")
f1.close()

def words_starts_with(fname, alpha):
    f1 = open(fname,"r")
    lines = [e.strip("\n")for e in f1.readlines()]
    words = []
    for cursor in lines:
        w = [e for e in cursor.split() if e[0] == alpha]
        words.extend(w)
    f1.close()
    return words


reslst = words_starts_with("data.txt", "a")
print(reslst)