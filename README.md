
# CauliCare 🌿

CauliCare is a cutting-edge web application designed to assist farmers and agricultural enthusiasts in diagnosing diseases in cauliflower crops using deep learning technology. With just an image of a cauliflower leaf, users can identify potential diseases and take timely action to protect their crops.








https://github.com/user-attachments/assets/e07ed2ad-b957-4501-9f7a-2c23b967aa76



## Features

### 📎 Image Upload
- Seamlessly upload images of cauliflower leaves directly from your device.
- Supported formats: JPEG, PNG, and more.

### 🌱 Disease Prediction
- Harness the power of advanced deep learning models to predict common cauliflower diseases.
- Fast and accurate results to aid in effective crop management.

### 🔧 User-Friendly Interface
- Intuitive and visually appealing design tailored for ease of use.
- Mobile-friendly layout ensures accessibility across devices.

## How It Works
1. **Upload an Image**: Choose a clear image of the affected cauliflower leaf.
2. **Model Analysis**: The backend processes the image using a trained deep learning model.
3. **View Results**: The app displays the predicted disease along with confidence levels.

## Tech Stack

### Frontend
- **HTML & CSS**: For a clean and responsive user interface.

### Backend
- **Flask (Python)**: Lightweight and efficient web framework to handle requests and integrate the ML model.

### Machine Learning
- **TensorFlow/Keras**: Deep learning frameworks used to train and deploy the disease prediction model.

## Installation

### Prerequisites
- Python 3.8 or later
- pip (Python package manager)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/A08rpita/caulicare.git
   cd caulicare
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Application**:
   ```bash
   flask run
   ```
5. **Access the App**:
   Open `http://127.0.0.1:5000` in your web browser.

## Usage

- Navigate to the upload page.
- Select an image of the cauliflower leaf.
- Click on the "Predict" button to get the disease diagnosis.
- View the results and recommended actions.

## Dataset

The model is trained on a curated dataset of cauliflower leaf images containing samples of healthy and diseased leaves. If you'd like to contribute to the dataset, please reach out.

## Future Enhancements

- Add support for multilingual interfaces to cater to a diverse user base.
- Expand the model to diagnose diseases in other vegetables and crops.
- Include detailed guides for disease prevention and treatment.











