from django.db import models

# Create your models here.

class Encuesta(models.Model):
    name_user = models.CharField(max_length=20)
    age = models.IntegerField()
    pregunta_1 = models.CharField(max_length=20)
    pregunta_2 = models.CharField(max_length=20)
    pregunta_3 = models.CharField(max_length=20)
    pregunta_4 = models.CharField(max_length=20)
    pregunta_5 = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.name_user)