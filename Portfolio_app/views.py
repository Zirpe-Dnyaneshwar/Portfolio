from django.shortcuts import render
from .models import contact_data

# Create your views here.
def home(request):
    return render(request,'home.html')
def home(request):
    if request.method=='GET':
        return render(request,'home.html')
    else:
        contact_data(
            name=request.POST.get('Name'),
            email=request.POST.get('Email'),
            subject=request.POST.get('Subject'),
            msg=request.POST.get('Message')
        ).save()
        return render(request,'home.html')