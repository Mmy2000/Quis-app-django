from django.shortcuts import render
from django.shortcuts import render , redirect , get_object_or_404
from .forms import SignupForm , UserForm , ProfileForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.urls import reverse
from django.db.models import Count
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
# Create your views here.

def signup(request):
    if request.method == "POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            
            usernames = form.cleaned_data['username']
            passwords = form.cleaned_data["password1"]
            user = authenticate(username=usernames,password=passwords)
            login(request,user)

            return render(request,'profile/profile.html')
            
    else:
        form=SignupForm()

    return render(request,'registration/signup.html',{'form':form})

@login_required(login_url='login')
def profile(request):
    profile=Profile.objects.get(user=request.user)

    return render(request,'profile/profile.html',{'profile':profile})