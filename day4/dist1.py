#Given:
data = "five zero eight nine"

#Expected:
#5089

map = {
    "five":5,
    "zero":0,
    "eight":8,
    "nine":9
}

result = [map[e] for e in data.split()]
print(result)
