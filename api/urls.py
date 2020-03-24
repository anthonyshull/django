from rest_framework.routers import SimpleRouter

from .views import EngineerViewSet

router = SimpleRouter()
router.register('engineers', EngineerViewSet, basename='engineers')

urlpatterns = router.urls
