# Generated by Django 4.1.5 on 2023-05-05 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_employee",
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
