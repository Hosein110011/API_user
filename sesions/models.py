from django.db import models


class Session(models.Model):
    session = models.TextField()
    expire_date = models.DateTimeField()
    create_date = models.DateTimeField(auto_now_add=True)
    