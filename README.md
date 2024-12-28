# Admission_Project

![Image Alt](https://github.com/Madhu-Sudhana-Rao/Admission_Project/blob/40ee9fe21fd8091072ff5ca52016798e6cd01a11/Screenshot%202024-12-28%20155346.png)

# Admission Predictor

## Overview
Admission Predictor is a machine learning-powered web application designed to estimate a student's likelihood of gaining admission to a university. By analyzing key academic and experiential parameters, this tool provides real-time, dynamic predictions to help students make informed decisions during the application process.

## Features
- **Dynamic Predictions:** Accurate predictions based on GRE scores, TOEFL scores, CGPA, SOP/LOR strength, and research experience.
- **User-Friendly Interface:** A professionally designed, responsive UI for a seamless user experience.
- **Machine Learning Integration:** Utilizes a TensorFlow/Keras-trained neural network for robust predictions.
- **Customizable Backend:** Built with Flask for ease of deployment and scalability.

## Tech Stack
- **Backend:** Flask (Python)
- **Machine Learning Framework:** TensorFlow, Keras
- **Frontend:** HTML5, CSS3
- **Tools & Libraries:** NumPy, Pandas, Pickle

## Installation
### Prerequisites
- Python 3.7 or above
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/admission-predictor.git
   cd admission-predictor
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open the app in your browser at `http://127.0.0.1:5000`.

## Usage
1. Input details such as GRE, TOEFL, and CGPA into the form.
2. Click "Predict" to calculate your admission likelihood.
3. View results dynamically on the web interface.


## How It Works
1. **Data Preprocessing:** User inputs are normalized for consistency.
2. **Prediction Model:** A trained neural network processes the data and provides predictions.
3. **Output Display:** Results are rendered dynamically on the frontend.

## Future Enhancements
- Support for additional parameters like extracurricular activities.
- Insights into areas of improvement based on predictions.
- Database integration for storing user data and predictions.

## Contributing
Contributions are welcome! If you'd like to contribute:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
- TensorFlow and Keras for machine learning tools.
- Bootstrap for design inspiration.

