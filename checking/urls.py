from django.urls import path

from checking.apps import CheckingConfig
from checking.views import QuestionsView

app_name = CheckingConfig.name

urlpatterns = [
    path('<int:pk>/questions/', QuestionsView.as_view(), name='questions'),
]
