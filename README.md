# python-practice

Welcome to the training


1) in brief about current role
2) programming  - yes/no
3) why python ? - for Automation    
                - for ML
                - for API 
                - others


Object BAsed lang     - develop fns.... using classes  
Object Oriented Lang  - develop classes

Object Oriented Terms:-
=======================
class       - table
object      - row
data member - columns
methods     - operations
mutator     - write/overwrite
non-mut     - readonly 
predicate   - returns True/False
messaging   - object.methodname()

Refvar = new CLASSNAME() # allocate memory
                         # call a ctor
                         # returns the address

Convert user story into a OBJECT ORIENTED MESSAGING
data entry operator has collected some info like this
1234 prasad sb  25000
1235 bhoomika rd 15000  fill these to table

acc1 = new Account()
acc2 = new Account()

acc1.fill(1234,"prasad","sb", 25000)
acc2.fill(1235,"bhoomika","rd",15000)

acc1.withdraw(2000)

if acc2.isSavings()
{
  acc1.report()
}
else
{
  acc1.show()
} 

#as per previous understading - prasad is "acc1"
                              - bhoomika is "acc2"
#How to check the balance of bhoomika
object.methodname()
acc2.checkbal()    
acc2.withdraw(500)
acc1.deposit(200)


------------------------------------------------------------------

in python ready made class - list class
methods  - append(ITEM)
         - sort()
         - reverse()
         - pop(INDEX)

I have visited diff cities like blr, chn, hyd, tvm

i have my frnds - hari guru raja john

city = new list()
frnds = new list()
city.append("blr")
city.append("chn")
city.append("hyd")
city.append("tvm")

frnds.append("hari")
frnds.append("guru")
frnds.append("raja")
frnds.append("john")
frnds.sort()

city.reverse()

Key take-away:-
----------------
>> class/object/datamem/methods/
>> mutator/nonmut/predicate
>> Convert user story into Object ORiented MEssage


Memory Layout:-
===============
code   - source code 
data   - fixed - global variable - shrink & expand - no
stack  - fixed - local variable  - shrink & expand - no
heap   - Dynamic - any variable  - shrink & Expand - yes

Note:
 In Python programmers will have zero control over stack & data
           programmers will have control only on HEAP AREA


REferences:-
============
name="amar"    #name is referecnce     - in the Book keeper
               #"amar" is string object- in the HEAP

               

Book Keeper:-  # namespace/symboltable/package
==============
>> records variable/funct/class/module 
>> ACTIVE COUNT of variable/function/class/libname
>> define a variable   - register var into book keeper
>> goes out of scope   - name will be deleted
>> display the book keeper -  dir()


Deep Dive of Objects:-
=======================
>>Every object will have - data/unique-id/type/refcount

a=10    

print(num)         #   10
print(type(num))   #  <class "int">
print(id(num))     #  65524

import sys

print(sys.getrefcount(num))   # ?
print(sys.getsizeof(num))     # ?

Copy object in python:-
=======================
a=10
res=a    # this is called as SHALLOW COPY

NOTE: default copy in python is SHALLOW COPY


Reference count:-
=================
>> no of dependents on the value 
>> default value  = 1
>> ref count increases = copy the variable 
>> ref count decreases = var goes out of scope


Data structures :-
==================

                    Data Structures
                           |
           ----------------------------------
          |                                  |
      Im-Mutable                         Mutable                       
      Constants                          Non-Constants
      readonly                           read-write

      int                                bytearray
      float                              list
      str                                set
      bytes                              dict
      bool
      complex
      NoneType
      tuple
      frozenset
      
age=36
ht=5.5
name='vijay'      # Single quoted - one-line data 
name="vijay"      # Dobule Quoted - one-line data 
name='''vijay'''  # Triple quoted - one/multiline data
isSavings=Ture    # boolean - first letter is CAPITAL
isSavings=False
result = None     # define a NULL value in python
weeks =("sun","mon","tue","wed","thu","fri","sat")  # tuple 

grplst = ["alpha", "beta", "delta"]      # list
cset = {"blr","chn","hyd","mum"}         # Set
atab = {
         "kar" : "blr",                  # dict
         "mah" : "mum",
         "tn"  : "chn"
       }

FAQ on data structres:-
-----------------------
what is the diff b/w str & bytes ? str - unicode
                                   bytes - ASCII

What is the diff b/w tuple & list ? tuple - im-mutable
                                    list  - mutable

What is the diff b/w set & list ?   list - can have duplicates
                                    set  - cannot have duplicates


Cafeteria:-
============
>> 20 seater capacity
>> there is no cleaning staff

Memory LEkage:-
===============
>> we have a free space but it has NOT CLEANED
>> Solution - we need house keepers 

Garbage collector:- (GC)
===================
>> Memory House Keepers - who cleans un-used memory
>> python has as GC installed - so there is no MEMORY LEAKAGE             

=================================================================


                        python
                          |
          ---------------------------------
         |                                 |
       2.x                               3.x
 
      2.4                                3.5
      2.6                                3.6
      2.7                                3.7
                                         3.8
(31/dec/2019)                            3.9    (latest)


python2			python3
--------		-------
print "hello"     	print("Hello")
xrange()          	range()



S/w utils / tools for developers:-
----------------------------------
1) compiler
2) text editor
3) debugger
4) help system
5) others

IDE:-
======
pycharm   - we need to install
VScode    - we need to install
spyder    - comes by default with anaconda distr
          - jupyter notebook
pyDev     - we need to install 
IDLE      - comes by default with python.org distr
atom      - we need to install 
sublime   - we need to install 


Websites for python developers:-
================================
1) python.org      - to download -the complier
   anaconda.com    - to download -for datascience
   activestate.com - to download -for unix/linux/macos

2) online help   - www.docs.python.org/3

3) coding style  - www.pep8.org

4) library repo  - www.pypi.org

5) Pycharm IDE   - www.jetbrains.com




=================================================================
How to write & Execute in IDE:-
===============================

# my first program
# to add 2 nos

