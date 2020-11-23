import pickle

config = {
    "loc1": [10, 20],
    "loc2": [30, 40]
}

f1 = open("data.pkl", "wb")
pickle.dump(config, f1)
f1.close()

import pickle

f1 = open("data.pkl", "rb")
res = pickle.load(f1)
print(res)
f1.close()