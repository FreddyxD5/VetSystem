from rest_framework import serializers
from apps.pet.models import Pet, CategoryPet
from apps.diagnostic.models import Diagnostic
from apps.diagnostic.api.serializers import DiagnosticSerializer


class CategoryPetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryPet
        exclude = ('created_at','modified_at', 'eliminated_at', 'status', )

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        exclude = ('created_at','modified_at', 'eliminated_at', 'status', )


class PetDiagnosticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        exclude = ('created_at','modified_at', 'eliminated_at', 'status', )

    def to_representation(self, instance):
        diagnostics = Diagnostic.objects.filter(pet = instance.id, status=True)
        diagnostics_data = DiagnosticSerializer(diagnostics, many=True)
        return {            
            "name":instance.name,
            "age":instance.age,
            "gender":instance.gender,
            "breed":instance.breed,
            "chip_number":instance.chip_number,            
            "category":instance.category.nombre,
            "diagnostics": diagnostics_data.data if diagnostics is not None else []
        }
        