num1 = input("Enter the num1 : ")
num2 = input("Enter the num2 : ")
res = int(num1) + int(num2)
print("RESULT = ",res)


Input statements:-
==================
>> expects the data from keyboard
>> always in the form of strings

age = int(input("Enter u r age : "))
OR
age = input("Enter u r age : ")
age = int(age)



Output statements:-
===================
a=10
b=20
c=a+b

prin(c)
print("result = ",c)       # prefered
print("result = "+str(c))  # not a prefered way

print("sum of %s and %s is %s" %(a,b,c))         # prefered way
print("sum of {0} and {1} is {2}".format(a,b,c)) # not used much
print(f"sum of {a} and {b} is {c}")              # not used much   


Task:-
------
Given:-
--------
enter u r first name  :  ravi
enter u r mid name    :  shankar
enter u r last name   :  prasad

Expected:-
-----------
full name = ravi shankar prasad
full name = RAVI-SHANKAR-PRASAD

solution:-
----------
first = input("First name : ")
mid   = input("Mid name   : ")
last  = input("Last name  : ")

res1="%s %s %s" %(first,mid,last)
res2="%s-%s-%s" %(first,mid,last)

print("Full name = ",res1)
print("Full name = ",res2.upper())


str-class:-
===========
>>collection of alpha-numeric
>>im-mutable
>>default char set - unicode
>>also supports    - ASCII via bytes strings
>>index & slicing


1) define a string    :  a="bengaluru"
2) string length      :  res = len(a)
3) indexing           :  first elem  : a[0]
                         last elem   : a[-1]
4) Slicing            :  F4     = a[:4]
                         EF4    = a[4:]
                         L4     = a[-4:]
                         EL4    = a[:-4]
                         EF2-EL2= a[2:-2]
                         Alt    = a[::2] / a[1::2]
                         reverse= a[::-1]
5) search substr      :  if "day" in sent /if "day" not in sent 
                         res = sent.index("day")
                         res = sent.count("day")
6) split              :  flst = data.split(DELIMITER)
7) join               :  STRING = "DELIMITER".join(STRLIST)
8) trim               :  res=data.strip() / lstrip()/ rstrip()
9) replace            :  res=data.replace("-","=")



demo program:-
==============
given    :  harish
expected :  Harish

solution:-
----------- 
name = input("Enter u r name : ")
res = name[0].upper() + name[1:]
print(res)



Task:-
======
given    :  arvindhan

expected :  arvindhaN   - last 1 to upper
            ArvindhaN   - first 1 & last 1 upper
            ARVindHAN   - first 3 & last 3 upper
            arvin       - first 5
            arvi-NDHAN  - first 4 & except first 4

solution:-
----------
res1 = name[:-1] + name[-1].upper() 
res2 = name[0].upper()+ name[1:-1] + name[-1].upper()
res3 = name[:3].upper()+ name[3:-3] + name[-3:].upper()
res4 = name[:5] 
res5 = name[:4] + "-" + name[4:].upper()


search for a substring within a STRING:-
========================================
Ex1:-
-----
>> membership operator  - "in"

sent = "today is a weekday tuesday working day"

res = "work"  in sent
print(res)     # True

res = "wink"  in sent
print(res)     # False

res = "DAY" in sent
print(res)     # False

Ex2:-
-----             1         2         3
        01234567890123456789012345678901234567
sent = "today is a weekday tuesday working day"

res = sent.index("day")  # returns the starting index

print(res)  # 2

res = sent.index(day, 3)  
print(res)  # 15 

Ex3:-
-----
sent = "today is a weekday tuesday working day"

res = sent.count("day")

print(res)  # 4


"day" in sent                           - True/False
sent.index("day") / sent.rindex("day")  - returns index
sent.find("day")                        - returns index
sent.count("day")                       - no of occurances


example for split:-
===================

delimiter   = special char within double quotes
separator   = special char i.e comma - outside double quotes
              (SYNTAX) 

data="10-20-30-40"  # hyphen - delimiter

data="10,20,30,40"  # coma   - delimiter

data="10:20:44"     # colon  - delimiter

data = [10,20,30,40]  # comma - separator

data = ["10-20-30", "50-60-70"]  - hyphen - delimiter 
                                 - comma  - separator

Ex1:-
------
data="15-aug-1947"

flst = data.split("-") 
      
                  0     1       2
print(flst)  # [ "15", "aug", "1947"]
print(flst[0])  # 15
print(flst[-1]) # 1947
print(flst[-2]) # aug

print(flst[0][0])  # 1
print(flst[1][-1]) # g
print(flst[-1][-1]) # 7

print(flst[1][:2])  #au

print(flst[-1][::-1]) # 7491
print(flst[-1][-2:])  # 47
print(flst[1][1:-1])   # u

                     
ex2:-
------
data = "hari-john-rama blr,mys,hub"

major delimiter = WHITE SPACE
minor delimiter = hyphen & comma

flst = data.split()  
                  flst[0]            flst[1]
print(flst)  #  ["hari-john-rama" , "blr,mys,hub"]

alst=flst[0].split("-") 
blst=flst[1].split(",")

print(alst)  ["hari", "john", "rama"]
print(blst)  ["blr", "mys", "hub"]





Task on split:-
================
1)data = "this is new way to do things"

first word = 
last word  = 
first words last char = ?
last words first 4    = ?

solution:-
----------
wlst = data.split()
print(wlst[0])
print(wlst[-1])
print(wlst[0][-1])
print(wlst[-1][:4])

2) data = "north-10-south-20-east-30-west-40"
display only zones 

solution:-
----------
flst = data.split("-")
print(flst[::2])

3)data="15-aug-1947 10:30:45"

display date = ?
display time = ?
display hour = ?
display mins = ?
display secs = ?

solution:-
----------
datestr,timestr = data.split()
print(datestr)
print(timestr)
hour,mins,sec = timestr.split(":")
print(hour)
print(mins)
print(sec)


4) data="arun-blr-10,20,30,40"
find total marks

solution:-
----------
 #"arun-blr-10,20,30,40".split("-")
 #  0        1          2
 #["arun", "blr", "10,20,30,40"]

