from rest_framework import serializers
from apps.pet.models import Pet, CategoryPet

class CategoryPetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryPet
        exclude = ('created_at','modified_at', 'eliminated_at', 'status', )

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        exclude = ('created_at','modification_at', 'eliminated_at', 'status', )