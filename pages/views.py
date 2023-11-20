from django.shortcuts import redirect, render
from contacts.utils import  send_notification

from cars.models import Car
from django.contrib.auth.models import User
from django.contrib import messages

from pages.models import Team

from django.utils.translation import gettext as _
# Create your views here.


def home(request):
    teams=Team.objects.all()
    featured_cars=Car.objects.order_by("-created_at").filter(is_featured=True)
    all_cars=Car.objects.order_by("-created_at")
    #search_fields=Car.objects.values('model','city','year','body_style')
    model_search=Car.objects.values_list('model',flat=True).distinct()
    city_search=Car.objects.values_list('city',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style',flat=True).distinct()



    context= {
        'teams':teams,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
        #'search_fields' : search_fields,
        'model_search' : model_search,
        'city_search' : city_search,
        'year_search' : year_search,
        "body_style_search"  :   body_style_search,
    }

    return render(request,'pages/home.html',context)


def about(request):
    teams=Team.objects.all()
    context={
        'teams':teams,
    }
    return render(request,'pages/about.html',context)


def services(request):
    return render(request,'pages/services.html')



def contact(request):
    if request.method== 'POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        phone=request.POST['phone']
        message=request.POST['message']

        admin_info=User.objects.get(is_superuser=True)    
        admin_email=admin_info.email
        email_template='accounts/emails/contact_email.html'
        email_subject="You have a new message from CarHouse website regarding "+subject
        messgae_body="Name: "+name+". Email: "+email+". Phone: "+phone+". Message: "+message

        context= {
            'message':messgae_body,
            'user':admin_info,
            'name':name,
            'email':email,
            'phone':phone,
            'message':message,
        }
        send_notification(email_subject,email_template,context)

        messages.success(request,_('contact_message'))
        return redirect('contact')
       

        


    return render(request,'pages/contact.html')