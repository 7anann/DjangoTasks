from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hellodemo(request):
    print(request)
    return render(request,'homePage.html')

def hellodemoparam(request, name):
    print(name)
    return HttpResponse(f'<h1>Welcome {name}</h1>')