from django.shortcuts import render
from django.http import HttpResponse
from django.middleware.csrf import get_token
from django.contrib import messages
from PIL import Image
from .ml_model import predictor
from .disease_info import disease_info
import json

def client_side_upload(request):
    """Client-side upload page - NO DATABASE STORAGE, browser-only analysis"""
    return render(request, 'tomato_app/client_side_upload.html')

def debug_upload(request):
    """Debug upload page to test file uploads"""
    context = {
        'csrf_token': get_token(request)  # Ensure CSRF token is available
    }
    return render(request, 'tomato_app/debug_upload.html', context)

def simple_upload(request):
    """Enhanced simple upload page with beautiful UI - NO DATABASE STORAGE"""
    if request.method == 'POST':
        try:
            # Check if image was uploaded
            if 'image' not in request.FILES:
                messages.error(request, "Please select an image file to upload.")
                return redirect('simple_upload')
            
            uploaded_file = request.FILES['image']
            
            # Validate file type
            allowed_types = ['image/jpeg', 'image/jpg', 'image/png']
            if uploaded_file.content_type not in allowed_types:
                messages.error(request, "Please upload a JPG, JPEG, or PNG image file.")
                return redirect('simple_upload')
            
            # Validate file size (10MB max)
            if uploaded_file.size > 10 * 1024 * 1024:
                messages.error(request, "File size must be less than 10MB.")
                return redirect('simple_upload')
            
            # Process image
            img = Image.open(uploaded_file).convert('RGB')
            result = predictor.predict(img)
            
            if result.get('success'):
                disease_data = disease_info.get(result['predicted_class'], {})
                
                # Create temporary prediction object (not saved to DB)
                class TempPrediction:
                    def __init__(self, image_name, prediction, confidence):
                        self.image_name = image_name
                        self.prediction = prediction
                        self.confidence = confidence
                        self.created_at = None

                temp_prediction = TempPrediction(
                    image_name=uploaded_file.name,
                    prediction=result['predicted_class'],
                    confidence=result['confidence']
                )

                context = {
                    'image_name': uploaded_file.name,
                    'result': result,
                    'disease_info': disease_data,
                    'prediction': temp_prediction,
                }
                
                return render(request, 'tomato_app/simple_upload_enhanced.html', context)
            else:
                messages.error(request, f"Analysis failed: {result.get('error')}")
                
        except Exception as e:
            messages.error(request, f"Error processing image: {str(e)}")
            
    # GET request - show enhanced upload form
    return render(request, 'tomato_app/simple_upload_enhanced.html')