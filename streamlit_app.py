import streamlit as st
import numpy as np
from tensorflow import keras
from PIL import Image

@st.cache_resource
def load_model():
    return keras.models.load_model('model/CNN_model.keras')

def preprocess_image(image):
    img = image.convert('RGB')
    img = img.resize((224, 224))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array / 255.0

st.set_page_config(page_title="Image Classification", layout="wide")
st.title("Breast cancer detection")

model = load_model()

uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image')
    preprocessed_image = preprocess_image(image)

    prediction = model.predict(preprocessed_image)
    predicted_class = np.argmax(prediction, axis=1)[0]

    st.subheader("Prediction Results")
    cm_labels = ['MALIGNANT', 'BENIGN']
    st.write(f"Predicted class: {cm_labels[predicted_class]}")
    st.write(f"Confidence: {prediction[0][predicted_class]:.2f}")


else:
    st.info("Please upload a PNG or JPG image file.")
