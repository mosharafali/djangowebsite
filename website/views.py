from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import sys
import youtube_dl
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import wolframalpha
import pickle








def home(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message= request.POST['message']

        send_mail(
        name,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
        )        

    return render(request, 'home.html', {})


       

def all_download_video(request):
    url = request.POST.get('url') 
    print("Someone just tried to download","url")
    with youtube_dl.YoutubeDL() as ydl:
        url = ydl.extract_info(url, download=False)
        print(url)
        try:
            download_link = url["entries"][-1]["formats"][-1]["url"]
        except:
            download_link = url["formats"][-1]["url"]
        return redirect(download_link+"&dl=1")

def bot_search(request):
    query = request.GET.get('query')

    try:
        client = wolframalpha.Client("9KPR9V-8WH5AU9TRJ")
        res = client.query(query)
        ans = next(res.results).text
        return render(request, 'bot_search.html', {'ans': ans, 'query': query})

            
    except Exception:
        try:
            ans = wikipedia.summary(query, sentences=10)
            return render(request, 'bot_search.html', {'ans': ans, 'query': query})


        except Exception:
            ans = "FOUND NOTHING"
            return render(request, 'bot_search.html', {'ans': ans, 'query': query})    

def about(request):
    return render(request, 'about.html', {})

def projects(request):
    return render(request, 'projects.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def titanic(request):
    return render(request, 'titanic.html', {})

def getPredictions(pclass, sex, age, sibsp, parch, fare, C, Q, S):
    model = pickle.load(open('ml_model.sav', 'rb'))
    scaled = pickle.load(open('scaler.sav', 'rb'))

    prediction = model.predict(scaled.transform([
        [pclass, sex, age, sibsp, parch, fare, C, Q, S]
    ]))
    
    if prediction == 0:
        return 'no'
    elif prediction == 1:
        return 'yes'
    else:
        return 'error'

def result(request):
    pclass = int(request.GET['pclass'])
    sex = int(request.GET['sex'])
    age = int(request.GET['age'])
    sibsp = int(request.GET['sibsp'])
    parch = int(request.GET['parch'])
    fare = int(request.GET['fare'])
    embC = int(request.GET['embC'])
    embQ = int(request.GET['embQ'])
    embS = int(request.GET['embS'])

    result = getPredictions(pclass, sex, age, sibsp, 
                            parch, fare, embC, embQ, embS)

    return render(request, 'result.html', {'result': result})    

def python(request):
    return render(request, 'python.html', {})    

def ml(request):
    return render(request, 'ml.html', {})    

def ds(request):
    return render(request, 'ds.html', {})  

def terms(request):
    return render(request, 'terms.html', {})   

def privacy(request):
    return render(request, 'privacy.html', {})   

def acronyms(request):
    return render(request, 'acronyms.html', {})      

def webbot(request):
    return render(request, 'webbot.html', {})     

def bot_search(request):
    query = request.GET.get('query')

    try:
        client = wolframalpha.Client("9KPR9V-8WH5AU9TRJ")
        res = client.query(query)
        ans = next(res.results).text
        return render(request, 'bot_search.html', {'ans': ans, 'query': query})

            
    except Exception:
        try:
            ans = wikipedia.summary(query, sentences=10)
            return render(request, 'bot_search.html', {'ans': ans, 'query': query})


        except Exception:
            ans = "FOUND NOTHING"
            return render(request, 'bot_search.html', {'ans': ans, 'query': query})


