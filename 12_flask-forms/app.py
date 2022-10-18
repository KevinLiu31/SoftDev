# WeLoveTrees - Ravindra Mangar, Mahir Riki, Kevin Liu
# SoftDev
# K12: Take and Give
# 17-10-2022
# time spent: 2 hrs

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not.
TASK: Predict which...
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests.
Process results.
PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

@app.route("/" , methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    #request is the ip where you are getting data from.
    print(request)
    print("***DIAG: request.args ***")
    #the args is where the values of the form is stored in.
    print(request.args)
    #print(request.args[0])
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    #name, similar to printing request
    print(request.headers)
    return render_template( 'login.html' )
    #when press submit it updates the request.


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print(request.args.get('username'))
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template("response.html", username=request.form['username'], post_method=request.method)



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()