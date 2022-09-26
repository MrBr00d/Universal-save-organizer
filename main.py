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
        # Game.instances.append(self)

#check is save data exists and open it
def load():
    global game_info
    if "Game_Info.pkl" in os.listdir():
        with open('Game_Info.pkl', 'rb') as f:
            game_info = pickle.load(f)
    list_games()


def add_game(name, savefile):
    global game_info
    if "game_info" in globals():
        if name in list(game_info.keys()):
            print("Game already exists")
            return
        else:
            game_info[name] = Game(name,savefile)
            print("Added game")
            with open("Game_Info.pkl", 'wb') as f:
                pickle.dump(game_info, f)
            list_games()
            return
    else:
        game_info = {name: Game(name,savefile)}
        with open("Game_Info.pkl", 'wb') as f:
            pickle.dump(game_info, f)
        print("New game added")
        list_games()
        return
       
def remove_game(game):
    if game in game_list:
        game_info.pop(f'{game}')
        with open("Game_Info.pkl", 'wb') as f:
            pickle.dump(game_info, f)
        list_games()

def list_games():
    global game_list
    game_list = list(game_info.keys())
    
def list_profiles(game):
    global profile_list
    dir = game_info[game].directory
    profile_list = [i.name for i in os.scandir(dir) if i.is_dir()]
    

# Create profile creation method
# Todo: load in existing profiles
def create_profile(game, profile):
    if profile not in profile_list:
        os.mkdir(os.path.join(game_info[game].directory, profile))
        list_profiles(game)
    else:
        return print("Error: Profile already exists")

# Create delete profile method
# Todo: check if it already exists
def remove_profile(game, profile):
    if profile in profile_list:
        shutil.rmtree(os.path.join(game_info[game].directory, profile))
        list_profiles(game)
    else:
        return print("Error: no such profile exists")


