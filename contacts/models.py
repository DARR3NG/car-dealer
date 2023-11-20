from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    car_id=models.IntegerField()
    customer_need=models.CharField(max_length=100)
    car_title=models.CharField(max_length=100)
    car_photo=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    price=models.IntegerField(default=0)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    message=models.TextField(blank=True)
    user_id=models.IntegerField(blank=True)
    created_at=models.DateTimeField(blank=True,auto_now_add=True)


    def __str__(self) -> str:
        return self.email