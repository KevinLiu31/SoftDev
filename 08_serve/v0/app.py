# TNPG: PPP
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) # ...

@app.route("/") # ...
def hello_world():
    print(__name__) # ...
    return "No hablo queso!"  # ...

app.run()  # ...
                
# displays "no hablo queso!" on browser.
# prints __main__ to terminal