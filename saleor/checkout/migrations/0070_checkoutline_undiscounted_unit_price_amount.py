# Generated by Django 4.2.15 on 2024-10-23 11:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("checkout", "0069_merge_20240514_1008"),
    ]

    operations = [
        migrations.AddField(
            model_name="checkoutline",
            name="undiscounted_unit_price_amount",
            field=models.DecimalField(
                blank=True, decimal_places=3, max_digits=12, null=True
            ),
        ),
    ]
