import berserk

session = berserk.TokenSession("052oFyKs8nbYmmEH")
client = berserk.Client(session=session)

def blitz(username):
    return(int((client.users.get_rating_history(username).strip('][').split('{'))[2].split("[")[-1].split(",")[-2].strip("]]}")))

def bullet(username):
    return (int((client.users.get_rating_history(username).strip('][').split('{'))[1].split("[")[-1].split(",")[-2].strip("]]}")))

def rapid(username):
    return(int((client.users.get_rating_history(username).strip('][').split('{'))[3].split("[")[-1].split(",")[-2].strip("]]}")))

usernames = ["abhatnagar23", "AChandrasekar23", "LeggiadraVendetta", "ahamrah27", "gnorthup23", "rebeccaharris", "penguingim1"]


print("Blitz Leaderboard")
BlitzDict = {}
for i in range(0, len(usernames)):
    BlitzDict[usernames[i]] = blitz(usernames[i])
BlitzTuples = sorted(BlitzDict.items(), key=lambda item: item[1], reverse=True)
SortedBlitzDict = {k: v for k, v in BlitzTuples}

for key, value in SortedBlitzDict.items():
    print(key, ":", value)
print("")
print("Rapid Leaderboard")

RapidDict = {}
for i in range(0, len(usernames)):
    RapidDict[usernames[i]] = rapid(usernames[i])
RapidTuples = sorted(RapidDict.items(), key=lambda item: item[1], reverse=True)
SortedRapidDict = {k: v for k, v in RapidTuples}

for key, value in SortedRapidDict.items():
    print(key, ":", value)

print("")
print("Bullet Leaderboard")

BulletDict = {}
for i in range(0, len(usernames)):
    BulletDict[usernames[i]] = bullet(usernames[i])
BulletTuples = sorted(BulletDict.items(), key=lambda item: item[1], reverse=True)
SortedBulletDict = {k: v for k, v in BulletTuples}

for key, value in SortedBulletDict.items():
    print(key, ":", value)
