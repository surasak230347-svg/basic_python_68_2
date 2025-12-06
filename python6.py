#function
def myFullName(firstName="Unknow",lastname="forger"):
    fullName = firstName+""+lastname
    return fullName

print(myFullName("loid","forger"))
print(myFullName("yor","forger"))
print(myFullName("anya","forger"))
print(myFullName("bond","forger"))

def redpotion(hp):
    hp += 50
    return hp
currenthp = 100
print("current Hp:",currenthp)
currenthp= redpotion(currenthp)
print("after using red potion hp:",currenthp)