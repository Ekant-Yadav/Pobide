# from django.http.request import HttpRequest
# from django.http.response import HttpResponse
from django.shortcuts import render
from home import mlmodel
# from bs4 import BeautifulSoup

def index(request):
    return render(request, 'home.html')

def verify(request):
    if request.method=='POST':
        news = request.POST.get('input')
        # print(news)
        validity = mlmodel.verification(str(news))
        # bias = mlmodel.biases(news)
        wiki = mlmodel.wiki(str(news))
        # wiki ="www.google.com"
        op= 1 if wiki[0]=="1" else None
        # print(op)
        wiki=wiki[1:]
        # soup = BeautifulSoup(wiki,"html5lib")
        # print(wiki)
        # return HttpResponse(wiki)
        context={
            'news':news,
            'validity': "False" if validity[0]==1 else "True",
            # 'bias':bias
            'wiki': wiki,
            'op':op,
        }
    return render(request, 'index.html', context)