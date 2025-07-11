#Import Flask
from flask import Flask


#Create Flask instance
app=Flask(__name__)


#Define function and route
@app.route('/') #Decorator to expose the function to flask #route is flask function which contents the url 
def home():
    return "Hello World! Vikash"

#Trigger the flask app
if __name__=='__main__': #Default python that runs initially internally
    app.run() #run is the flask function

# http://127.0.0.1:5000 (Protocal:Local Ip Address:Default port for flask)
# print(home())