marks = data.split("-")[2].split(",")
tot = int(marks[0]) + int(marks[1]) + int(marks[2]) + int(marks[3])
prin(tot)



List comprehension:-
=====================
>> set comp         - res = { e for e in datalst } 
>> dict comp        - res = { key:value for e in datalst }
>> generator comp   - res = ( e for e in datalst )


OUTPUTLIST = [ OPERATION_ON_E  for e in INPUTLIST ]

OUTPUTLIST = [ OPERATION_ON_E  for e in INPUTLIST if CONDITION ] 

newmarks = [int(e)  for e in marks ]

ex:-
----
alst = [10,20,30,40,50]

reslst = [ e+1 for e in alst if e>20]  




ex1:-
-----
alst = [10,20,30,40,50]

# incr every element by 1 & Store in a new list - reslst
reslst = [ e+1 for e in alst ]  

ex2:-
-----
alst = [1,2,3,4,5]

# square element & Store in a new list - blst
blst = [e*e for e in alst]

ex3:-
-----
alst =["prasad", "karthik","rathna", "akhil"]

# convert each string to upper case & store in blst
blst = [ e.upper() for e in alst]

ex4:-
-----
alst =["prasad", "karthik","rathna", "akhil"]

#extract first char of each name & store in blst
blst = [ e[0] for e in alst   ] 

solution:-
----------
data="arun-blr-10,20,30,40"
marks = data.split("-")[2].split(",")
print(marks) ["10","20", "30", "40"]

newmarks= [int(e) for e in marks]
print(newmarks)  [10, 20 , 30 , 40]

print(sum(newmarks))



example for join:-
===================
>> STRING = "DELIMITER".join(STRLIST)

alst =["prasad", "karthik","rathna", "akhil"]
res= "-".join(alst)
print(res)   # "prasad-karthik-rathna-akhil"

task:-
------
Given
alst = [1,2,3,4,5]

Expected:-
res="1=2=3=4=5"
res="12345"

solution:-
----------
alst = [1,2,3,4,5]

res1 = "=".join(str(e) for e in alst)
res2 = "=".join(str(e) for e in alst)

print(res1)
print(res2)

example for trim:-
==================

data = "---------hai--bye--------"

res1=data.lstrip("-")
res2=data.rstrip("-")
res3=data.strip("-")


data = "     hai--bye      "

res1=data.lstrip()
res2=data.rstrip()
res3=data.strip()

------------------------------------------------------------------
if-else:-
===========
>> instead of flower brackets we used INDENTED BLOCKS

demo:-
======
name=input("enter u r name : ").lower()
myname="hari"
if name == myname:
    print("yes")
    print("same")
else:
    print("no")
    print("diff")

print("main")    


Task1:-
--------
Enter u r age : 16

Can cast vote / Cannot Cast vote

Task2:-
-------
given    : data = "ravi-math=20,sci=40,soc=50"
expected : tot > 150  - permitted
                      - not permit


solution:-
-----------
data = "ravi-math=20,sci=40,soc=50"
data = data.replace("=",",")
flst = data.split(",")
marks = [int(e) for e in flst[1::2]]
if sum(marks) > 150:
   print("Allowed")
else:
   print("Not Allowed")


for-iterator:-
==============
>> also called as foreach-loop
>> designed to traverse/visit every element in the collection
>> collection                           - Iterables
>> cursor which moves on the collection - Iterator
>> Starts from the first element        - FIRST ELEMENT
>> stops at STOPITERATION exception     - StopIteration

namelst =["prasad", "karthik","rathna", "akhil"] #collection

#using a foriterator 
#we have to visit each name, Extract the first character

for cursor  in  namelst : 
    res = cursor[0].upper()
    print(res)

########OR################
namelst[:] = [e[0].upper() for e in namelst]  # INPALCE
blst = [e[0].upper() for e in namelst]  # OUTPALCE

print(blst)

Task:-
------
Given:-
-------
datlst = [
          "10-nov-2020",
          "15-dec-2010",
          "5-apr-1998",
          "31-dec-1990"
         ]
Expected:-
----------
nov - N
dec - D
apr - A
dec - D

==================================================================
tuple-class:-
=============
>> constant collection
>> Im-mutable - shrink & Expand INPLACE - NO
>> Indexing & slicing

 
1) Define a tuple      : weeks=("sun","mon","tue","wed")
                         weeks="sun","mon","tue","wed"
2) length              : res = len(weeks)
3) search for "sat"    : if "sat" in weeks
4) index               : same as string
5) Slicing             : same as string
6) merge               : c=a+b
7) Compare             : if a==b

tuple unpacking:-
-----------------
1)
a=10
b=20
c=30
OR
a,b,c = 10,20,30

2)
*a,b,c = 10,20,30,40,50,60
a,*b,c = 10,20,30,40,50,60
a,b,*c = 10,20,30,40,50,60


3)
data="15-aug-1947"
dd,mm,yy   = data.split("-")
           # ["15", "aug", "1947"]

4)
data="ravi-blr-10-20-30-40-50"

name,city,*marks = data.split("-")  # trick

------------------------------------------------------------------
list-class:-
============
>> collection 
>> Mutable   - shrink & expand INPLACE = YES ( very important)
>> INPLACE operations
>> custom sorts

1) define a empty list  :  alst = []
2) Define a list        :  alst = [10,20,30,40]
3) length               :  res=len(alst)
4) search for 24        :  if 24 in alst
5) append               :  alst.append(25)  
6) del based on index   :  alst.pop(0)
   del based on value   :  alst.remove(30)
   del slice            :  del alst[:4]
7) sort                 :  alst.sort()             # asc order           
                           alst.sort(reverse=True) # desc order
8) reverse              :  alst.reverse()

see later:-
-----------
alst.extends(NEWLST)
ans =  sorted(alst)
ans =  alst[::-1]

Guess:-
--------
alst = [40,30,10,20,23,43]
alst.sort()
print(alst)


#A)  [10,20,23,30,40,43]
#B)  [43,40,30,23,20,10]
#C)  None
#D)  None of the above


