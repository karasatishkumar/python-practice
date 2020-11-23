class Student:

    def __init__(self, name, mark):  # parameterized CTOR
        self.name = name
        self.mark = [int(e) for e in mark.split(",")]
        self.total = 0

    def findtotal(self):
        self.total = sum(self.mark)

    def show(self):
        print("Marks : %s" %(self.mark))
        print("Total : %s" % (self.total))


st1 = Student("ravi", "10,20,30")
print(st1.findtotal())
st1.show()  # name = ravi

