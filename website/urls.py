from django.urls import path
from . views import home, about, projects, titanic, result, python, ml, ds, acronyms, webbot, terms, privacy
from . import views



app_name='ytproject'

urlpatterns = [
    path('', views.home),
    path('about.html', views.about, name="about"),
    path('projects.html', views.projects, name="projects"),
    path('contact.html', views.contact, name="contact"),
    path('titanic.html', views.titanic, name="titanic"),
    path('result/', views.result, name="result"),
    path('python.html', views.python, name="python"),
    path('ml.html', views.ml, name="ml"),
    path('ds.html', views.ds, name="ds"),
    path('acronyms.html/', views.acronyms, name="acronyms"),
    path('webbot.html', views.webbot, name="webbot"),
    path('bot_search/', views.bot_search, name="bot_search"),
    path('terms.html', views.terms, name="terms"),
    path('privacy.html', views.privacy, name="privacy"),
    path('all_download_video/', views.all_download_video, name='all_download_video'),
  
  
   
    
]