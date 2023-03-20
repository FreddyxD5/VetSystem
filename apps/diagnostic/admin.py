from django.contrib import admin
from apps.diagnostic.models import Diagnostic

# Register your models here.

class DiagnosticAdmin(admin.ModelAdmin):
    list_display = ('pet', 'veterinary', 'observations', 'medication', )

    @admin.display(empty_value='???')
    def veterinary(self, obj):
        return obj.vet.nombre_completo()

admin.site.register(Diagnostic, DiagnosticAdmin)