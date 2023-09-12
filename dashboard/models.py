from django.db import models

# Create your models here.
class Data(models.Model):
    end_year=models.CharField(max_length=100,db_column="end_year")
    intensity=models.CharField(max_length=100,db_column="intensity")
    sector=models.CharField(max_length=100,db_column="sector")
    topic=models.CharField(max_length=100,db_column="topic")
    insight=models.CharField(max_length=500,db_column="insight")
    url=models.CharField(max_length=500,db_column="url")
    region=models.CharField(max_length=100,db_column="region")
    start_year=models.CharField(max_length=100,db_column="start_year")
    impact=models.CharField(max_length=100,db_column="impact")
    added=models.CharField(max_length=100,db_column="added")
    published=models.CharField(max_length=100,db_column="published")
    country=models.CharField(max_length=100,db_column="country")
    relevance=models.CharField(max_length=100,db_column="relevance")
    pestle=models.CharField(max_length=100,db_column="pestle")
    source=models.CharField(max_length=200,db_column="source")
    title=models.CharField(max_length=500,db_column="title")
    likelihood=models.CharField(max_length=100,db_column="likelihood")
    
    class Meta:
        db_table="data"
        verbose_name_plural='data'
        
        
from django.db import models
from  django.db.models import JSONField

class JsonData(models.Model):
    data = models.JSONField()

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)