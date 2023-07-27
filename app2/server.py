from flask import Flask
  2 
  3 # create flask app
  4 app = Flask(__name__)
  5 
  6 
  7 # add all the routes
  8 
  9 @app.route("/", methods=["GET"])
 10 def root():
 11     return "welcome to python flask"
 12 
 13 
 14 # run the application
 15 app.run(host="0.0.0.0", port=4000, debug=True)
~                                 
