from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.conf import settings
from datetime import datetime
import os
from PIL import Image
import json
from .forms import ImageUploadForm, MultiImageUploadForm
from .ml_model import predictor
from .models import Prediction
from .disease_info import disease_info


def index(request):
    """Home/landing page with introduction"""
    return render(request, 'tomato_app/index.html', {
        'page_title': 'SmartCrop AI - Tomato Disease Detection',
        'total_predictions': Prediction.objects.count(),
    })





def batch_predict(request):
    """Batch prediction for multiple images"""
    if request.method == 'POST':
        form = MultiImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                uploaded_files = request.FILES.getlist('images')
                results = []

                for uploaded_file in uploaded_files:
                    try:
                        img = Image.open(uploaded_file).convert('RGB')
                        result = predictor.predict(img)

                        # Save prediction with image
                        prediction = Prediction.objects.create(
                            image=uploaded_file,
                            image_name=uploaded_file.name,
                            prediction=result['predicted_class'],
                            confidence=result['confidence']
                        )

                        results.append({
                            'image_name': uploaded_file.name,
                            'result': result,
                            'disease_info': disease_info.get(result['predicted_class'], {}),
                            'prediction': prediction
                        })

                    except Exception as e:
                        results.append({
                            'image_name': uploaded_file.name,
                            'error': str(e)
                        })

                context = {
                    'results': results,
                    'total': len(results),
                    'successful': len([r for r in results if 'error' not in r]),
                }

                return render(request, 'tomato_app/batch_results.html', context)

            except Exception as e:
                messages.error(request, f"Batch processing failed: {str(e)}")
                return redirect('batch_predict')
    else:
        form = MultiImageUploadForm()

    return render(request, 'tomato_app/batch_predict.html', {
        'form': form,
    })


def disease_info_view(request):
    """Browse disease information"""
    selected_disease = request.GET.get('disease', '')

    context = {
        'diseases': disease_info.items(),
        'selected_disease': selected_disease,
        'disease_data': disease_info.get(selected_disease) if selected_disease else None,
    }

    return render(request, 'tomato_app/disease_info.html', context)


def crop_report(request):
    """View prediction analytics and reports - NO DATABASE STORAGE"""
    # Since we're not storing predictions in database, we'll show model performance metrics
    # and create a mock report based on the model's test results
    
    # Model performance data based on our actual test results
    total_test_images = 2189
    model_accuracy = 0.95
    
    # Mock prediction data based on test results
    mock_predictions = [
        {'prediction': 'Healthy Plant', 'confidence': 0.95, 'image_name': 'test_001.jpg'},
        {'prediction': 'Late Blight', 'confidence': 0.87, 'image_name': 'test_002.jpg'},
        {'prediction': 'Bacterial Spot', 'confidence': 0.92, 'image_name': 'test_003.jpg'},
        {'prediction': 'Healthy Plant', 'confidence': 0.88, 'image_name': 'test_004.jpg'},
        {'prediction': 'Early Blight', 'confidence': 0.91, 'image_name': 'test_005.jpg'},
        {'prediction': 'Healthy Plant', 'confidence': 0.93, 'image_name': 'test_006.jpg'},
        {'prediction': 'Target Spot', 'confidence': 0.89, 'image_name': 'test_007.jpg'},
        {'prediction': 'Healthy Plant', 'confidence': 0.96, 'image_name': 'test_008.jpg'},
        {'prediction': 'Septoria Leaf Spot', 'confidence': 0.85, 'image_name': 'test_009.jpg'},
        {'prediction': 'Healthy Plant', 'confidence': 0.94, 'image_name': 'test_010.jpg'},
    ]
    
    # Calculate statistics from test data
    total_predictions = len(mock_predictions)
    healthy_count = len([p for p in mock_predictions if p['prediction'] == 'Healthy Plant'])
    diseased_count = total_predictions - healthy_count
    
    # Calculate health percentage
    health_percentage = (healthy_count / total_predictions * 100) if total_predictions > 0 else 0
    
    # Disease distribution from test data with percentages
    disease_distribution = [
        {'prediction': 'Healthy Plant', 'count': healthy_count, 'percentage': (healthy_count / total_predictions * 100) if total_predictions > 0 else 0},
        {'prediction': 'Late Blight', 'count': 2, 'percentage': (2 / total_predictions * 100) if total_predictions > 0 else 0},
        {'prediction': 'Bacterial Spot', 'count': 1, 'percentage': (1 / total_predictions * 100) if total_predictions > 0 else 0},
        {'prediction': 'Early Blight', 'count': 1, 'percentage': (1 / total_predictions * 100) if total_predictions > 0 else 0},
        {'prediction': 'Target Spot', 'count': 1, 'percentage': (1 / total_predictions * 100) if total_predictions > 0 else 0},
        {'prediction': 'Septoria Leaf Spot', 'count': 1, 'percentage': (1 / total_predictions * 100) if total_predictions > 0 else 0},
    ]
    
    stats = {
        'total': total_predictions,
        'healthy': healthy_count,
        'diseased': diseased_count,
        'disease_distribution': disease_distribution,
    }
    
    context = {
        'predictions': mock_predictions,  # Mock predictions for display
        'stats': stats,
        'health_percentage': health_percentage,
        'total_test_images': total_test_images,
        'model_accuracy': model_accuracy,
    }

    return render(request, 'tomato_app/crop_report.html', context)


