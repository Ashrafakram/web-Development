# Generated by Django 5.1.1 on 2024-09-09 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bloging", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="img_url",
            field=models.URLField(null=True),
        ),
    ]
