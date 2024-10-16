# Generated by Django 5.1.2 on 2024-10-16 11:35

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Reservation",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=15)),
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("guests", models.IntegerField()),
                ("special_requests", models.TextField(blank=True, null=True)),
            ],
        ),
    ]