import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import sys

# Load the model and class labels
model = tensorflow.keras.models.load_model('keras_model.h5')
with open('labels.txt', 'r') as f:
    class_names = [line.strip() for line in f.readlines()]

# Check if an image path is provided
if len(sys.argv) < 2:
    print("❌ Please provide an image path: python predict_image.py test_images/example.jpg")
    sys.exit()

image_path = sys.argv[1]

# Load and preprocess the image
image = Image.open(image_path).convert('RGB')
image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)
image_array = np.asarray(image)
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
data = np.expand_dims(normalized_image_array, axis=0)

# Make prediction
prediction = model.predict(data)[0]
predicted_index = np.argmax(prediction)
predicted_label = class_names[predicted_index]
confidence = prediction[predicted_index] * 100

# Output
print(f"{predicted_label} ({confidence:.2f}%)")
