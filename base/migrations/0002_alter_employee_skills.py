# Generated by Django 5.0.7 on 2024-07-26 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="skills",
            field=models.TextField(blank=True, null=True),
        ),
    ]
