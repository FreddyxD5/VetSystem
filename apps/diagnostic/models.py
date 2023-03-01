from django.db import models
from apps.base.models import BaseModel
from apps.pet.models import Pet


# Create your models here.


class Diagnostic(BaseModel):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    # doctor = models.ForeignKey(Employee, on_delete=models.CASCADE)    
    observations = models.TextField()
    medication = models.TextField()
    instruction = models.TextField()
    active = models.TextField()

    def __str__(self):
        return f"Diagnostic{self.pet.name} - {self.pet.owner.nombres}"
    

#class DiagnosticDetail(BaseModel):
#    diagnostic = models.ForeignKey(Diagnostic, on_delete=models.CASCADE)
    

