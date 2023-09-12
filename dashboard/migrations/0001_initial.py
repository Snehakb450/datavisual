# Generated by Django 4.2.4 on 2023-08-26 08:31

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Data",
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
                ("end_year", models.CharField(db_column="end_year", max_length=40)),
                ("intensity", models.CharField(db_column="intensity", max_length=40)),
                ("sector", models.CharField(db_column="sector", max_length=40)),
                ("topic", models.CharField(db_column="topic", max_length=40)),
                ("insight", models.CharField(db_column="insight", max_length=40)),
                ("url", models.CharField(db_column="url", max_length=40)),
                ("region", models.CharField(db_column="region", max_length=40)),
                ("start_year", models.CharField(db_column="start_year", max_length=40)),
                ("impact", models.CharField(db_column="impact", max_length=40)),
                ("added", models.CharField(db_column="added", max_length=40)),
                ("published", models.CharField(db_column="published", max_length=40)),
                ("country", models.CharField(db_column="country", max_length=40)),
                ("relevance", models.CharField(db_column="relevance", max_length=40)),
                ("pestle", models.CharField(db_column="pestle", max_length=40)),
                ("source", models.CharField(db_column="source", max_length=40)),
                ("title", models.CharField(db_column="title", max_length=40)),
                ("likelihood", models.CharField(db_column="likelihood", max_length=40)),
            ],
            options={
                "db_table": "data",
            },
        ),
    ]
