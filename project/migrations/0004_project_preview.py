# Generated by Django 4.2.2 on 2023-07-07 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_project_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='preview',
            field=models.ImageField(null=True, upload_to='media/project'),
        ),
    ]
