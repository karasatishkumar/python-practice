from Base import *
class Derived(Base):
   def __init__(self,a,b):
      Base.__init__(self,a)     # ctor cascading
      print("Derived Ctor")
      self.b = b
   def foo(self):
      print("DERIVED... foo")
      print("B = ",self.b)
ob1 = Derived(10,20)