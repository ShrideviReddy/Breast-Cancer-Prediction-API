import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
model = pickle.load(open('model1.pkl', 'rb'))
ALLOWED_HOSTS = ['*']

@app.route('/')
def home():
    return render_template('appui.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction[0]

    return render_template('appui.html', prediction_text='Predicted Class:  {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
