# your heading here
import random
from flask import Flask
app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?
def random1():
    list_of_string = {"Hello", "Bought", "Banana"}
    return random.choice(list_of_string)
@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "Anson is weird" # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


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
