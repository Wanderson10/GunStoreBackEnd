# Generated by Django 4.1.5 on 2023-05-30 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("weapons", "0007_alter_weapon_tipe"),
    ]

    operations = [
        migrations.AlterField(
            model_name="weapon",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
