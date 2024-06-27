import random

from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import RegistrationForm, UserForm, ResetPasswordForm
from users.models import User


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "users/register.html"

    def get_success_url(self):
        return reverse('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = True
        user.save()
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


class ResetPasswordView(PasswordResetView):
    email_template_name = 'users/reset_password.html'
    form_class = ResetPasswordForm
    template_name = 'users/reset_password.html'

    def get_success_url(self):
        return reverse('users:login')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        user = User.objects.get(email=email)

        password = ''.join([str(random.randint(0, 9)) for _ in range(8)])
        user.password = make_password(password)
        user.save()
        message = f"Ваш новый пароль: {password}"
        send_mail(
            subject="Смена пароля",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )
        return super().form_valid(form)
