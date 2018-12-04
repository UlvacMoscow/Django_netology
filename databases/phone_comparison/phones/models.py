from django.db import models

# Create your models here.
class Phone(models.Model):
    brand = models.CharField('brand', max_length=40)
    model_name = models.CharField('model_name', max_length=50)
    screen = models.CharField('screen', max_lenght=5)
    camera = models.BooleanField('camera', default=True)
    battery
    memory
