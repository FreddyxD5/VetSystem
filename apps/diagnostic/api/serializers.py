from rest_framework import serializers
from apps.diagnostic.models import Diagnostic

class DiagnosticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostic
        exclude = ('active', 'modified_at', 'eliminated_at', )

    def to_representation(self, instance):
        print(instance)
        return {
            "pet_name": instance.pet.name,
            "veterinary" :instance.vet.nombre_completo(),
            "observations":instance.observations,
            "medication":instance.medication,
            "instruction":instance.instruction,
            "created_at":instance.created_at
        }
