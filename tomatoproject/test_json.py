#!/usr/bin/env python3
"""Test JSON serialization of prediction results"""

import os
import sys
import django
from django.conf import settings

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tomato_disease.settings')
sys.path.append('/home/ogega/Projects/Tomato_Disease_Detection-main/tomatoproject')
django.setup()

import json
from PIL import Image
from tomato_app.ml_model import predictor
from tomato_app.disease_info import disease_info

def test_prediction():
    """Test the prediction and JSON serialization"""
    try:
        # Create a simple test image
        test_img = Image.new('RGB', (224, 224), color='green')
        
        # Get prediction
        result = predictor.predict(test_img)
        print("✅ Prediction result:", json.dumps(result, indent=2, default=str))
        
        # Test disease info serialization
        if result.get('success'):
            disease_name = result['predicted_class']
            disease_data = disease_info.get(disease_name, {})
            print(f"\n✅ Disease info for {disease_name}:")
            print(json.dumps(disease_data, indent=2, default=str))
            
            # Test the API response format
            api_response = {
                'success': True,
                'prediction': {
                    'class': str(result['predicted_class']),
                    'confidence': float(result['confidence']),
                    'disease_info': {str(k): str(v) for k, v in disease_data.items()}
                },
                'all_predictions': [
                    {
                        'disease': str(pred.get('disease', '')),
                        'confidence': float(pred.get('confidence', 0)),
                        'is_predicted': bool(pred.get('is_predicted', False))
                    }
                    for pred in result.get('all_predictions', [])
                ]
            }
            
            print(f"\n✅ API response (JSON serializable):")
            print(json.dumps(api_response, indent=2))
            print("\n🎉 JSON serialization test PASSED!")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_prediction()