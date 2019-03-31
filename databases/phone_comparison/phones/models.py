from django.db import models

# Create your models here.
class Phone(models.Model):
    model_name = models.CharField('model_name', max_length=40)
    brand = models.CharField('brand', max_length=40)
    screen = models.CharField('screen', max_length=5)
    processor = models.CharField('processor', max_length=40)
    camera = models.BooleanField('camera', default=True)
    battery = models.IntegerField('battery', default=100)
    memory = models.IntegerField('memory', default=0)


    def get_all_phones():
        return Phone.objects.all()


class Nokia(Phone):
    scan_eye = models.BooleanField('scan_eye', default=False)
    def __str__(self):
        return self.brand + self.model_name


class Xiaomi(Phone):
    scan_finger = models.BooleanField('scan_finger', default=False)
    def __str__(self):
        return self.brand + self.model_name

class Asus(Phone):
    teleport = models.BooleanField('teleport', default=False)
    def __str__(self):
        return self.brand + self.model_name
