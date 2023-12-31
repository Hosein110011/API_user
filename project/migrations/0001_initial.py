# Generated by Django 4.2.2 on 2023-06-27 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.TextField()),
                ('publisher_id', models.TextField()),
                ('content', models.TextField()),
                ('state', models.PositiveSmallIntegerField(choices=[(1, 'visible'), (2, 'hidden')], default=2)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('edited_time', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
                ('asset_id', models.TextField()),
            ],
        ),
    ]
