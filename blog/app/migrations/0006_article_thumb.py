# Generated by Django 4.2.1 on 2023-06-01 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_student_body"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="thumb",
            field=models.ImageField(blank=True, default="default.png", upload_to=""),
        ),
    ]
