
# Your code here 
import random

def chat():
    coworkers = ["Jack", "Lenny", "Michelle", "Andrea"]
    chatee = coworkers[random.randomint(0, len(coworkers)-1)]
    print(f"Chatting with {chatee} ...")
    print(f"Done")


def getWater():
    print(f"Getting water...")
    print(f"That was refreshing.")

def useSocialMedia():
    socialMedia = ["FaceBook", "Twitter", "YouTube", "Reddit"]
    choice = socialMedia[random.randomint(0, len(socialMedia)-1)]
    print(f"Using {choice} ...")
    print("Done")
