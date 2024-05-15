from django.shortcuts import render
from django.shortcuts import render , redirect , get_object_or_404
from .forms import SignupForm , UserForm , ProfileForm
from .models import Profile
from quizes.models import Quizes
from result.models import Result
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

def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        user_form = UserForm(request.POST , instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES,instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            myprofile = profile_form.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            messages.success(request,'Done! Your Profile has been updated.')
            return redirect('/accounts/profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    return render(request,'profile/profile_edit.html',{
        'user_form':user_form,
        'profile_form':profile_form,
    })

def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)

            # Reset password email
            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password'
            message = render_to_string('registration/password_reset_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'Password reset email has been sent to your email address.')
            return redirect('login')
        else:
            messages.error(request, 'Account does not exist!')
            return redirect(reverse('accounts:forgotPassword'))
    return render(request, 'registration/password_reset_form.html')

def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect(reverse('accounts:resetPassword'))
    else:
        messages.error(request, 'This link has been expired!')
        return redirect('login')
    
def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = User.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('login')
        else:
            messages.error(request, 'Password do not match!')
            return redirect(reverse('accounts:resetPassword'))
    else:
        return render(request, 'registration/resetPassword.html')
    
def myQuizes(request):
    quiz = Quizes.objects.filter(result__user=request.user)
    result = Result.objects.filter( user=request.user)
    context = {
        'quiz':quiz,
        'result':result
    }
    return render(request , 'profile/myQuizes.html' , context)