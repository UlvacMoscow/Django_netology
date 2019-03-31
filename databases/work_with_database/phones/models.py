from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.SlugField(max_length=150)
    price = models.FloatField('цена')
    image = models.ImageField(verbose_name='Изображение', )
    release_date = models.DateField(verbose_name='Релиз')
    lte_exists = models.BooleanField('LTE')

    def phones():
        return Phone.objects.all()
