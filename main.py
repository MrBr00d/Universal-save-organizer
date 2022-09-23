'''
Op het moment is het inladen opgelost. Er zijn nu 2 variables die hetzelfde hebben.
De class variable Game.instances en de global variable game_info.
Ze worden beide ingeladen en opgeslagen omdat ik nu nog niet weet of het een probleem is
dat Game.instances een class variable is.
'''

import os
import shutil
import pickle
        
class Game:
    instances = []
    def __init__(self, name, savefile):
        self.name = name
        self.savefile = savefile
        self.directory = '\\'.join(self.savefile.split("\\")[:-1])
        Game.instances.append(self)

#check is save data exists and open it
def load():
    if "Game_Info.pkl" in os.listdir():
        with open('Game_Info.pkl', 'rb') as f:
            Game.instances = pickle.load(f)    
    global game_info
    global load_unpacked
    game_info = {}
    load_unpacked = [x for x in Game.instances]
    print(load_unpacked)
    for i in load_unpacked:
        x = i.name
        game_info[x] = i
    print(game_info)

load()
print(Game.instances)
x = Game.instances
x["DS3"].savefile
print(load_unpacked[0])
load_unpacked.

def add_game(name, savefile):
    global game_info
    if "game_info" in globals():
        for i in game_info.keys():
            if i in name:
                print("Game already exists")
                return
            else:
                game_info[name] = []
                globals()[f'{name}'] = Game(name,savefile)
                print("Added game")
                with open("Game_Info.pkl", 'wb') as f:
                    pickle.dump(game_info, f)
                return
    else:
        game_info = {name: Game(name,savefile)}
        # globals()[f'{name}'] = Game(name,savefile) temp out?
        # name = game(name, savefile)
        with open("Game_Info.pkl", 'wb') as f:
            pickle.dump(game_info, f)
        print("New game added")
        return
       
# DS2 = game("DS2", r"D:\test\DARKSII0000.sl2")
# add_game("DS2")

add_game("DS3", r"D:\test\DARKSII0000.sl2")
print(game_info.get())

game_info = [DS2, DS3]
with open("test.pkl", "wb") as f:
    for i in game_info:
        print(i)

del game_info
#load games
with open("test.pkl", "rb") as f:
    print(pickle.load(f))
    




# Create profile creation method
# Todo: load in existing profiles
def create_profile(game, profile):
    if profile not in profile_list:
        os.mkdir(os.path.join(game.directory, profile))
        profile_list.append(profile)
    else:
        return print("Error: Profile already exists")

# Create delete profile method
# Todo: check if it already exists
def remove_profile(game, profile):
    if profile in profile_list:
        shutil.rmtree(os.path.join(game.directory, profile))
    else:
        return print("Error: no such profile exists")

DS2 = game("DS2", r"D:\test\DARKSII0000.sl2")
DS1 = game("DS1", r"D:\test2")
