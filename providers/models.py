from django.db import models
import uuid

# Create your models here.
class Users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile_picture = models.ImageField(upload_to='media/profile_pictures/', default='default.jpg')
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    identity_number = models.CharField(max_length=13, unique=True)
    phone_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    role = models.CharField(max_length=20, choices=[('PROVIDER', 'Provider'), ('SEARCHER', 'Searcher')])

    def __str__(self):
        return f"{self.name} {self.surname} - {self.role}"  

class jobs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    pay = models.DecimalField(max_digits=10, decimal_places=2)
    date_posted = models.DateTimeField(auto_now_add=True)
    searcher = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='jobs')

    def __str__(self):
        return self.title
    
class Services(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    provider = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_posted = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='media/services_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='media/services_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='media/services_images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='media/services_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.provider.name} {self.provider.surname}"