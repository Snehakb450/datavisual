# Generated by Django 4.2.4 on 2023-09-11 10:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0007_alter_data_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="data",
            name="insight",
            field=models.CharField(db_column="insight", max_length=500),
        ),
        migrations.AlterField(
            model_name="data",
            name="url",
            field=models.CharField(db_column="url", max_length=500),
        ),
    ]
