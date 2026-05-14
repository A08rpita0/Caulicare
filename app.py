from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

# Load the trained model
MODEL_PATH = "./model1.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Define class labels
class_names = ["Bacterial spot rot", "Black Rot", "Downy Mildew","No disease"] 

# Preprocess the image
def preprocess_image(image):
    image = image.resize((256, 256))  
    image = np.array(image) / 255.0  
    image = np.expand_dims(image, axis=0)  
    return image

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

def predict_(model, img):
    img_array=tf.keras.preprocessing.image.img_to_array(img)
    img_array=tf.expand_dims(img_array,0)

    predictions=model.predict(img_array)
    print(predictions)
    predicted_class=class_names[np.argmax(predictions[0])]
    confidence=round(100*(np.max(predictions[0])),2)
    return predicted_class, confidence

@app.route("/predict", methods=["POST"])
def predict():
    # Get the uploaded file
    file = request.files["image"]
    if not file:
        return render_template("index.html", error="Please upload an image.")
    
    # Preprocess and predict
    image = Image.open(file)
    # processed_image = preprocess_image(image)
    # prediction = model.predict(processed_image)
    # predicted_class = CLASS_NAMES[np.argmax(prediction)]
    
    prediction ,_ = predict_(model, image)  # Get predictions
    print(prediction)
    
    return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
