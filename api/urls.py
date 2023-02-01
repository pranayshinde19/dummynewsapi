from django.urls import path,include
from django.conf.urls.static import static
from .views import *
from django.conf import settings
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('business',business,basename='business')
router.register('entertainment',entertainment,basename='entertainment')
router.register('technology',technology,basename='technology')
router.register('country',country,basename='country')

urlpatterns = [
    path('',include(router.urls)),
] 
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)