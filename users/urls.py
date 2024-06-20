from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import RegisterView, UserUpdateView, ResetPasswordView

from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("registration/", RegisterView.as_view(), name="register"),

    path("profile/", UserUpdateView.as_view(), name="profile"),
    path("password-reset/", ResetPasswordView.as_view(), name="password_reset"),
]