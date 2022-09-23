import random as random
""" Undesirable
 SoftDev
 K01 -- Krewes
 2022-09-22
 time spent:

 DISCO: How to use rangRange. The value contained in each key value pair do not have to be of uniform length.

 QCC: What other way are there to generate random number. How does older computers generate random number using
 limited resources.

 OPS SUMMARY:Choose a random key, and then choose a random value in the value associated with the key.
 Put all the keys of the dictionary in a list. Choose a random number between 0 and the length of the 
 dictionary, and then save the value of the
 key associated with that number as a list variable: RngResult.

"""
#krewes = {2:["A", "B"], 7:["C", "D", "E"], 8:["F", "G"]}
krewes = {
           2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY"],
           7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
           8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "wanying"]
         }
resaurant = {}
def getDevo(a):
    keys = list(a)
    RngResult = random.randrange(len(a))
    keyResult = keys[RngResult]
    resultList = a[keyResult]
    RngResult = random.randrange(len(resultList))
    resultValue = resultList[RngResult]
    return resultValue

print(getDevo(krewes))
