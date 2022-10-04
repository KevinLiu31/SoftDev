# your heading here

from flask import Flask
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
banana = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?
@banana.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return getDevo(krewes)  # Q4: Will this appear anywhere? How u know?

banana.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:

QCC:
0. We have seen it while using Java constructors for objects.
1. It is the director and path to the file
2. It will print to the terminal
3. It will print the value __name__
4. Yes it will print whereever "print(__name__)" will print to
5. It is similar to a main method/ a driver when used to run a series of command
...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''
