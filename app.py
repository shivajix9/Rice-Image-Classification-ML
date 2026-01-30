import streamlit as st
import cv2
import numpy as np
import joblib
from skimage.feature import hog
from PIL import Image
import base64


# Load trained objects
dt_model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")
le = joblib.load("label_encoder.pkl")

st.set_page_config(page_title="Decision Tree Image Classifier")

st.title("🌾 Rice Image Classification using best ML model")
st.write("HOG feature extraction +  best ML model")

#bg image
with open("bag.jpg", "rb") as f:
    img = base64.b64encode(f.read()).decode()


uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)
#bg image
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{img}");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

if uploaded_file is not None:
    # Display image
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",width=300)

    # Convert to OpenCV format
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # 🔴 MUST MATCH TRAINING PREPROCESSING 🔴
    img = cv2.resize(img, (64, 64))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # HOG feature extraction (same as training)
    features = hog(
        gray,
        orientations=9,
        pixels_per_cell=(8, 8),
        cells_per_block=(2, 2),
        block_norm='L2-Hys'
    )

    # Scale features
    features = scaler.transform([features])

    # Prediction
    prediction = dt_model.predict(features)
    class_name = le.inverse_transform(prediction)

    st.success(f"✅ Predicted Class: **{class_name[0]}**")