# Generated by Django 5.1.1 on 2024-09-10 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bloging", "0006_post_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutUs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
            ],
        ),
    ]
