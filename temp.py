# d = {"DS2": [], "DS1": []}

import pickle
import os

# with open('Game_List.pkl', 'wb') as f:
#     pickle.dump(d, f)

# # with open('Gme_List.pkl', 'rb') as f:
# #     loaded = pickle.load(f)
# os.listdir()

# with open("Game_List.pkl", 'wb') as f:
#     pickle.dump(game_list, f)

class test:
    instances = []
    def __init__(self, name, savefile):
        self.name = name
        self.savefile = savefile
        self.directory = '\\'.join(self.savefile.split("\\")[:-1])
        test.instances.append(self)
    

DS3 = test("DS3", r"D:\test\DARKS30000.sl2")
DS2 = test("DS2", r"D:\test\DARKSII0000.sl2")


del (DS3, DS2)
print(test.instances)
with open("Game_List.pkl", 'wb') as f:
    pickle.dump(test.instances, f)
# Load data
with open("Game_List.pkl", 'rb') as f:
    test.instances = pickle.load(f)
test_vars = [x for x in test.instances]

games = {}

for i in test_vars:
    x = i.name
    games[x] = i

print(games)
