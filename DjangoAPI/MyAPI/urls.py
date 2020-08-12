
from django.urls import path, include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('MyAPI',views.detailsView)
urlpatterns = [
    path('api/', include(router.urls)),
    path('status/',views.predictedprice),
    path('form/',views.contact,name='detailsform')
]
