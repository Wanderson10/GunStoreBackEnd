# Generated by Django 4.1.5 on 2023-05-05 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_is_employee"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_employee",
            field=models.BooleanField(default=False),
        ),
    ]
