class Base:
   def __init__(self,a):
      print("Base Ctor")
      self.a = a
   def show(self):
      print("BASE... SHOW")
      print("A = ",self.a)