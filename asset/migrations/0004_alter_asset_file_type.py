# Generated by Django 4.2.2 on 2023-07-01 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_alter_asset_file_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='file_type',
            field=models.IntegerField(choices=[(1, 'image'), (2, 'font'), (3, 'dynamic')], default=1),
        ),
    ]
