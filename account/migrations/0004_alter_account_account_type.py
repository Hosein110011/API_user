# Generated by Django 4.2.2 on 2023-07-01 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_account_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.IntegerField(choices=[(1, 'premium'), (2, 'basic')], default=2),
        ),
    ]