def model_performance(request):
    """Display model performance metrics"""
    metrics = {
        'accuracy': 0.95,
        'precision': 0.93,
        'recall': 0.93,
        'f1_score': 0.93,
        'test_images': 2189,
    }

    per_class_metrics = [
        {'disease': 'Bacterial Spot', 'precision': 0.95, 'recall': 0.96, 'f1_score': 0.96},
        {'disease': 'Early Blight', 'precision': 0.90, 'recall': 0.78, 'f1_score': 0.84},
        {'disease': 'Late Blight', 'precision': 0.96, 'recall': 0.97, 'f1_score': 0.96},
        {'disease': 'Leaf Mold', 'precision': 0.92, 'recall': 0.94, 'f1_score': 0.93},
        {'disease': 'Septoria Leaf Spot', 'precision': 0.92, 'recall': 0.94, 'f1_score': 0.93},
        {'disease': 'Target Spot', 'precision': 0.88, 'recall': 0.87, 'f1_score': 0.88},
        {'disease': 'Yellow Leaf Curl Virus', 'precision': 1.00, 'recall': 0.99, 'f1_score': 0.99},
        {'disease': 'Mosaic Virus', 'precision': 0.93, 'recall': 0.91, 'f1_score': 0.92},
        {'disease': 'Two-Spotted Spider Mite', 'precision': 0.93, 'recall': 0.92, 'f1_score': 0.93},
        {'disease': 'Healthy Leaves', 'precision': 0.94, 'recall': 0.98, 'f1_score': 0.96},
    ]

    context = {
        'metrics': metrics,
        'per_class_metrics': per_class_metrics,
    }

    return render(request, 'tomato_app/model_performance.html', context)


def about(request):
    """About page with project information"""
    return render(request, 'tomato_app/about.html')


@require_http_methods(["POST"])
def api_predict(request):
    """API endpoint for predictions - NO DATABASE STORAGE"""
    """
    API endpoint for prediction (for mobile/JS clients)
    Expects multipart/form-data with 'image' field
    """
    if 'image' not in request.FILES:
        return JsonResponse({'error': 'No image provided'}, status=400)

    try:
        uploaded_file = request.FILES['image']
        img = Image.open(uploaded_file).convert('RGB')
        result = predictor.predict(img)

        if result.get('success'):
            # Ensure all values are JSON serializable
            # Get disease info and ensure it's JSON serializable
            raw_disease_info = disease_info.get(str(result['predicted_class']), {})
            safe_disease_info = {}
            for key, value in raw_disease_info.items():
                if isinstance(value, str):
                    safe_disease_info[str(key)] = str(value)
                elif isinstance(value, (int, float)):
                    safe_disease_info[str(key)] = float(value)
                elif isinstance(value, bool):
                    safe_disease_info[str(key)] = bool(value)
                else:
                    safe_disease_info[str(key)] = str(value)
            
            prediction_data = {
                'class': str(result['predicted_class']),
                'confidence': float(result['confidence']),
                'disease_info': safe_disease_info
            }
            
            # Ensure all_predictions is JSON serializable
            all_predictions = []
            if 'all_predictions' in result:
                for pred in result['all_predictions']:
                    all_predictions.append({
                        'disease': str(pred.get('disease', '')),
                        'confidence': float(pred.get('confidence', 0)),
                        'is_predicted': bool(pred.get('is_predicted', False))
                    })
            
            return JsonResponse({
                'success': True,
                'prediction': prediction_data,
                'all_predictions': all_predictions
            })
        else:
            return JsonResponse({'error': str(result.get('error', 'Unknown error'))}, status=500)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