Guess:-
=======
alst = [10,20,30,40,50]

alst.append(alst.pop())

print(alst)


A) [50,10,20,30,40]

B) [10,20,30,40,50]

C) [20,30,40,50,10]

D) None of the above


demo for collection problem:-
-----------------------------
>> in a collection problem we need to have a EMPTY LIST

emplst = [
           "ravi-blr-sales-15000",
           "hari-hyd-purch-25000",
           "john-tvm-accts-14000",
           "arun-chn-finan-16000"
         ]
####problem: - collect all the dept names in a LIST

empty=[]

for record in emplst:
    name,loc,dept,salary=record.split("-")
    empty.append(dept)

print(empty)



demo for filter problem:-
-------------------------
emplst = [
           "ravi-blr-sales-15000",
           "hari-hyd-purch-25000",
           "john-tvm-accts-14000",
           "arun-chn-finan-16000"
         ]
####problem: - display only emps names - drawing salary > 15000


for record in emplst:
    name,loc,dept,salary=record.split("-")
    if int(salary) >=15000:
       print(name)

Task1:-
-------
plst = [
         "dvd-  hw  -  20  ",
         "   mon - hw - 40",
         "prn - hw - 50",
         "win - sw-50",
         "office - sw - 10",
         "keb-hw-10"
       ]

Expected:-
-----------
hwlst = ["dvd", "mon", "prn", "keb"]
swlst = ["win", "office"]
         
solution:-
----------
hwlst,swlst = [],[]
for record in plst:
  name,ctgry,qty = record.split("-")
  if ctgry.strip()="sw":
     hwlst.append(name.strip())
  else:
     swlst.append(name.strip())

print(hwlst)
print(swlst)

Task2:-
--------
studlst = [
           "ravi-blr-10,20,30",
           "hari-mys-40,50,60",
           "guru-gdg-70,80,90",
           "mahi-hub-50,60,30"
          ]
Expected:-
----------
newlst =["ravi-60", "hari-150", "guru-240", "mahi-140"]

solution:-
==========
empty = []
for record in studlst:
    name, place, marks =  record.split("-")
    markslst = marks.split(',')
    total = sum([int(e) for e in markslst])
    empty.append(name + "-" + str(total))

print(empty)

=================================================================
                     DAta STructures
                            |
             --------------------------------
            |                                |
         Sequence                          Non-Sequence
 
    stores them in given order          don't store in given order
    index - allowed                     indexing - not allowed
    slicing - allowed                   slicing  - not allowed
    allows duplicates                   does't allow duplicates

    str/tuple/list                      set/dict
    search : BIGOH(n)                   BIGOH(1)


we have 1lakh records - 1 lakh minutes
we have 1crore records - 1 crore minutes
                        

we have 1lakh records  - 1 minutes
we have 1crore records - 1 minutes


set-class:-
============
>> collection of Im-Mutables
>> mutable - shrink & expand INPLACE - YES
>> indexing -  NO
>> slicing  -  NO
>> Non-sequence
>> duplicates are auto deleted

1) define a empty set   :  grp = set()
2) define a set         :  a={10,30,40}
                        :  b={40,50}
3) length               :  res=len(a)
4) search for 25        :  if 25 in a
5) expand one ITEM      :  a.add(25)
6) shrink one ITEM      :  a.remove(10)
7) intersection         :  c=a&b
8) union                :  c=a|b
9) difference           :  c=a-b / c=b-a
10) symm diff           :  c=a^b




Task1:-
-------
grp1 = ["hari", "guru", "akhil", "prity","shimpu"]
grp2 = ["satish", "guru", prasad", "prity","balaji"]

find common
find uncommon

solution:-
----------
set1 = set(grp1)
set2 = set(grp2)
print("Common   = ",set1&set2)
print("UnCommon = ",set1^set2)



Task2:-
-------
grp1 = ["hari-60", "guru-10", "akhil-40", "prity-50","shimpu-70"]
grp2 = ["satish-60", "guru-80", prasad-95", "prity-70","balaji-80"]

find common
find uncommon

solution:-
----------
grp4 = {e.split("-")[0] for e in grp1}
grp5 = {e.split("-")[0] for e in grp2}
print(grp4 ^ grp5)
print(grp4 & grp5)


Applications of set:-
----------------------
>> to remove duplicates 
>> common
>> uncommon
>> diff

-----------------------------------------------------------------
dict-class:-
============
>> collection of key & value pairs
>> mutable - shrink & Expand - YES
>> indexing - allowed
>> Slicing -  not allowed
>> non-sequence
>> hashes, map, htable , lookuptable


1) define a empty dict   : ctab={}
2) define a dict         : ctab={
                                 "red"  : 10,
                                 "blue  : 20,
                                 "green": 30
                                }
3) length                : res = len(ctab)
4) search for "red"      : if "red" in ctab
5) get value of "red"    : res = ctab["red"] / ctab.get("red")
6) shrink                : ctab.pop("blue")
7) expand                : ctab["brown"] = 40


see later:-
-----------
atab.update({......})
merge 2 dict


Demo:-
------
menu = {
         "dosa"  : 50,
         "poha"  : 40,
         "upma"  : 40,
         "poori" : 66,
         "idly"  : 20,
       }

item = input("Enter u r choice : ").lower()
if item in menu : 
   print("yes")
   price = menu[item]  
   print(item, price)
else:
   print("no")
   print("not found")


Task1:-
-------
stab = {
         "ravi" : ["blr", "CSE", "10,20,30,40"],
         "arun" : ["chn", "CIV", "40,50,60,70"],
         "tara" : ["hyd", "MECH", "54,45,65,34"],
         "manu" : ["tvm", "ECE" , "43,76,46,34"]
       }

ravi
loc = blr
stream = cse
total = 100
max = 40
min = 10
avg = 20.50

solution:-
-----------
name = input("Enter u r name : ").lower()
if name in stab:
   data = stab[name]
   print("LOC     = ",data[0])
   print("Stream  = ",data[1])
   marks = [int(e) for e in data[2].split(",")]
   print("Total   = ",sum(marks))
   print("MAx     = ",max(marks))
   print("Min     = ",min(marks))
   print("Avg     = ",sum(marks)/len(marks))
