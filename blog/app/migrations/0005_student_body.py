# Generated by Django 4.2.1 on 2023-05-29 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_student_finances"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="body",
            field=models.TextField(default="hello"),
            preserve_default=False,
        ),
    ]
