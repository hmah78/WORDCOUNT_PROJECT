from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return render(request,'home.html')

def count(request):
    text= request.GET['textarea']
    word_list = text.split()
    return render(request,'count.html',{'text':text,'count':len(word_list)})

def about(request):
    return render(request,'about.html')