from rest_framework.routers import DefaultRouter
from apps.pet.api.api import CategoryPetViewSet

router = DefaultRouter()

router.register('category_pet', CategoryPetViewSet, basename = 'category_pet')

urlpatterns = router.urls

