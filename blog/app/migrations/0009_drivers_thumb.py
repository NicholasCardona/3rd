# Generated by Django 4.2.1 on 2023-06-01 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0008_alter_drivers_team"),
    ]

    operations = [
        migrations.AddField(
            model_name="drivers",
            name="thumb",
            field=models.ImageField(
                blank=True, default="driver_default.png", upload_to=""
            ),
        ),
    ]
