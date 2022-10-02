from django.db import models

# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    phone =  models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    message = models.TextField()


    def __str__(self):
        return self.name

class indexContent(models.Model):
    slidesThemeName = models.CharField(max_length=300, default='Regular')
    greetings1 = models.CharField(max_length=1000)
    slogan1 = models.CharField(max_length=1500, default="")
    greetings2 = models.CharField(max_length=1000)
    slogan2 = models.CharField(max_length=1500, default="")
    greetings3 = models.CharField(max_length=1000)
    slogan3 = models.CharField(max_length=1500, default="")

    def __str__(self):
        return self.slidesThemeName