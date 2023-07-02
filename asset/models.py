from django.db import models



class Asset(models.Model):
    
    
    FILE_TYPE_CHOICES = (
        (1, 'image'),
        (2, 'font'),
        (3, 'dynamic')
    )

    asset_id = models.IntegerField(default=1)
    upload_file = models.FileField(upload_to='upload')
    file_type = models.IntegerField(choices=FILE_TYPE_CHOICES, default=1)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)