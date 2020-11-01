from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Profile,Business,Authority,Hospital
from .forms import ProfileUpdateForm
# Create your views here.
def home(request):
   
    return render(request,'watch/home.html')

def contacts(request):
    neighborhood=request.user.profile.neighborhood
    authorities=Authority.objects.filter(neighborhood=neighborhood).all
    hospitals=Hospital.objects.filter(neighborhood=neighborhood).all
    businesses=Business.objects.filter(neighborhood=neighborhood).all
    return render(request,'watch/profile/contactlist.html',{'businesses':businesses,'authorities':authorities,'hospitals':hospitals})

def sign_up(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email= request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
        user.save()
        profile=Profile.objects.create(user=user,first_name=user.first_name,last_name=user.last_name,email=user.email)
        return redirect('login')
    else:
        return render(request,'registration/register.html')

def profile(request):
    profile=request.user.profile

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
    else:
        form=ProfileUpdateForm
    return render(request,'watch/profile/profile.html', {'form':form})

