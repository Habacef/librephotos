# Generated by Django 3.1.14 on 2022-02-20 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0021_remove_photo_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="photo",
            name="video_length",
            field=models.TextField(blank=True, null=True),
        ),
    ]
