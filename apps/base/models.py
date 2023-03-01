from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateField('Fecha de Creacion', auto_now_add =True, auto_now=False)
    modified_at = models.DateField('Fecha de modificacion', auto_now=True, auto_now_add=False)
    eliminated_at = models.DateField('Fecha de eliminacion', auto_now=True, auto_now_add=False)    

    class Meta:
        abstract = True