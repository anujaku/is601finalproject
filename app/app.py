"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.internet_story_controller import InternetStoryController
from app.controllers.early_innovations_controller import EarlyInnovationsController
from app.controllers.home_computers_controller import HomeComputersController
from app.controllers.pylint_controller import PylintController
from app.controllers.aaa_controller import AAAController
from app.controllers.oops_controller import OOPSController
from app.controllers.design_pattern_controller import DesignPatternController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/internetstory", methods=['GET'])
def internetstory_get():
    return InternetStoryController.get()

@app.route("/earlyinnovations", methods=['GET'])
def earlyinnovations_get():
    return EarlyInnovationsController.get()

@app.route("/homecomputers", methods=['GET'])
def homecomputers_get():
    return HomeComputersController.get()

@app.route("/pylint", methods=['GET'])
def pylint_get():
    return PylintController.get()

@app.route("/aaa", methods=['GET'])
def aaa_get():
    return AAAController.get()

@app.route("/oopsconcepts", methods=['GET'])
def oopsconcepts_get():
    return OOPSController.get()

@app.route("/designpatterns", methods=['GET'])
def designpatterns_get():
    return DesignPatternController.get()
