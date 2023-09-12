from django.urls import path
from . import views
app_name='dashboard'

urlpatterns = [ 
    path ('',views.get_home, name="home"), 
    path('master/',views.master,name="master"),
    path ('intensity/',views.intensity, name="intensity"), 
    path('bar_chart/', views.bar_chart_view, name='bar_chart'),
     path ('likelihood/',views.likelihood, name="likelihood"), 
    path ('relevance/',views.relevance, name="relevance"), 
       path ('end_year/',views.end_year, name="end_year"), 
        path ('country/',views.country, name="country"), 
         path ('topic/',views.topic, name="topic"), 
          path ('region/',views.region, name="region"), 
           path ('sector/',views.sector, name="sector"),  
    
    
    
]

