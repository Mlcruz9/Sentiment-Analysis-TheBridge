from flask import Flask, jsonify, request
import os
import pickle

os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def hello():
    return "Bienvenido a mi API de Sentiment Analysis"


@app.route('/api/v1/predict', methods=['GET'])
def predict():

    model = pickle.load(open('finished_model.model','rb'))
    tweet = request.args.get('str', None)

    if tweet is None:
        return "Introduce tu cuerpo de texto"
    else:
        prediction = model.predict([tweet])
    
    return jsonify({'predictions': prediction[0]})