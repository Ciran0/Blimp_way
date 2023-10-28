
import api_request_code
from flask import Flask, render_template

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cal')
def cal():
    return render_template('index2.html')


@app.route('/city/<depart>/<arrive>')
def city(depart, arrive):
    depart = api_request_code.get_coordinates(depart)
    arrive = api_request_code.get_coordinates(arrive)
    return api_request_code.get_points_between_coordinates(depart, arrive, 4)
# main driver function


if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
