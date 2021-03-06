from django.db import models
    

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    phone = models.CharField(max_length=13)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    file = models.FileField()



    def __str__(self):
        return self.name
