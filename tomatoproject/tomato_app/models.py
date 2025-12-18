from django.db import models
import os


def prediction_image_path(instance, filename):
    """Generate upload path for prediction images"""
    # Create path: predictions/YYYY/MM/DD/filename
    from datetime import datetime
    now = datetime.now()
    return os.path.join('predictions', now.strftime('%Y/%m/%d'), filename)


class Prediction(models.Model):
    """Store prediction results for analytics"""
    image = models.ImageField(upload_to=prediction_image_path, null=True, blank=True)
    image_name = models.CharField(max_length=255)
    prediction = models.CharField(max_length=100)
    confidence = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.image_name} - {self.prediction}"

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Prediction'
        verbose_name_plural = 'Predictions'
