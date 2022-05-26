from django.db import models
from django.db import models
from django.dispatch import receiver
from django.forms import CharField
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  

class ProductModel(models.Model):
    image = models.ImageField(upload_to=upload_name_path, null=True)
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    description = RichTextField()
    original_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=4, decimal_places=2, default=18)
    
    objects = ProductManager()
        
    class Meta:
        db_table = 'allitson'
    
    def __str__(self):
       return '{} {} {}'.format(self.image, self.title, self.slug,self.active, self.featured, self.description,self.original_price, self.price, self.tax)

class TagModel(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    product = models.ManyToManyField(Product, blank=True, related_name="tag_list")
    

    class Meta:
        db_table = 'organization'

    def __str__(self):
        #return self.title
        return '{} {} {} {} {} {} {} {} {}'.format(self.title, self.slug, self.timestamp, self.active,self.product
        )



        
        
        
