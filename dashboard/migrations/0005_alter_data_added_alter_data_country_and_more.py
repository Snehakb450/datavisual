# Generated by Django 4.2.4 on 2023-09-11 10:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0004_uploadedfile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="data",
            name="added",
            field=models.CharField(db_column="added", max_length=100),
        ),
        migrations.AlterField(
            model_name="data",
            name="country",
            field=models.CharField(db_column="country", max_length=100),
        ),
        migrations.AlterField(
            model_name="data",
            name="end_year",
            field=models.CharField(db_column="end_year", max_length=100),
        ),
        migrations.AlterField(
            model_name="data",
            name="impact",
            field=models.CharField(db_column="impact", max_length=100),
        ),
        migrations.AlterField(
            model_name="data",
            name="insight",
            field=models.CharField(db_column="insight", max_length=100),
        ),
        migrations.AlterField(
            model_name="data",
            name="intensity",
            field=models.CharField(db_column="intensity", max_length=100),
        ),
        migrations.AlterField(
            model_name="data",
            name="likelihood",
            field=models.CharField(db_column="likelihood", max_length=100),
        ),
        migrations.AlterField(
            model_name="data",
            name="pestle",
            field=models.CharField(db_column="pestle", max_length=100),
        ),
        migrations.AlterField(
            model_name="data",
            name="published",
            field=models.CharField(db_column="published", max_length=100),
        ),
        migrations.AlterField(
            model_name="data",
            name="region",
            field=models.CharField(db_column="region", max_length=100),
        ),
        migrations.AlterField(
            model_name="data",
            name="relevance",
            field=models.CharField(db_column="relevance", max_length=100),
        ),
        migrations.AlterField(
            model_name="data",
            name="sector",
            field=models.CharField(db_column="sector", max_length=100),
        ),
        migrations.AlterField(
            model_name="data",
            name="source",
            field=models.CharField(db_column="source", max_length=100),
        ),
        migrations.AlterField(
            model_name="data",
            name="start_year",
            field=models.CharField(db_column="start_year", max_length=100),
        ),
        migrations.AlterField(
            model_name="data",
            name="title",
            field=models.CharField(db_column="title", max_length=100),
        ),
        migrations.AlterField(
            model_name="data",
            name="topic",
            field=models.CharField(db_column="topic", max_length=100),
        ),
        migrations.AlterField(
            model_name="data",
            name="url",
            field=models.CharField(db_column="url", max_length=100),
        ),
    ]