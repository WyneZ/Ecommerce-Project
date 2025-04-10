from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, default='customer')
    password = models.CharField(max_length=100)
    address = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.email
    






