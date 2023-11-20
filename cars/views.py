from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage,Paginator,PageNotAnInteger

from cars.models import Car

# Create your views here.


def cars(request):
    cars=Car.objects.order_by("-created_at")
    paginator=Paginator(cars,4)
    page=request.GET.get('page')
    paged_cars=paginator.get_page(page)
    model_search=Car.objects.values_list('model',flat=True).distinct()
    city_search=Car.objects.values_list('city',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style',flat=True).distinct()
    context={
        "cars":paged_cars,
        'model_search' : model_search,
        'city_search' : city_search,
        'year_search' : year_search,
        "body_style_search"  :   body_style_search,
        
    }
    return render(request,'cars/cars.html',context)


def car_detail(request,id):

    singl_car=get_object_or_404(Car,pk=id)
    
    context={
        'singl_car':singl_car,

    }


    return render(request,'cars/car_detail.html',context)



def search(request):
    cars=Car.objects.order_by("-created_at")
    

    model_search=Car.objects.values_list('model',flat=True).distinct()
    city_search=Car.objects.values_list('city',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style',flat=True).distinct()
    transmission_search=Car.objects.values_list('translations__transmission',flat=True).distinct()


    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        print("first if")
        if keyword:
            cars=cars.filter(translations__description__icontains = keyword).distinct()
            print("description ",cars)
            

    
    if 'model' in request.GET:
        model=request.GET['model']
        print("first if")
        if model:
            cars=cars.filter(model__icontains = model)
            print("second if")
    
    if 'city' in request.GET:
        city=request.GET['city']
        
        if city:
            cars=cars.filter(city__icontains = city)
            print("second if")

    if 'year' in request.GET:
        year=request.GET['year']
        print("first if")
        if year:
            cars=cars.filter(year__iexact = year)
            print("second if")

    if 'body_style' in request.GET:
        body_style=request.GET['body_style']
        print("first if")
        if body_style:
            cars=cars.filter(body_style__iexact = body_style)
            print("second if")
        
    if 'min_price' in request.GET:
        min_price=request.GET['min_price']
        max_price=request.GET['max_price']
        if max_price:
            cars=cars.filter(price__gte=min_price, price__lte=max_price)
    
    
    if 'transmission' in request.GET:
        transmission=request.GET['transmission']
        print("first if")
        if transmission:
            cars=cars.filter(translations__transmission__iexact = transmission)
            print("second if",cars)
           
    print('hna',cars,model_search,city_search,year_search,body_style_search,transmission_search)
    context={
        'cars' : cars,
        'model_search' : model_search,
        'city_search' : city_search,
        'year_search' : year_search,
        'body_style_search'  :   body_style_search,
        'transmission_search' : transmission_search,
        
    }

    print("context",context)
    return render(request,"cars/search.html",context)

