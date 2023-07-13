from django.shortcuts import render
from .models import Email 

def email(request):
     return render(request, 'app/email.html', {
          "email": Email
     })

def hello(request):
     return render(request, 'app/hello.html', {})