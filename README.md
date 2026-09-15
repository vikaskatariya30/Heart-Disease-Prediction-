# Heart Disease Prediction

A Streamlit web app that predicts whether a patient is likely to have heart disease based on clinical measurements, using a machine learning model trained on the classic UCI/Cleveland Heart Disease dataset.

## Overview

The app collects a patient's clinical data through a simple form and returns an instant prediction — likely or unlikely to have heart disease — using a pre-trained classification model.

## Features

- Interactive Streamlit UI for entering patient details
- Inputs: age, sex, chest pain type, resting blood pressure, serum cholesterol, fasting blood sugar, resting ECG results, maximum heart rate achieved, exercise-induced angina, and ST depression (oldpeak)
- Categorical inputs are automatically encoded to match the model's expected features
- Real-time prediction with a clear success/error message

## Project Structure

```
Heart-Disease-Prediction-/
├── app.py                 # Streamlit application
├── model.pkl              # Trained classification model
├── scaler.pkl             # Fitted feature scaler
├── model_training.ipynb   # Notebook used to train and export the model
├── LICENSE
└── README.md
```

## Tech Stack

- Python
- Streamlit
- Pandas
- Scikit-learn (model training/scaling)

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
git clone https://github.com/vikaskatariya30/Heart-Disease-Prediction-.git
cd Heart-Disease-Prediction-
pip install streamlit pandas scikit-learn
```

### Run the App

```bash
streamlit run app.py
```

Then open the local URL shown in your terminal (usually `http://localhost:8501`).

## How It Works

1. The user enters patient details through the Streamlit form.
2. Categorical fields (sex, chest pain type, fasting blood sugar, resting ECG, exercise-induced angina) are converted into the one-hot encoded features the model expects.
3. The feature vector is scaled using the saved `scaler.pkl`.
4. The trained model (`model.pkl`) predicts the outcome, and the app displays whether the patient is likely or unlikely to have heart disease.

## Model Training

The model was trained and exported in `model_training.ipynb`, which covers data preprocessing, encoding, feature scaling, and model fitting.

## Disclaimer

This project is for educational purposes only and is **not** a substitute for professional medical diagnosis. Always consult a qualified healthcare provider for medical advice.

## License

This project is licensed under the Apache-2.0 License. See the [LICENSE](LICENSE) file for details.

## Author

**Vikas Katariya**
GitHub: [@vikaskatariya30](https://github.com/vikaskatariya30)