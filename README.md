PIN Sensor Side-Channel Prediction Webapp

This repository contains a web application for training and deploying machine learning models to analyze side-channel sensor data (such as accelerometer and gyroscope readings) to predict PIN inputs.

The project is inspired by and builds upon prior research in side-channel attacks leveraging motion sensors, such as the work from https://github.com/matteonerini/pin-side-channel-attacks.

Disclaimer / Research Context

This tool is intended for research, educational, and experimental purposes only. The effectiveness of side-channel PIN inference depends on numerous factors including sensor quality, device hardware, user behavior, and environmental noise. Real-world applicability may vary significantly.

Getting Started — Installation & Usage

Follow these instructions to run the project locally on your machine.

1. Clone the repository
git clone https://github.com/Elnimo-00/Pin-sensor-prediction-webapp.git

cd Pin-sensor-prediction-webapp

3. (Optional but recommended) Create and activate a Python virtual environment

On macOS/Linux:

python3 -m venv venv

source venv/bin/activate


On Windows (PowerShell):

python -m venv venv

venv\Scripts\Activate.ps1

3. Install required dependencies

The main dependencies are listed in the backend/requirements.txt file:

pip install -r backend/requirements.txt

4. Start the backend server

Navigate to the backend directory and run the FastAPI server with auto-reload enabled for development:

cd backend

uvicorn app:app --reload

5. Access the web application

Once the server is running, open your browser and go to:

http://localhost:8000


You should see the web interface for training models and analyzing PIN side-channel data.

Project Structure Overview

backend/ — Contains the FastAPI backend server code and ML model training logic.



data/ — (Optional) Folder to store sensor datasets for training and evaluation.

requirements.txt — Python dependencies for backend.

Features

Upload and preprocess motion sensor data (accelerometer and gyroscope).

Train various ML models to infer PINs from side-channel signals.

Evaluate model accuracy and performance metrics.

Interactive web UI for ease of use.

Notes

Ensure your Python environment is 3.7+ for compatibility.

Adjust port numbers or configuration in uvicorn command if needed.

The project is under active development; contributions and feedback are welcome.
