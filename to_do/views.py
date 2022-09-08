from django.shortcuts import render, HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse("><h1>helolo</h1><p>this is a paragraph</p>")