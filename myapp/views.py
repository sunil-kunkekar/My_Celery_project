from django.shortcuts import render
from my_celery_project.celery import * 

# Create your views here.
def index(request):
    print("Results: ")
    result1 = add.delay(10,42)
    print("result1:",result1)
    return render(request, "myapp/home.html")