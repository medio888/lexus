from django.http.response import HttpResponse
from django.shortcuts import redirect 
from django.http import HttpResponse


def api_redirect(request):
    return redirect('/api/')


def home(request):
    return HttpResponse("Добро пожаловать на главную страницу Lexus!")  