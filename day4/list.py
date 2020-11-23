#Task1: -
grp1 = ["hari", "guru", "akhil", "prity", "shimpu"]
grp2 = ["satish", "guru", "prasad", "prity","balaji"]

print("common : %s " %(set(grp1) & set(grp2)))
print("uncommon : %s " %(set(grp1) ^ set(grp2)))



#Task2:-
grp1 = ["hari-60", "guru-10", "akhil-40", "prity-50", "shimpu-70"]
grp2 = ["satish-60", "guru-80", "prasad - 95", "prity - 70","balaji - 80"]

print("common : %s " %({e.split("-")[0].strip() for e in grp1} & {e.split("-")[0].strip() for e in grp2}))
print("uncommon : %s " %({e.split("-")[0].strip() for e in grp1} ^ {e.split("-")[0].strip() for e in grp2}))

