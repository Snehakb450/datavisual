# Generated by Django 4.2.4 on 2023-09-11 10:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0006_alter_data_insight_alter_data_title_alter_data_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="data",
            name="title",
            field=models.CharField(db_column="title", max_length=500),
        ),
    ]
