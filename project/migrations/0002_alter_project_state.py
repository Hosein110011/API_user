# Generated by Django 4.2.2 on 2023-06-27 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='state',
            field=models.CharField(choices=[(1, 'visible'), (2, 'hidden')], default=2, max_length=200),
        ),
    ]
