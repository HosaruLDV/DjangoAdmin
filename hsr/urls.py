from django.urls import path
from hsr.views import func
from hsr.apps import HsrConfig

app_name = HsrConfig.name

urlpatterns = [
    path('', func)
]