else:
   print("not found") 

TAsk2:-
-------
Given: 
data="five zero eight nine"

Expected:
5089

solution:-
----------
data="five zero eight nine"
dict_values = { 
                 "zero"  : "0",
                 "one"   : "1",
                 "two"   : "2",
                 "three" : "3",
                 "four"  : "4",
                 "five"  : "5",
                 "six"   : "6",
                 "seven" : "7",
                 "eight" : "8",
                 "nine"  : "9"}
data_words= data.split(" ")
final = ""
for e in data_words:
    final = final + dict_values[e]
print(final)


Applications of dict:-
-----------------------
>>Conversion
>>frequency count
>>subtotal
>>subgroup

------------------------------------------------------------------
Nested DAta STructures:-
========================

a = ((10,20), (30,40))  # tuple within a tuple
a = ([10,20], [30,40])  # list within a tuple


a = [(10,20), (30,40)]  # tuple within a list
a = [[10,20], [30,40]]  # list within a list  # MATRIX


a = {                     # list within a dict
     "ravi" : [10,20],
     "john" : [30,40]
    }

                          # dict within a dict
a = {                      
     "ravi" : {"loc" : "blr", "marks" :  [10,20]},
     "john" : {"loc" : "mys", "marks" :  [30,40]}
    }


-------------------------------------------------------------------
Extended DATA STRUCTURES:-
--------------------------
Ex1:-
-----
import array

arr = array.array("i")   # "i" denotes integer
arr.append(20)
arr.append(50)
arr.append(10)
arr.append(30)
print(arr)

arr.append("434")  # error


Ex2:-
------
import collections

alst = ["blr","chn","hyd", "blr","hyd", "blr", "blr", "blr"]

freq = collections.Counter(alst)

print(freq)

==================================================================
Files:-
========
>> to store the data permanently for the future use
>> data persistance 
>> read-writing into the HARD DISK
>> I/o between RAM & DISK - STRING
>> 3 reference points
      BOF - 0
      CUR - 1
      EOF - 2
>> file opening modes              OLD DATA     file not found  
     r  - readonly        - BOF  -  retained  - Error
     w  - overwrite       - BOF  -  lost      - create new
     a  - append          - EOF  -  retained  - create new
     r+ - read-write      - BOF  -  retained  - Error
     w+ - overwrite-read  - BOF  -  lost      - create new
     a+ - append-read     - EOF  -  retained  - create new
>> Binary modes  - rb/wb/ab/rb+/wb+/ab+

How to write into the file:-
----------------------------
f1         = file handler - user defined
open       = inbuilt function
data.txt   = filename
"w"        = open the file in WRITE MODE

f1 = open("data.txt", "w")
f1.write("prity")
f1.write("shimpu")
f1.write("satish")
f1.write("balaji")
f1.close()


OR


f1 = open("data.txt", "w")
f1.write("prity\n")
f1.write("shimpu\n")
f1.write("satish\n")
f1.write("balaji")
f1.close()


How to read from the file:-
---------------------------

fob = open("data.txt", "r")

for cursor in fob:
   cursor = cursor.rstrip("\n")
   print(cursor)

fob.close()


Task1:-
-------
f1 = open("data.txt","w")
f1.write("ravi-blr-10,20,30\n")
f1.write("hari-chn-40,50,60\n")
f1.write("kala-hyd-43,65,34\n")
f1.write("manu-mys-43,23,76")
f1.close()

Expected:-
-----------
etab={"ravi" : 60,
      "hari" : 150,
      "kala" : ?
      "manu" : ?
     }

Task2:-
-------
f1 = open("new.txt", "w")
f1.write("hello world of unix\n")
f1.write("lookz simple but not as it is\n")
f1.write("now the new way is there\n")
f1.write("bye for now")
f1.close()

solution:-
----------
dict1 = {}
fob =  open("data.txt","r")
for cursor in fob:
    cursor = cursor.strip("\n")
    words = cursor.split("-")
    dict1[words[0]] = sum([int(e) for e in words[-1].split(",")])
print(dict1)
fob.close()


EXpected:-
----------
hello world of unix           = 4
lookz simple but not as it is = 7
now the new way is there      = 6
bye for now                   = 3
                        Total = ?

solution:-
----------
f1 = open("new.txt","r")
words = {}
for line in f1:
    line = line.rstrip("\n")
    wordlst = line.split()
    words[line] = len(wordlst)
print(words)
f1.close()




Tricks:-
--------
fob = open("data.txt", "r")
print(fob.read())
fob.close()

OR

#auto close the file
with open("data.txt", "r") as fob:
   print(fob.read())


other ways to read :-
---------------------
strbuffer = fob.read()     # read compelete & return it as string
strbuffer = fob.readline() # read one line & return it as string
lstbuffer = fob.readlines()# read compelete & return stringlist

Guess:-
-------
f1 = open("num.txt", "w+")
f1.write("10\n")
f1.write("20\n")
f1.write("30\n")
f1.write("40")

res = f1.read() 
print(res)
f1.close()

A) 10\n20\n30\n40
B) 40
C) BLANK - EMPTY STRING
D) 10


Guess:-
-------
f1 = open("num.txt", "w+")
f1.write("10\n")
f1.write("20\n")
f1.write("30\n")
f1.write("40")

f1.seek(0,0)      # reset the cursor to the BOF

res = f1.read() 
print(res)
f1.close()

A) 10\n20\n30\n40
B) 40
C) BLANK - EMPTY STRING
D) 10

==================================================================
Functions:-
===========
>> Function Objects
>> define functions first & Then call them   - INTERPRETER
>> variable defined within fn                - LOCAL Vars
>> can return multiple values in python      - TUPLE
>> there is no type checking of ARGS
>> function which accepts arguments & Return the value 
   is called as "PURE FUNCTION"
>> def express(a,b,c):         # compulsory-positional args
   def express(a=25,b=11,c=33) # optional  -default args
   def express(a,b,c=10)       # hybrid


