data = "ravi-math=20,sci=40,soc=50"
res = [int(e.split("=")[-1]) for e in data.split("-")[-1].split(",")]
if sum(res) > 150:
    print("Permited")
else:
    print("Not Permited")