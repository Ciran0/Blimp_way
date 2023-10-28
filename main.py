
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/city/<depart>/<arrive>')
def city(depart, arrive):
    return depart+arrive
# main driver function


if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()