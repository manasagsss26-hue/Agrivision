from flask import Flask, render_template, request, redirect, send_from_directory, url_for
import numpy as np
import json
import uuid
import tensorflow as tf
import os

app = Flask(__name__)

# Load model
model = tf.keras.models.load_model("models/plant_disease_recog_model_pwp.keras")

# Labels
label = [
 'Apple__Apple_scab','Apple_Black_rot','Apple_Cedar_apple_rust','Apple__healthy',
 'Background_without_leaves','Blueberry__healthy','Cherry__Powdery_mildew',
 'Cherry__healthy','Corn_Cercospora_leaf_spot Gray_leaf_spot','Corn__Common_rust',
 'Corn__Northern_Leaf_Blight','Corn_healthy','Grape__Black_rot',
 'Grape__Esca(Black_Measles)','Grape__Leaf_blight(Isariopsis_Leaf_Spot)','Grape___healthy',
 'Orange__Haunglongbing(Citrus_greening)','Peach__Bacterial_spot','Peach__healthy',
 'Pepper,bell_Bacterial_spot','Pepper,_bell_healthy','Potato__Early_blight',
 'Potato__Late_blight','Potato_healthy','Raspberry_healthy','Soybean__healthy',
 'Squash__Powdery_mildew','Strawberry_Leaf_scorch','Strawberry__healthy',
 'Tomato__Bacterial_spot','Tomato_Early_blight','Tomato__Late_blight',
 'Tomato__Leaf_Mold','Tomato_Septoria_leaf_spot','Tomato__Spider_mites Two-spotted_spider_mite',
 'Tomato__Target_Spot','Tomato_Tomato_Yellow_Leaf_Curl_Virus','Tomato__Tomato_mosaic_virus',
 'Tomato___healthy'
]

# Load JSON descriptions
with open("plant_disease.json", 'r') as file:
    plant_disease = json.load(file)

# Create folder
if not os.path.exists("uploadimages"):
    os.makedirs("uploadimages")

@app.route('/uploadimages/<path:filename>')
def uploaded_images(filename):
    return send_from_directory('./uploadimages', filename)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

def extract_features(image):
    image = tf.keras.utils.load_img(image, target_size=(160,160))
    image = tf.keras.utils.img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image

def model_predict(image_path):
    img = extract_features(image_path)
    prediction = model.predict(img)
    predicted_label = label[np.argmax(prediction)]
    return predicted_label

@app.route('/upload/', methods=['POST','GET'])
def uploadimage():
    if request.method == "POST":
        image = request.files['img']

        temp_id = uuid.uuid4().hex
        filename = f"temp_{temp_id}_{image.filename}"
        save_path = f"uploadimages/{filename}"

        image.save(save_path)

        prediction = model_predict(save_path)

        return render_template(
            'home.html',
            result=True,
            imagepath=url_for('uploaded_images', filename=filename),
            prediction=prediction
        )

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
