from django.shortcuts import render
from my_celery_project.celery import * 

# Create your views here.
def index(request):
    print("Results: ")
    result1 = add.delay(10,42)
    print("result1:",result1)
    return render(request, "myapp/home.html")

# # Display addition value after task execution
# def index(request):
#     result = add.delay(10, 30)
#     return render(request, "myapp/home.html", {'result':result})

# def check_result(request, task_id):
#     # Retrieve the task result using the task_id
#     result = AsyncResult(task_id)
#     # print("Ready: ", result.ready())
#     # print("Successful: ", result.successful())
#     # print("Failed: ", result.failed())
#     # print("Get: ", result.get())
#     return render(request, 'myapp/result.html', {'result':result})

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')