ex1:-
-----
def square(num):
  res = num*num
  print("LOCAL VARS ",locals())
  return res

ans=square(5)
print(ans)


fn name       = square
no of args    = 1
type of args  = int/float
is it pure fn = yes
type of fn    = positional
  

ex2:-
-----
def collect(dlst):
  empty=[]   
  if type(dlst) == list:
    for elem in dlst:
      empty.append(int(elem.split("-")[1]))
  return empty

datlst = ["alpha-10", "beta-20", "delta-30", "gamma-40"]
newlst=collect(datlst)
print(newlst) # [10,20,30,40]


fn name       = collect
no of args    = 1
type of args  = list
is it pure fn = yes
type of fn    = positional


ex3:-
-----
def above_50(tab):
  empty=[]
  for k,v in tab.items():
     if v>=50:
         empty.append(k)

  return empty


ptab={"DVD": 20, "CD": 55, "MON": 30, "PRN": 60"}
newlst = above_50(ptab)
print(newlst) # [ "CD", "PRN"]


fn name       = above_50
no of args    = 1
type of args  = dict
is it pure fn = yes
type of fn    = positional


Ex4:-
-----
def wordcount(fn="temp.txt"):
   words,chars,lines = 0,0,0
   with open(fn,"r") as fob:
       for elem in fob:
           lines+=1
           words+=len(elem.split())
           chars+=len(elem)
   print("Lines = ",lines)
   print("Words = ",words)
   print("Chars = ",chars)
   

fname="data.txt"
wordcount(fname)


fn name       = wordcount
no of args    = 1
type of args  = str
is it pure fn = no
type of fn    = default




Given:-
--------
f1 = open("data.txt", "w")
f1.write("arun works around this\n")
f1.write("data and also fine")
f1.close()
fname="data.txt"
alpha="a"
reslst = words_starts_with(fname, alpha)
print(reslst)
  
Expected:-
-----------
["arun", "around", "also"]



solution:-
==========
def words_starts_with(fn, alpha):
 res=[]
 with open(fn,"r") as f1:
   wlist = f1.read().split()
   for word in wlist:
     if word[0]==alpha:
      res.append(word)
 return res

OR
def words_starts_with(fn, alpha):
 with open(fn,"r") as f1:
   wlist = f1.read().split()
   return [e for e in wlist if e[0]==alpha]







keyword args:-
==============
def connect(host="local",user="guest",password="guest",command="ls"):
   pass

sc1:-
-----
let host name be default
    user be default
    password be default
change only command = "top"

connect(command="top")

sc2:-
-----
let user be default
    password be default
change only command = "top"
change host name = "appserver"

connect(command="top",host="appserver")

sc3:-
------

connect("dbserver",command="uptime")   #guess
                  # mix & match of non-keyword & keyword args

 host = dbserver
 user = guest
 pwd  = guest
 cmd  = uptime


sc4:-
------

 hostname - default
 password - default

 command  - set to uptime
 user     - set to admin

connect(command="uptime", user="admin")


RULE:-
------
non-keyword leftmost, keyword rightmost in any fn call

 def connect(host="local",user="guest",password="guest",command="ls"):
   pass

 connect(user="root", "admin@123", "ls")   # IN-VALID

 connect(user="root", "admin@123", command="ls")   # IN-VALID

 connect("admin@123", command="ls",user="root")   # VALID
                                                  # not matching position

 connect(password="admin@123", command="ls",user="root")   # VALID

 connect("mailserver","admin",command="backup") # VALID


Variable args:-
================
>> *args    -args is a NAMING CONVENTION   - TUPLE
>> **kwargs -kwargs is a NAMING CONVENTION - DICT

def callme(*args,**kwargs):
  print("Call me")
  print("ARGS = ",args)
  print("KWARGS = ",kwargs)


callme(10,20,30,a=40,b=50)  # args=(10,20,30)
                            # kwargs={"a" : 40, "b" : 50}

callme(1,2,3)   # args  = [1,2,3]
                # kwargs= {}

callme(blr=20,delhi=30)  # args   = [] 
                         # kwargs = {"blr" : 20 , "delhi" : 30}

callme()     # args =   []
             # kwargs = {}


lambda expressions:-
====================
>> one liner fns
>> pure fns


f(x) = x+5

def f(x):
  return x+5

#OR

f = lambda x : x+5

res = f(10)
print(res)


task:-
------
f1("manish sharma")      - sharma
f2("manish sharma")      - ms
f3("arun-blr-10,20,30")  - ["10", "20", "30"]
f4("arun-blr-10,20,30")  - [10, 20, 30 ]
f5("arun-blr-10,20,30")  - 60


solution:-
-----------
f1 = lambda x : x.split()[1]
f2 = lambda x : x.split()[0][0]+x.split()[1][0]
f3 = lambda x : x.split("-")[2]
f4 = lambda x : [str(e) for e in x.split("-")[2].split(",")]
f5 = lambda x : sum([int(e) for e in x.split("-")[2].split(",")])

print(f1("manish sharma")) #- sharma
print(f2("manish sharma"))
print(f3("arun-blr-10,20,30"))
print(f4("arun-blr-10,20,30"))
print(f5("arun-blr-10,20,30"))


------------------------------------------------------------------
Custom sort:-
=============
Ex1:-
=====
studlst = [
           "ravi-blr-80",
           "taja-chn-84",
           "arun-hyd-45",
           "mahi-tvm-67",
           "yash-blr-86",
           "john-mys-85"
          ]
studlst.sort()
print("\n".join(studlst))


Ex2:-
=====
studlst = [
           "ravi-blr-80",
           "taja-chn-84",
           "arun-hyd-45",
           "mahi-tvm-67",
           "yash-blr-83",
           "john-mys-85"
          ]
studlst.sort(key=lambda x : int(x.split("-")[2]))
print("\n".join(studlst))


#x="ravi-blr-45"
#f =lambda x : int(x.split("-")[2]) 
==================================================================
Modules & packages:-
=====================
>> Module is Library
>> Package is FOLDER - collection of modules
>> collection of fns/classes/variables
>> file extension should be .py
>> creates a PYTHON BYTE CODES ".PYC"
>> load a library
    -import modulefilename
    -from modulefilename import *
>> Fully Qualified Names / Relative Names
>> module search path


FQN-names - any name can have ONLY one FQN
REL-names - any name can have MORE THAN ONE REL names

FQN ==> world.asia.india.kar.blr

REL names
we are in "asia"  - india.kar.blr
we are in "india" - kar.blr
we are in "kar"   - blr 


mathlib.py
----------
def square(num):
  res = num**2
  print("SQUARE = ",res)

def greet():
  print("Good Morning!!")

def add(a,b):
  ans = a + b
  print("SUM = ",ans)

def express(a,b,c):
  ans  = a*b + b/c
  print("EXPRESS = ",ans)


consumer1.py:-
-------------
import mathlib

print(dir(mathlib))

print(dir())

mathlib.square(5)


Consumer2.py:-
--------------
from mathlib import *

print(dir())

square(5)


4 different ways of loading a library:-
---------------------------------------
1) import mathlib          # FQN
                           # avoids name clashes
   mathlib.square(5)


