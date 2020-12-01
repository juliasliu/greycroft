from flask import Flask
from flask import request
from flask_cors import CORS
import sys
import json

from .rev_analysis import *

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    CORS(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return "Hello World!"

    @app.route('/rev_analysis', methods=['POST'])
    def rev_analysis():
        # print("IS REQUEST JSON FORMAT", file=sys.stdout)
        # print(request.is_json, file=sys.stdout)
        # print("IS JSON FORMATTED CORRECTLY", file=sys.stdout)
        # print(request.get_json(force=True), file=sys.stdout)
        # print("WHAT IS JSON OBJECT", file=sys.stdout)
        # data = json.loads(request.get_json(force=True), strict=False)
        # data = request.get_json(force=True)
        # print(data["mrr"], file=sys.stdout)
        r = RevAnalysis(request.get_json()["arr"])
        mrr = r.mrr_by_customer()
        # rev_analysis = r.rev_analysis()
        # response.headers.add('Access-Control-Allow-Origin', '*')
        # print(mrr, file=sys.stdout)
        return mrr

    return app
