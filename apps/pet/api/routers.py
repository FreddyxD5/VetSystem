from rest_framework.routers import DefaultRouter
from apps.pet.api.api import CategoryPetViewSet, PetViewSet

router = DefaultRouter()

#Category
router.register('category_pet', CategoryPetViewSet, basename = 'category_pet')

#Pet
router.register('pet', PetViewSet, basename='pet')

urlpatterns = router.urls

