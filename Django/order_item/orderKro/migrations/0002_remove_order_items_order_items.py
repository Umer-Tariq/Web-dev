# Generated by Django 5.1.1 on 2024-10-29 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orderKro", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="items",
        ),
        migrations.AddField(
            model_name="order",
            name="items",
            field=models.ManyToManyField(related_name="orders", to="orderKro.item"),
        ),
    ]
