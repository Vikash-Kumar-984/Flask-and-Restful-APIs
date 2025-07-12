#Import Flask
from flask import Flask, jsonify, render_template 
#render_template is used to link html page


#Create Flask instance
app=Flask(__name__)


#Define function and route
# @app.route('/') #Decorator to expose the function to flask #route is flask function which contents the url 
# def home():
#     return "Hello World! Vikash"

#'/' , '/about' , '/data' : 3 Webpages Creation

# Exposing the function to flask
# @app.route('/')
# def home():
#     return "Welcome to the website! By Vikash Kumar"

@app.route('/about')
def about():
    # data = "This is the workspace for flask application"
    # return data
    return """<h1>About Us</h1><br>
              <h2>This is the workspace for flask application</h2><br>
              <h2>Debug is added at app.run(debug=True)</h2><br>
              <h3>Thank you for visiting our website</h3><br>"""

@app.route('/data')
def data():
    user_data = {"name":"Vikash Kumar",
                 "age":24}
    return jsonify(user_data) #Jsonify is recommended to use

# @app.route('/')
# def home_page():
#     name="Vikash"
#     return render_template('index.html',name=name) #to display from index.html file and take input from frontend to backend


@app.route('/',methods=['GET'])
def home():
    return "Welcome! Champ!!!"

#Trigger the flask app
if __name__=='__main__': #Default python that runs initially internally
    app.run(debug=True) #run is the flask function #debug=True will automatically detect the change and there is no need to reload again and again

# http://127.0.0.1:5000 (Protocal:Local Ip Address:Default port for flask)
# Request-Response Lifecycle of flask
# print(home())