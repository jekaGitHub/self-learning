from django.urls import path

from materials.apps import MaterialsConfig
from materials.views import HomeListView

app_name = MaterialsConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
]
