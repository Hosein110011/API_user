from django.db import models


class Project(models.Model):
    
    
    STATE_TYPE_CHOICES = (
        (1, 'visible'),
        (2, 'hidden')
    )
    
    
    project_id = models.TextField()
    preview = models.ImageField(upload_to='project', null=True)
    publisher_id = models.TextField()
    content = models.TextField()
    state = models.IntegerField(choices=STATE_TYPE_CHOICES, default=2)
    created_time = models.DateTimeField(auto_now_add=True)
    edited_time = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    asset_id = models.TextField()

    