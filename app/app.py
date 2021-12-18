"""A simple flask web app"""
from flask import Flask,render_template
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.pageone_controller import OriginController
from app.controllers.pagetwo_controller import FounderController
from app.controllers.pagethree_controller import Article1Controller
from app.controllers.pagefour_controller import Article2Controller

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/basicform", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/basicform", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/page1", methods=['GET'])
def origin_post():
    return OriginController.get()

@app.route("/page2", methods=['GET'])
def founder_post():
    return FounderController.get()

@app.route("/page3", methods=['GET'])
def article1_post():
    return Article1Controller.get()

@app.route("/page4", methods=['GET'])
def article2_post():
    return Article2Controller.get()
