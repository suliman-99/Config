from rest_framework_nested import routers
from CoreApp.views import *


router = routers.DefaultRouter()

router.register(
    'configs',
    ConfigViewSet,
    basename='configs'
)

urlpatterns = router.urls