2) import mathlib as  m    # aliasing FQN
                           # Avoids name clashes
   m.square(5)            
 

3) from mathlib import *   # REL
                           # have name clashes
   square(5)


4) from matlib import square  # selective 
                              # have name clashes
   square(5)           

Note:-
--------
"__pycache__" special folder is autocreated for PYTHON BYTE CODES


What is names clashes ?
------------------------
Ex1:-
------
rathna.py		satish.py
---------		----------
def start():		def begin():
  pass			  pass

def stop():		def end():
  pass			  pass


consumer.py:-
-------------
from rathna import *
from satish import *

start()
begin()


Ex2:-
------
>> later "satish" changed the fun "begin" to "start"

rathna.py		satish.py
---------		----------
def start():		def start():
  pass			  pass

def stop():		def end():
  pass			  pass


consumer.py:-
-------------
from rathna import *
from satish import *

start()     # Always call the recent lib fns i.e satish
            # satish version of "start"


Ex3:-
------
>> alias the clashing name

rathna.py		satish.py
---------		----------
def start():		def start():
  pass			  pass

def stop():		def end():
  pass			  pass


consumer.py:-
-------------
from rathna import *
from satish import *
from rathna import start as start2

start()     # Always call the recent lib fns i.e satish
            # satish version of "start"

start2()    # this will call rathna lib fns - start




module search path:-
--------------------
>> LIBPATH in python

import sys

print(sys.path)

OR

env variable - PYTHONPATH


Example for packages:-
======================
>> package is a FOLDER
>> special file named "__init__.py"

import packagename  # INVALID
import modulename   # VALID
from package import * # VALID 
from module import *  # VALID



                            C:
                            |-----------> I AM HERE
                          mobile
                            |
              -------------------------------
             |                               |               
           nokia                           sony
             |                               |
  ----------------------                     |
 |                      |                    | 
a50.py                b40.py               k7.py
-------               -------              -----
def start():          def start():         def begin():
  pass                    pass               pass

def test():           def report():        def test():
  pass                    pass               pass


#load only start of a50
from mobile.nokia.a50 import start

start()





# get into MODULE "k7" using "from" - 
from mobile.sony.k7 import *

test()


# load "k7" using "from"
from mobile.sony import k7

k7.test()



# we have to test all the mobiles
from mobile import *

nokia.a50.test()
nokia.b40.report()
sony.k5.test()


#we have to test all the NOKIA devices
from mobile.nokia import *

a50.test()
b40.report()



# we have to test only "a50" device
import mobile.nokia.a50

mobile.nokia.a50.test()


Common Exception while loading a MODULE/PACKAGE:-
-------------------------------------------------
ModuleNotFoundError: No module named 'second123'

Common Exception while calling a MODULE FUNCTION:-
--------------------------------------------------
AttributeError: module 'second' has no attribute 'todays'

TypeError: add() missing 2 required positional arguments: 'a' and 'b'


===================================================================
                        Class Development
                               |
             --------------------------------------
            |                                      |
        Compile Time                           Run Time
 
   -C++/JAVA/C#                          - python
   -we declare data memebers             - we don't declare data mem 
   -we declare methods                   - we declare methods
   -"this" is implicit for methods       - "this" is explicit 
   -supports overloading                 - does't support overloading   
   -supports inheritance                 - supports inheritance 
   -constructor cascading                - don't have ctor cascading
   -supports over-riding                 - supports over-riding
        
Intro to Classes:-
==================
>> Always class name should starts with CAPITAL letter
>> default access specifier is PUBLIC
>> every class is a derived class of special class named -"object"


class Person:

   def __init__(self,name,loc,age): # parameterized CTOR
      print("I AM BORN.....")
      self.name = name
      self.loc  = loc
      self.age  = age

   def convert(self):
      self.name = self.name.upper()

   def show(self):
      print(self.name,self.loc,self.age)



p1 = Person("guru","blr",20)
p1.show()
p1.convert()
p1.show()


example:-
---------
########################
#filename = Person.py  #
########################
class Person:

   def __init__(self,name,loc,age): # parameterized CTOR
      print("I AM BORN.....")
      self.name = name
      self.loc  = loc
      self.age  = age

   def convert(self):
      self.name = self.name.upper()

   def show(self):
      print(self.name,self.loc,self.age)


#filename = consumer.py
########################
import Person

p1 = Person.Person("guru","blr",20)
p1.show()
p1.convert()
p1.show()



#filename = consumer.py
########################
from Person import Person

p1 = Person.Person("guru","blr",20)
p1.show()
p1.convert()
p1.show()



Task:-
------

st1 = Student("ravi", "10,20,30")
st1.findtotal()
st1.show() # name = ravi
           # marks = [10,20,30]
           # total = 60

solution:-
----------
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def findTotal(self):
        self.total = sum([int(e) for e in self.marks.split(",")])
    def show(self):
        print("name=", self.name)
        print("marks=",self.marks)
        print("total=", self.total)
