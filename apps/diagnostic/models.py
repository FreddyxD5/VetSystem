from django.db import models
from django.core.exceptions import ValidationError
from apps.base.models import BaseModel
from apps.pet.models import Pet
from apps.users.models import Usuario


# Create your models here.


class Diagnostic(BaseModel):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    vet = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    observations = models.TextField()
    medication = models.TextField()
    instruction = models.TextField()
    active = models.TextField()

    def __str__(self):
        return f"Diagnostic{self.pet.name} - {self.pet.owner.nombres}"
    
    def save(self,*args,**kwargs):
        if self.vet.role != 'VET':
            raise ValidationError(_('Debe asignar un veterinario'), code='role_error')
        super(Diagnostic, self).save(*args, **kwargs)



