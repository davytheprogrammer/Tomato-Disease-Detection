"""
Machine Learning Model Handler for Tomato Disease Detection
"""
import os
from pathlib import Path
from django.conf import settings
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image


class TomatoDiseasePredictor:
    """Singleton class to handle model loading and predictions"""
    _instance = None
    _model = None
    _class_names = [
        "Bacterial Spot", "Early Blight", "Late Blight", "Leaf Mold",
        "Septoria Leaf Spot", "Two-Spotted Spider Mite", "Target Spot",
        "Tomato Yellow Leaf Curl Virus", "Tomato Mosaic Virus", "Healthy Plant"
    ]

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._model is None:
            self.load_model()

    def load_model(self):
        """Load the trained model"""
        try:
            model_path = Path(settings.MODEL_PATH)
            if model_path.exists():
                self._model = tf.keras.models.load_model(model_path)
                print(f"Model loaded successfully from {model_path}")
            else:
                # Look for model in parent directory (original structure)
                alt_path = Path(settings.BASE_DIR).parent / 'models' / 'best_mobilenet_finetuned.keras'
                if alt_path.exists():
                    self._model = tf.keras.models.load_model(alt_path)
                    print(f"Model loaded from alternative path: {alt_path}")
                else:
                    raise FileNotFoundError(f"Model not found at {model_path} or {alt_path}")
        except Exception as e:
            print(f"Error loading model: {e}")
            self._model = None

    def predict(self, img: Image.Image) -> dict:
        """
        Predict disease from image

        Args:
            img: PIL Image object

        Returns:
            Dictionary with prediction results
        """
        if self._model is None:
            return {"success": False, "error": "Model not loaded"}

        try:
            # Preprocess image
            img_resized = img.resize((224, 224))
            img_array = image.img_to_array(img_resized)
            img_array = np.expand_dims(img_array, axis=0) / 255.0

            # Make prediction
            predictions = self._model.predict(img_array, verbose=0)[0]

            # Get top prediction
            pred_idx = np.argmax(predictions)
            pred_name = self._class_names[pred_idx]
            confidence = float(predictions[pred_idx])

            # Get all predictions with confidence scores
            all_predictions = [
                {
                    'disease': str(name),
                    'confidence': float(score),
                    'is_predicted': bool(i == pred_idx)
                }
                for i, (name, score) in enumerate(zip(self._class_names, predictions))
                if float(score) > 0.01  # Filter out very low confidence predictions
            ]

            # Sort by confidence
            all_predictions.sort(key=lambda x: x['confidence'], reverse=True)

            return {
                'success': True,
                'predicted_class': str(pred_name),
                'confidence': float(confidence),
                'all_predictions': all_predictions
            }

        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }


# Global instance
predictor = TomatoDiseasePredictor()
