stab = {
    "ravi": ["blr", "CSE", "10,20,30,40"],
    "arun": ["chn", "CIV", "40,50,60,70"],
    "tara": ["hyd", "MECH", "54,45,65,34"],
    "manu": ["tvm", "ECE", "43,76,46,34"]
}

#ravi
#loc = blr
#stream = cse
#total = 100
#max = 40
#min = 10
#avg = 20.50
student = input("Enter the student name : ").lower()
if student in stab :
   print("Name : %s" %(student))
   print("Location : %s" %(str(stab[student][0])))
   print("Stream : %s" %(str(stab[student][1])))
   mark = [int(e) for e in stab[student][2].split(",")]
   print("Total : %s" %(sum(mark)))
   print("Max : %s" % (max(mark)))
   print("Min : %s" % (min(mark)))
   print("Avg : %s" % (sum(mark)/len(mark)))
else:
   print("%s not found in out records" %(student))