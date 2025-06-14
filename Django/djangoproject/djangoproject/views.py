from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("welcome to django world...!")
    return render(request,'website/index.html')