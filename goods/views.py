from django.shortcuts import HttpResponse
import datetime


def hello_view(request):
    if request.method == "GET":
        return HttpResponse("Hello! It's my project))")


def now_date_view(request):
    current_date = datetime.date.today()
    if request.method == "GET":
        return HttpResponse(f"Today is {current_date}")


def goodbye_view(request):
    if request.method == "GET":
        return HttpResponse("Goodbye user!))")
