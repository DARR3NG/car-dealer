from django.shortcuts import redirect, render
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from contacts.models import Contact
from django.utils.translation import gettext_lazy as _

# Create your views here.

def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,_('auth_message_success'))
            return redirect('dashboard')
        else:
            messages.error(request,_('auth_message_invalid_cred'))
            return redirect('login')
            
        

    return render(request,'accounts/login.html')


def register(request):
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname = request.POST["lastname"]
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_passwrod=request.POST['confirm_password']

        if password == confirm_passwrod:
            if User.objects.filter(username=username).exists():
                messages.error(request,_('register_username_exist'))
                return redirect('register')
            else:
                 if User.objects.filter(email=email).exists():
                    messages.error(request,_('register_email_exist'))
                    return redirect('register')
                 else:
                     user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
                     auth.login(request,user)
                     messages.success(request,_('auth_message_success'))
                     return redirect('dashboard')
                     user.save()
                     messages.success(request,"Account created successfully!")
                     return redirect('login')


        else:
            messages.error(request,_('register_password_not_match'))
            return redirect('register')

    return render(request,'accounts/register.html')


@login_required(login_url='login')
def dashboard(request):
    user_inquiry = Contact.objects.order_by('-created_at').filter(user_id=request.user.id)
    
    context={
        'inquiries':user_inquiry,
    }
    return render(request,'accounts/dashboard.html',context)


def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,_('logout_success'))
        return redirect("home")

    return redirect("home")
