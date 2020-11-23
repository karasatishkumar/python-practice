class ZeroError(Exception):
    def __init__(self, mesg):
        Exception.__init__(self)
        self.mesg = mesg

    def __str__(self):  # equivalent - toString() of java
        return self.mesg


try:
    num = input("Enter a number : ")
    num = int(num)
    if num == 0:
        raise ZeroError("num cannot be ZERO.....")
    res = num * num

except ValueError as e1:
    print("Action1", e1)
except ZeroError as e2:
    print("Action2", e2)
except Exception as e3:
    print(e3)
else:
    print("ANSWer = ", res)
finally:
    print("Clean")