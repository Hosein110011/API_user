from django.db import models


IMPORTANCE_TYPE_CHOICES =(
        (1, 'update'),
        (2, 'not important')
    )

class Version(models.Model):
    version = models.CharField(max_length=255)
    google_store_url = models.CharField(max_length=255)
    bazar_url = models.CharField(max_length=255)
    miket_url = models.CharField(max_length=255)
    importance = models.IntegerField(choices=IMPORTANCE_TYPE_CHOICES, default=1)
    
