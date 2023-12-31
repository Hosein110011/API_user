# Generated by Django 4.2.2 on 2023-06-25 04:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone_number', models.BigIntegerField(null=True, unique=True, validators=[django.core.validators.RegexValidator('^989[0-3,9]\\d{8}$')])),
                ('phone_number2', models.BigIntegerField(blank=True, null=True, unique=True, validators=[django.core.validators.RegexValidator('^989[0-3,9]\\d{8}$')])),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('otp', models.IntegerField(default=1)),
                ('user_id', models.IntegerField(default=1)),
                ('telephone', models.BigIntegerField(blank=True, null=True)),
                ('account_type', models.PositiveSmallIntegerField(choices=[(1, 'premium'), (2, 'basic')], default=2)),
            ],
        ),
    ]