st = Student('sh', '10,20,30')
st.findTotal()
st.show()


Major points w.r.t classes:-
============================
1) define a class           - class Person:
2) how to create objects    - p1 = Person("hari","blr",30)
3) access data members      - self.name
4) access methods           - self.findtotal()
5) Ctor                     - def __init__(self)
6) this pointer             - "self" - its not a keyword

7) private data members     - self.__datamember
8) class data members       - static data member of C++/JAVA
9) class methods            - static method of C++/JAVA
10) inheritance             - class Derived(Base)
11) method over-riding      - super().METHODNAME()
                            - BASECLASSNAME.METHODNAME(self)

example for class data member & Class method:-
-----------------------------------------------
class Product:
   total=0        # class data-member

   def __init__(self,name,qty):
       self.name = name
       self.qty = qty
       Product.total+=self.qty

   def show(self):
       print(self.name,self.qty)

   @classmethod                 #  class method
   def display(cls):
       print("Total = ",Product.total)
       print("Total = ",cls.total)

p1 = Product("A",10)
p2 = Product("B",20)
p3 = Product("C",30)
Product.display()     # p3.display()


Example for Inheritance & method over-riding:-
==============================================
Ex1:-
=====
class Base:
   def __init__(self,a):
      print("Base Ctor")
      self.a = a
   def show(self):
      print("BASE... SHOW")
      print("A = ",self.a)

class Derived(Base):            # how to derive class
   def __init__(self,a,b):
      Base.__init__(self,a)     # ctor cascading
      print("Derived Ctor")
      self.b = b
   def foo(self):
      print("DERIVED... foo")
      print("B = ",self.b)

ob1 = Derived(10,20)
ob1.show()
ob1.foo()

       
Ex2:- for method over-riding
==============================
>> MRO - method resolution order

class Base:
   def __init__(self,a):
      print("Base Ctor")
      self.a = a
   def show(self):
      print("BASE... SHOW")
      print("A = ",self.a)

class Derived(Base):            # how to derive class
   def __init__(self,a,b):
      Base.__init__(self,a)     # ctor cascading
      print("Derived Ctor")
      self.b = b
   def show(self):
      super().show()            # Base.show(self)
      print("DERIVED... foo")
      print("B = ",self.b)

ob1 = Derived(10,20)
ob1.show()
ob1.foo()



==================================================================
Intro to Exception Handling:-
=============================
>> clean exit of a program
>> explicit exception handling - try/except/else/finally/raise
>> Exception class hierarchy -  https://docs.python.org/3/library/exceptions.html#exception-hierarchy


class ZeroError(Exception):     # user defined exception
   def __init__(self,mesg):
      Exception.__init__(self)
      self.mesg = mesg
   def __str__(self):           # equivalent - toString() of java
      return self.mesg

try: 
    num = input("Enter a number : ")
    num = int(num)
    if num==0:
       raise ZeroError("num cannot be ZERO.....")  # explicit throw
    res=num*num

except ValueError as e1:
    print("Action1",e1)
except ZeroError as e2:
    print("Action2",e2)
except Exception as e3:           # generic catch block
    print(e3)
else:                             # optional syntax
    print("ANSWer = ",res)
finally:                          # optional syntax
    print("Clean")
 


Core Libs:-
===========
>>list of all the standard libraries
>>https://docs.python.org/3/library/index.html

import datetime

help(datetime)
print(datetime.date.today())
print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%d %m %Y %H %M %S %a %b"))


import sys  # interface b/w python program & python interpreter

print(sys.version)  
print(sys.executable) 
print(sys.path)
print(sys.argv)   # Command line args


import os   # interface b/w python program & OS

print("OS = ",os.name)
print("PWD = ",os.getcwd())
print("PID = ",os.getpid())


import re

data="10,20 30:40;50,60-70"
flst = re.split("[,\s:;\-]",data)
print(flst)


import re

data = "10,,,,,,30,,,40,50,,,,,,60,70,,80"
data = re.sub(",+", ",",data)
flst = data.split(",")
print(flst)


import sqlite3:-
----------------
 RDBMS - oracle/mysql/MSQL/Sybase/DB2

import sqlite3

con = sqlite3.connect("c:\\pyprogs\\master.db")
cur = con.cursor()

cur.execute("select * From emps")

for elem in cur:
   print(elem)

con.close()


-----------------------------------------------------------------
import pickle
import shelve
import json
import sqlite3


import pickle

config  = {
           "loc1" : [10,20],
           "loc2" : [30,40]
          }

f1 = open("data.pkl", "wb")
pickle.dump(config,f1)
f1.close()

import pickle

f1 = open("data.pkl", "rb")
res = pickle.load(f1)
print(res)
f1.close()

------------------------------------------------------------------

Core Utils:-
============
1) how to debug - set a breakpoint
                - run in debug mode
                - stepin/setpover
                - continue
                - display values
                - stop
2) how to unittest             - pytest3 / unittest
3) how to write documentation  - triple quotes
4) how to install repo lib     - pip install modulename
5) how to distribute           - setuptools/distutils


C:\>  pip list              - list all the repo libs
C:\>  pip install xlrd      - to install a specific library
C:\>  pip uninstall xlrd    - to uninstall a specific library


$  sudo pip3 list              - list all the repo libs
$  sudo pip3 install xlrd      - to install a specific library
$  sudo pip3 uninstall xlrd    - to uninstall a specific library

program to read from a XL file:-
----------------------------------
import xlrd

book = xlrd.open_workbook("hello.xlsx")

print(book.nsheets)        # Display the no of sheets
print(book.sheet_names())  # display the sheet names


first_sheet = book.sheet_by_index(0)   # we are selecting the -sheet1
 
#print(first_sheet.row_values(0))
#cell = first_sheet.cell(0,0)
#print(cell)
#print (cell.value)

print(first_sheet.nrows)               # no of rows
print(first_sheet.ncols)                # no of columns

for i in range(first_sheet.nrows):
  for j in range(first_sheet.ncols):
    print(first_sheet.cell(i,j).value,end =" ")
  print()


































































