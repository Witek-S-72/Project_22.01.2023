# Generated by Django 4.1.7 on 2023-02-23 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("examples", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="personaldata",
            name="gender",
            field=models.CharField(default="Mr.", max_length=10),
        ),
    ]
