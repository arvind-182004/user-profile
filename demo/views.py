from django.shortcuts import render
from .models import Profile


def home(request):
    users = Profile.objects.all()
    return render(request,'index.html',{'users':users})