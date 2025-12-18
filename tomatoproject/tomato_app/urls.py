from django.urls import path
from . import views
from .debug_views import debug_upload, simple_upload, client_side_upload

urlpatterns = [
    path('', views.index, name='index'),
    path('batch-predict/', views.batch_predict, name='batch_predict'),
    path('disease-info/', views.disease_info_view, name='disease_info'),
    path('crop-report/', views.crop_report, name='crop_report'),
    path('model-performance/', views.model_performance, name='model_performance'),
    path('about/', views.about, name='about'),

    # API endpoints
    path('api/predict/', views.api_predict, name='api_predict'),
    
    # Upload endpoints - Simple upload is now the primary interface
    path('upload/', simple_upload, name='upload_image'),  # Redirect to simple upload
    path('simple-upload/', simple_upload, name='simple_upload'),
    path('debug-upload/', debug_upload, name='debug_upload'),
    path('client-side-upload/', client_side_upload, name='client_side_upload'),
]
