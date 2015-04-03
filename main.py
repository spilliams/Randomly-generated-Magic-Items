from random import seed, choice, randint

def oneChoice(dictionary, key):
    return choice(dictionary[key]).strip()

def generateName():
    values = {key: oneChoice(name_dictionary, key) for key in name_dictionary}
    pattern = choice(name_patterns)
    return pattern.format(**values).strip()

def chooseValueReroll(key):
    value = [oneChoice(flavor_dictionary, key)]
    if "reroll" in value[0]:
        count = value[0].split(" ")[1]
        value = []
        for i in range(0,int(count)):
            reroll = oneChoice(flavor_dictionary, key)
            while "reroll" in reroll:
                reroll = oneChoice(flavor_dictionary, key)
            value.append(reroll)
    return value

def printItem(item):
    print("")
    joiner = "\n\t\t\t"
    print("Name:\t\t\t"+item["name"])
    print("Creator/Intended user:\t"+joiner.join(item["creators"]))
    print("Historic details:\t"+joiner.join(item["historicdetails"]))
    print("Minor Properties:\t"+joiner.join(item["minorproperties"]))
    print("Quirks:\t\t\t"+joiner.join(item["quirks"]))
    print("")
def printInstructions():
    print("1: reroll Name")
    print("2: reroll Creator")
    print("3: reroll Historic Details")
    print("4: reroll Minor Properties")
    print("5: reroll Quirks")
    print("6: write-in the Name")
    print("7: write-in the Creator")
    print("8: write-in the Historic Details")
    print("9: write-in the Minor Properties")
    print("10: write-in the Quirks")
    print("h: Help (print this menu)")
    print("(blank): redo previous command. If there is no previous command, exit")
    print("anything else: exit")

def generateItem():
    item = {key: chooseValueReroll(key) for key in flavor_dictionary}
    item["name"] = generateName()
    return item

seed()

# set up name dictionary
name_dictionary = {}
name_sources = ["concrete_noun","title","adjective","abstract_noun"]
for source in name_sources:
    with open ("names/{}.txt".format(source)) as f:
        name_dictionary[source] = f.readlines()
with open ("names/patterns.txt") as file:
    name_patterns = file.readlines()

# set up flavor dictionary
flavor_dictionary = {}
flavor_sources = ["creators","historicdetails","minorproperties","quirks"]
for source in flavor_sources:
    with open ("flavor/{}.txt".format(source)) as f:
        flavor_dictionary[source] = f.readlines()

go = True
lastInstruction = ""
item = generateItem()
printedInstructions = False

while go:
    printItem(item)
    if not printedInstructions:
        printInstructions()
        printedInstructions = True
    
    try:
        instruction = raw_input('command? ')
    except SyntaxError:
        instruction = ""
        
    if instruction == "":
        instruction = lastInstruction
    lastInstruction = instruction
    if instruction == "1":
        item["name"] = generateName();
    elif instruction == "2" or instruction == "3" or instruction == "4" or instruction == "5":
        key = flavor_sources[int(instruction)-2]
        item[key] = chooseValueReroll(key)
    elif instruction == "H" or instruction == "h":
        printInstructions()
    elif instruction == "6":
        item["name"] = raw_input("Write-in: ")
    elif instruction == "7" or instruction == "8" or instruction == "9" or instruction == "10":
        key = flavor_sources[int(instruction)-7]
        item[key] = raw_input("Write-in: ")
    else:
        go = False
    