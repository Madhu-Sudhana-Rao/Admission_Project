# app.py
from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('Admission.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve form data
        gre = float(request.form['gre'])
        toefl = float(request.form['toefl'])
        rating = float(request.form['rating'])
        sop = float(request.form['sop'])
        lor = float(request.form['lor'])
        cgpa = float(request.form['cgpa'])
        research = float(request.form['research'])

        # Prepare input array
        input_data = np.array([[gre, toefl, rating, sop, lor, cgpa, research]])

        # Make prediction
        prediction = model.predict(input_data)
        prediction = round((prediction[0][0])/100,2)

        return render_template('index.html', prediction=f"Predicted Chance of Admission: {prediction * 100}%")
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
