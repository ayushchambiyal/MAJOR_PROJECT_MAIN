from django.db import models
import datetime
import os
# Create your models here.
class cont_me(models.Model):
    first_name=models.CharField(max_length=122)
    last_name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    gender=models.CharField(max_length=30)
    message=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

class Signup(models.Model):
    first_name=models.CharField(max_length=122)
    last_name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    password1=models.CharField(max_length=30)
    password2=models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)
    
class Item(models.Model):
    name = models.TextField(max_length=191)
    price = models.TextField(max_length=50)
    description = models.TextField(max_length=500, null=True)
    seller_name = models.TextField(max_length=191)
    image = models.ImageField(upload_to=filepath, null=True, blank=True)
    dtime =models.DateTimeField(null=True)
    current_bidder_name = models.TextField(max_length=191)
#IT WILL DISPLAY AYUSH AS FIRST ENTRY 
#BASICALLY DISPALY PRIPSOSE
    def __str__(self):
        return self.name



