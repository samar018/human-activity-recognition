"""
Flask API for Human Activity Recognition
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from PIL import Image
import io
import tensorflow as tf
import os

app = Flask(__name__)
CORS(app)

# =========================
# CONFIG
# =========================

MODEL_PATH = r"E:\workspace\ML\Bangladesh\BAIUST\posture (2)\posture\posture\my_model.keras"
IMAGE_SIZE = 128

ACTIVITIES = [
    'Walking', 'Running', 'Standing', 'Sitting', 'Lying Down',
    'Climbing Stairs', 'Descending Stairs', 'Jumping', 'Cycling',
    'Stretching', 'Bending', 'Reaching', 'Pushing', 'Pulling', 'Lifting'
]

# =========================
# LOAD MODEL
# =========================

model = None

try:
    if os.path.exists(MODEL_PATH):
        model = tf.keras.models.load_model(MODEL_PATH)

        # ✅ Freeze everything (safe inference)
        for layer in model.layers:
            layer.trainable = False

        print("✅ Model loaded successfully")
    else:
        print("❌ Model file not found:", MODEL_PATH)

except Exception as e:
    print("❌ Error loading model:", str(e))


# =========================
# PREPROCESSING
# =========================

def preprocess_image(image):
    """Preprocess image for prediction"""

    # Ensure RGB
    image = image.convert('RGB')

    # Resize
    image = image.resize((IMAGE_SIZE, IMAGE_SIZE))

    # Convert to array
    img_array = np.array(image).astype('float32')

    # ✅ IMPORTANT: SAME preprocessing as training
    img_array = tf.keras.applications.efficientnet.preprocess_input(img_array)

    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    return img_array


# =========================
# ROUTES
# =========================

@app.route('/')
def home():
    return "✅ Human Activity Recognition API is running!"


@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None
    })


@app.route('/api/activities', methods=['GET'])
def get_activities():
    return jsonify({
        'activities': ACTIVITIES,
        'count': len(ACTIVITIES)
    })


@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        # Check file
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400

        file = request.files['image']

        # Read image
        image = Image.open(io.BytesIO(file.read()))

        # Preprocess
        processed_image = preprocess_image(image)

        # Prediction
        if model is None:
            return jsonify({'error': 'Model not loaded'}), 500

        # 🔥 CRITICAL FIX → NO RANDOMNESS
        predictions = model(processed_image, training=False).numpy()

        prediction_idx = int(np.argmax(predictions[0]))
        confidence = float(predictions[0][prediction_idx])

        # All predictions
        all_preds = {
            ACTIVITIES[i]: round(float(pred) * 100, 2)
            for i, pred in enumerate(predictions[0])
        }

        # Response
        return jsonify({
            'predicted_class': ACTIVITIES[prediction_idx],
            'confidence': round(confidence * 100, 2),
            'all_predictions': all_preds
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# =========================
# RUN
# =========================

if __name__ == '__main__':
    print("\n🚀 Starting Human Activity Recognition API...")
    print("📍 URL: http://localhost:5000")
    print("\nEndpoints:")
    print("  GET  /")
    print("  GET  /api/health")
    print("  POST /api/predict")
    print("  GET  /api/activities\n")

    app.run(debug=True, host='0.0.0.0', port=5000)
    