from django.shortcuts import render

# Create your views here.
def home(self):
    return render(request,'watch/home.html')