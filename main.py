from flask import Flask
from flask_restful import Resource, Api
from flask import request, jsonify
from src.train_model import train_model
import numpy as np


app = Flask(__name__)
api = Api(app)

MODEL = train_model()



@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name', "")

    return f"<h1 style='color:red'>hello {name} </h1>"


@app.route('/')
@app.route('/index')
def home():
    return "aplikacja ze srodowiskiem produkcyjnym API"


@app.route('/predict')
def predict():
    sepal_length = request.args.get('sepal_length')
    petal_length = request.args.get('petal_length')

    X = np.array([np.float(sepal_length), np.float(petal_length)])
    prediction = str(float(MODEL.predict(X)))

    return jsonify({'predicted_class': prediction})


class Main(Resource):
    def get(self):
        return jsonify("to jest tresc")


if __name__ == '__main__':
    app.run(port=5004, host="0.0.0.0")
