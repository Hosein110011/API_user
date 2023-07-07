from django.db import models
from django.core import validators 


COMPETITION_TYPE_CHOICES = (
    (1, 'premium'),
    (2, 'basic')
)


class Account(models.Model):
    
    ACCOUNT_TYPE_CHOICES = (
        (1, 'premium'),
        (2, 'basic')
    )
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.BigIntegerField(unique = True, null=True, blank=False, validators=[validators.RegexValidator(r'^989[0-3,9]\d{8}$')])
    phone_number2 = models.BigIntegerField(unique=True, blank=True, null=True, validators=[validators.RegexValidator(r'^989[0-3,9]\d{8}$')])
    image = models.ImageField(upload_to='avatars', null=True)
    email = models.EmailField(null=True, blank=True, unique=False)
    otp = models.IntegerField(default=1)
    user_id = models.IntegerField(default=1)
    telephone = models.BigIntegerField(blank=True, null=True)
    account_type = models.IntegerField(choices=ACCOUNT_TYPE_CHOICES, default=2)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Account'




