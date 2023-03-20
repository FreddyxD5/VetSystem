from django.db import models
from apps.users.models import Usuario, BaseModel

# Create your models here.
class CategoryPet(BaseModel):
    nombre = models.CharField('Pet Name Category',max_length=255)
    descripcion = models.TextField('Descripcion de la categoria')
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Pet(BaseModel):
    name = models.CharField('Nombre de la mascota', max_length=255)
    age = models.CharField('Edad de la mascota', max_length=20)
    gender = models.CharField('Gender', max_length=50)
    breed = models.CharField('Raza', max_length=150)
    chip_number = models.CharField('Numero de Chip', max_length=10, unique=True)
    owner = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryPet, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"