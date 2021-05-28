from django.conf.urls import url
from django.http import response
from django.shortcuts import render
import requests
API_KEY = 'ae9445c8f52d4a13b556b4fa11e4a19d'
def home(request):
    """country = request.GET.get('country')"""
    url =  f'https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    print(data)

    articles = data['articles']
    context = {
        'articles': articles
    }
    return render(request,'news_api/home.html',context)