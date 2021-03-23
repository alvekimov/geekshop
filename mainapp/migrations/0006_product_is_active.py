# Generated by Django 2.2.17 on 2021-02-28 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0005_productcategory_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_active",
            field=models.BooleanField(
                default=True, verbose_name="продукт активен"
            ),
        ),
    ]
