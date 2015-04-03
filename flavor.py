from random import seed, choice, randint

def oneChoice(key):
    return choice(dictionary[key]).strip()

def chooseValueReroll(key):
    value = [oneChoice(key)]
    if "reroll" in value[0]:
        print("reroll!")
        count = value[0].split(" ")[1]
        value = []
        print("count "+count)
        for i in range(0,int(count)):
            reroll = oneChoice(key)
            while "reroll" in reroll:
                reroll = oneChoice(key)
            value.append(reroll)
    return value

def printValues():
    print("")
    joiner = "\n\t\t\t"
    print("Creator/Intended user:\t"+joiner.join(values["creators"]))
    print("Historic details:\t"+joiner.join(values["historicdetails"]))
    print("Minor Properties:\t"+joiner.join(values["minorproperties"]))
    print("Quirks:\t\t\t"+joiner.join(values["quirks"]))
    print("")

def printInstructions():
    print("1: reroll Creator")
    print("2: reroll Historic Details")
    print("3: reroll Minor Properties")
    print("4: reroll Quirks")
    try:
        return input('command? ')
    except SyntaxError:
        return ""

seed()

dictionary = {}
list_of_sources=["creators","historicdetails","minorproperties","quirks"]
for source in list_of_sources:
    with open ("flavor/{}.txt".format(source)) as f:
        dictionary[source] = f.readlines()

values = {key: chooseValueReroll(key) for key in dictionary}

go = True
lastInstruction = ""

while go:
    printValues()
    instruction = printInstructions()
    if instruction == "":
        instruction = lastInstruction
    lastInstruction = instruction
    if instruction == 1 or instruction == 2 or instruction == 3 or instruction == 4:
        key = list_of_sources[instruction-1]
        values[key] = chooseValueReroll(key)
    else:
        go = False