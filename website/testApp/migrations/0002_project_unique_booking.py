# Generated by Django 5.1.1 on 2024-09-15 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testApp", "0001_initial"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="project",
            constraint=models.UniqueConstraint(
                fields=("name", "number"), name="unique_booking"
            ),
        ),
    ]
