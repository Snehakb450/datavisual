from django.shortcuts import render
from .models import Data
from django.http import HttpResponse
from django.http import JsonResponse
import plotly.express as px
import pandas as pd



# Create your views here.
def intensity(request):
    
    comparison_variables = ["likelihood", "relevance", "end_year", "country", "topic", "region", "sector"]

    
    plot_divs = []

    
    data_intensity = Data.objects.values('intensity')

    data_df = pd.DataFrame(data_intensity.values())

    for variable in comparison_variables:
       
        fig = px.bar(data_df, x=variable, y="intensity")

       
        plot_div = fig.to_html(full_html=False)

       
        plot_divs.append(plot_div)

    return render(request, 'dashboard/intensity.html', {'plot_divs': plot_divs})


def relevance(request):
    
    comparison_variables = ["likelihood", "intensity", "end_year", "country", "topic", "region", "sector"]

    
    plot_divs = []

    
    data_relevance = Data.objects.values('relevance')

    data_df = pd.DataFrame(data_relevance.values())

    for variable in comparison_variables:
       
        fig = px.bar(data_df, x=variable, y="relevance")

       
        plot_div = fig.to_html(full_html=False)

       
        plot_divs.append(plot_div)

    return render(request, 'dashboard/relevance.html', {'plot_divs': plot_divs})
    

def likelihood(request):
    
    comparison_variables = ["relevance", "intensity", "end_year", "country", "topic", "region", "sector"]

    
    plot_divs = []

    
    data_likelihood= Data.objects.values('likelihood')

    data_df = pd.DataFrame(data_likelihood.values()) 

    for variable in comparison_variables:
       
        fig = px.bar(data_df, x=variable, y="likelihood")

       
        plot_div = fig.to_html(full_html=False)

       
        plot_divs.append(plot_div)

    return render(request, 'dashboard/likelihood.html', {'plot_divs': plot_divs})
   


def end_year(request):
    
    comparison_variables = ["likelihood", "intensity", "relevance", "country", "topic", "region", "sector"]

    
    plot_divs = []

    
    data_end_year = Data.objects.values('end_year')

    data_df = pd.DataFrame(data_end_year.values())

    for variable in comparison_variables:
       
        fig = px.bar(data_df, x=variable, y="end_year")

       
        plot_div = fig.to_html(full_html=False)

       
        plot_divs.append(plot_div)

    return render(request, 'dashboard/end_year.html', {'plot_divs': plot_divs})
    

def country(request):
    
    comparison_variables = ["likelihood", "intensity", "end_year", "relevance", "topic", "region", "sector"]

    
    plot_divs = []

    
    data_country = Data.objects.values('country')

    data_df = pd.DataFrame(data_country.values())

    for variable in comparison_variables:
       
        fig = px.bar(data_df, x=variable, y="country")

       
        plot_div = fig.to_html(full_html=False)

       
        plot_divs.append(plot_div)

    return render(request, 'dashboard/country.html', {'plot_divs': plot_divs})
    


def topic(request):
    
    comparison_variables = ["likelihood", "intensity", "end_year", "country", "relevance", "region", "sector"]

    
    plot_divs = []

    
    data_topic = Data.objects.values('topic')

    data_df = pd.DataFrame(data_topic.values())

    for variable in comparison_variables:
       
        fig = px.bar(data_df, x=variable, y="topic")

       
        plot_div = fig.to_html(full_html=False)

       
        plot_divs.append(plot_div)

    return render(request, 'dashboard/topic.html', {'plot_divs': plot_divs})
    

def region(request):
    
    comparison_variables = ["likelihood", "intensity", "end_year", "country", "topic", "relevance", "sector"]

    
    plot_divs = []

    
    data_region = Data.objects.values('region')

    data_df = pd.DataFrame(data_region.values())

    for variable in comparison_variables:
       
        fig = px.bar(data_df, x=variable, y="region")

       
        plot_div = fig.to_html(full_html=False)

       
        plot_divs.append(plot_div)

    return render(request, 'dashboard/region.html', {'plot_divs': plot_divs})
    


def sector(request):
    
    comparison_variables = ["likelihood", "intensity", "end_year", "country", "topic", "region", "relevance"]

    
    plot_divs = []

    
    data_sector = Data.objects.values('sector')

    data_df = pd.DataFrame(data_sector.values())

    for variable in comparison_variables:
       
        fig = px.bar(data_df, x=variable, y="sector")

       
        plot_div = fig.to_html(full_html=False)

       
        plot_divs.append(plot_div)

    return render(request, 'dashboard/sector.html', {'plot_divs': plot_divs})
 

def master(request):
    unique_end_year_values = Data.objects.values('end_year').distinct() 
    unique_topics_values = Data.objects.values('topic').distinct() 
    unique_sector_values = Data.objects.values_list('sector', flat=True).distinct()
    unique_region_values = Data.objects.values_list('region', flat=True).distinct()
    unique_pest_values = Data.objects.values_list('pestle', flat=True).distinct()
    unique_source_values = Data.objects.values_list('source', flat=True).distinct()
    unique_swot_values = Data.objects.values_list('swot', flat=True).distinct()
    unique_country_values = Data.objects.values_list('country', flat=True).distinct()
    unique_sector_values = Data.objects.values_list('sector', flat=True).distinct()

    context = {
        'unique_end_year_values': unique_end_year_values,
        'unique_topics_values': unique_topics_values,
        'unique_sector_values': unique_sector_values,
        'unique_region_values': unique_region_values,
        'unique_pest_values': unique_pest_values,
        'unique_source_values': unique_source_values,
        'unique_swot_values': unique_swot_values,
        'unique_country_values': unique_country_values,
        'unique_sector_values': unique_sector_values,
    }

    
    return render(request,'dashboard/master.html',context) 

def bar_chart_view(request):
    data = Data.objects.all()

    # Extract data for the chart (e.g., labels and values)
    labels = [entry.title for entry in data]
    values = [entry.intensity for entry in data]

    context = {
        'labels': labels,
        'values': values,
         'data':data,
    }

    return render(request, 'dashboard/bar_chart.html', context)


def get_home(request):
 
    data = Data.objects.all()
    unique_intensity_count = Data.objects.values('intensity').distinct().count()
    unique_likelihood_count = Data.objects.values('likelihood').distinct().count()
    unique_relevance_count = Data.objects.values('relevance').distinct().count()
    unique_end_year_count = Data.objects.values('end_year').distinct().count()
    unique_country_count = Data.objects.values('country').distinct().count()
    unique_topic_count = Data.objects.values('topic').distinct().count()
    unique_region_count = Data.objects.values('region').distinct().count()
    unique_sector_count = Data.objects.values('sector').distinct().count()
       
    data_df = pd.DataFrame(data.values())
   
    dimensions = ["intensity", "likelihood", "relevance","end_year","country","topic","region","sector"]

    fig = px.scatter_matrix(data_frame=data_df, dimensions=dimensions)
    fig.update_layout(
    width=1200,  
    height=2000, 
    margin=dict(l=20, r=20, t=20, b=20), ) 

    plot_div = fig.to_html(full_html=False)

    return render(request, 'dashboard/home.html',
                  {'plot_div': plot_div,'unique_intensity_count': unique_intensity_count,'unique_likelihood_count':unique_likelihood_count,
                   'unique_relevance_count':unique_relevance_count,'unique_end_year_count':unique_end_year_count,
                   'unique_country_count':unique_country_count,'unique_topic_count':unique_topic_count,
                   'unique_region_count':unique_region_count,'unique_sector_count':unique_sector_count}) 

