# from django.http.request import HttpRequest
# from django.http.response import HttpResponse
from django.shortcuts import render
from home import verfication_check, biases_check
# from bs4 import BeautifulSoup

def index(request):
    return render(request, 'home.html')

def verify(request):
    if request.method=='POST':
        news = request.POST.get('input').rstrip()
        # print(news)
        validity = verfication_check.verification(str(news))
        wiki = verfication_check.wiki(str(news))
        op= 1 if wiki[0]=="1" else None
        wiki=wiki[1:]

        bias = biases_check.biases(news)
        
        context={
            'news':news.rstrip(),
            'validity': "False" if validity[0]==1 else "True",
            'bias': bias,
            'wiki': wiki,
            'op':op,
        }
    return render(request, 'index.html', context)