from django.contrib import admin
from . models import Data
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class DataResource(resources.ModelResource):
    class Meta:
        model=Data
        
class DataAdmin(ImportExportModelAdmin):
    resource_class=DataResource
    
admin.site.register(Data,DataAdmin) 