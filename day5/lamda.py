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