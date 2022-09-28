import random as random
""" Undesirable
 SoftDev
 K01 -- Krewes
 2022-09-22
 time spent:

 DISCO: How to use rangRange. The value contained in each key value pair do not have to be of uniform length.
 Some ways to generate RNG:
 randint(start, stop) - returns a value between start and stop.
 randrange(stop) - returns a value between 0 and stop, non inclusive of stop.
 getrandbits(n) - returns a value between 0 and 2^n - 1.
 choice(seq) - returns a random value from a sequence. doesn't work with dictionary.

 QCC: What other way are there to generate random number. How does older computers generate random number using
 limited resources.

 OPS SUMMARY: Put all the keys of the dictionary in a list. Choose a random number between 0 and the length
 of the dictionary, then from the list of keys, pull the key associated with the index that was given by the rng.


"""
#krewes = {2:["A", "B"], 7:["C", "D", "E"], 8:["F", "G"]}
krewes = {
           2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY"],
           7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
           8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "wanying"]
         }
resaurant = {}
def getDevo(a):
    ans = ""
    #puts all the keys in the dictionary into a list
    keys = list(a)
    #return an rng which will be used to take a value based on the index of the list of keys
    RngResult = random.randint(0, len(a) - 1)
    keyResult = keys[RngResult]
    #adds the period which is returned from the list of keys
    ans += "period: " + str(keyResult)
    #grabs the value associated with the randomly selected key
    resultList = a[keyResult]
    #take a RNG between 0 and the length of the list that is the value of the key.
    RngResult = random.randrange(len(resultList))
    # chooses a random element from the list
    resultValue = resultList[RngResult]
    ans += ", Name: " + str(resultValue)
    return ans
def getDevo2(a):
    ans = ""
    #puts all the keys in the dictionary into a list
    keys = list(a)
    #picks a random key from the list of keys
    randomKey = random.choice(keys)
    ans += "period: " + str(randomKey)
    #return a random value from the list associated with the key.
    ans += ", Name: " + random.choice(a[randomKey])
    return ans
print("way 1: " + getDevo(krewes))
print("way 2: " + getDevo2(krewes))
def getDevoHelp(a):
    ans = ""
    #puts all the keys in the dictionary into a list
    keys = list(a)
    #picks a random key from the list of keys
    randomKey = random.choice(keys)
    ans += "period: " + str(randomKey)
    #return a random value from the list associated with the key.
    return [randomKey, random.choice(a[randomKey])]
print(getDevoHelp(krewes))
def gameTime(a):
    counter = 0;
    print("Let's play a game!\n")
    print("How to Play: Imagine memorizing but not really\n")
    isValue = False
    while (not isValue):
        give = input("First give me a number between 1-106\n")
        try:
            n = int(give)
            if(107>n>0):
                isValue = True
            else:
                print("Value is not between 1-106")
        except ValueError:
            print("Please enter a value")
    print("You are given " + str(n) + " names\n")
    dicOfnum = {2:0, 7:0, 8:0}
    NameofNum = {2:[], 7:[], 8:[]}
    allName = []
    for x in range(n):
         tempList = getDevoHelp(a)
         a[tempList[0]].remove(tempList[1])
         allName.append(tempList[1])
         dicOfnum[tempList[0]] = dicOfnum[tempList[0]] + 1
         NameofNum[tempList[0]].append(tempList[1])
    print("You'll be given a dictionary of the period and the number of people in each period\n")
    print("And a list of names that you must match each period\n")
    print("When you are ready press enter")
    next = input("")
    print(dicOfnum)
    print("name")
    print(allName)
    print("Press enter to continue")
    next = input("")
    print("Your goal is now to enter a name, and then enter a period")
    while(len(allName) > 0):
        print(dicOfnum)
        print("name")
        print(allName)
        name = str(input("name of person"))
        while(not (name in allName)):
            print("please try again, make sure the name matches up with what is shown including CAPS!")
            name = str(input("name of person"))
        print("The name you select: " + name)
        period = int(input("period of person"))
        if(not (period in [2,7,8])):
            print("please select a proper period")
            period = int(input("period of person"))
        print("The option you put was: " + str(period) + ":" + name)
        if(name in NameofNum[period]):
            print("You are correct!")
            dicOfnum[period] = dicOfnum[period] - 1
            NameofNum[period].remove(name)
            allName.remove(name)
            next = input("Press enters")
        else:
            print("you are incorrect!")
            next = input("Press enters")
        counter+=1
        print("Amount of guesses: " + str(counter))
    print("Game Over: You achieved it in " + str(counter) + " guessse")
gameTime(krewes)
