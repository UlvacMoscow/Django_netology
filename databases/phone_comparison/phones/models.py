from django.db import models

# Create your models here.
class Phone(models.Model):
    model_name = models.CharField('model_name', max_length=40)
    screen = models.CharField('screen', max_length=5)
    camera = models.BooleanField('camera', default=True)
    battery = models.IntegerField('battery', default=100)
    memory = models.IntegerField('memory', default=0)

    def __str__(self):
        return self.model_name


class Nokia(models.Model):
    parametrs = models.ForeignKey(Phone, on_delete=models.CASCADE)
    name = models.CharField('name', max_length=50, default='Nokia')
    scan_eye = models.BooleanField('scan_eye', default=False)

    def __str__(self):
        return self.name


class Xiomi(models.Model):
    parametrs = models.ForeignKey(Phone, on_delete=models.CASCADE)
    name = models.CharField('name', max_length=50, default='Xiomi')
    scan_finger = models.BooleanField('scan_finger', default=False)

    def __str__(self):
        return self.name
