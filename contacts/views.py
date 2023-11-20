from django.shortcuts import redirect, render
from cars.models import Car

from contacts.utils import send_notification
from .models import Contact
from django.contrib import messages     
from django.core.mail import send_mail 
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your views here.


def inquiry(request):
   
    if request.method == 'POST':

        car_id=request.POST['car_id']
        car=Car.objects.get(pk=car_id)
        car_title=request.POST['car_title']
        user_id=request.POST['user_id']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        customer_need=request.POST['customer_need']
        city=request.POST['city']
        state=request.POST['state']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        price=car.price
        car_photo=car.car_photo
        

        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.info(request,_('inquiry_already'))
                return redirect('/cars/'+car_id)
        admin_info=User.objects.get(is_superuser=True)    
        admin_email=admin_info.email
        

        contact=Contact(car_id=car_id,car_title=car_title,user_id=user_id,first_name=first_name,last_name=last_name,customer_need=customer_need,city=city,state=state,email=email,phone =phone,message=message,price=price,car_photo=car_photo)

        mail_Subject='New Car Inquiry'
        email_template='accounts/emails/car_iquiry_admin_email.html'
        message = "You have a new inquiry for thec car ",car_title,". Please login to ur admin panel for more info."
        context={
            'user':admin_info,
            'message':message,
            'car':car,
        }
        send_notification(mail_Subject,email_template,context)

        """send_mail(
                    "New Car Inquiry",
                    "You have a new inquiry for thec car ",car_title,". Please login to ur admin panel for more info.",
                    "otmane.kastali@gmail.com",
                    [admin_email],
                    fail_silently=False,
                )"""

        contact.save()
        messages.success(request,_('inqiry_success'))
        return redirect('/cars/'+car_id)