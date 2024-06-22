from django.urls import path

from materials.apps import MaterialsConfig
from materials.views import HomeListView, MaterialsView, MaterialDetailView

app_name = MaterialsConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('chapters/<int:pk>/materials', MaterialsView.as_view(), name='materials'),
    path('view/<int:pk>/', MaterialDetailView.as_view(), name='material-detail'),
]
