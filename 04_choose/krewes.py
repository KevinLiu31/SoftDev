import random as random
from subprocess import list2cmdline
from xml.dom.minidom import AttributeList
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

def gameTime(a):
    print("Let's play a game!\n")
    length = 
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
    print("You are given " + str(n) + "names\n")
    list2 = 
    a = 0
    b = 0
    c = 0
    alist ={}
    blist ={}
    clist ={}
    while()
    dicOfnum = {2:a, 7:b, 8:c}
    print("You'll be given a dictionary of the perid and the number of people in each period\n")
    
    next = input("")
    
gameTime()

