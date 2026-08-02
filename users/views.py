from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import User
from .forms import UserRegistrationForm, UserLoginForm, UserUpdateForm


def register(request):
    """Регистрация нового пользователя с отправкой приветственного письма"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.username = form.cleaned_data.get('username', '') or user.email.split('@')[0]
            user.save()

            from django.core.mail import send_mail
            from django.conf import settings

            subject = 'Добро пожаловать в Django Shop!'
            message = f"""
Здравствуйте, {user.username}!

Благодарим вас за регистрацию в нашем интернет-магазине Django Shop.

Мы рады приветствовать вас в нашем сообществе!
Теперь вы можете просматривать товары, оставлять отзывы и следить за новинками.

С уважением,
Команда Django Shop
"""
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
            except Exception as e:
                print(f"Ошибка при отправке письма: {e}")

            messages.success(request, 'Регистрация успешно завершена! Проверьте вашу почту.')
            return redirect('users:login')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})


class UserLoginView(LoginView):
    """Контроллер для входа пользователя"""
    template_name = 'users/login.html'
    authentication_form = UserLoginForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        messages.success(self.request, 'Вы успешно вошли в систему!')
        return super().form_valid(form)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирование профиля пользователя"""
    model = User
    form_class = UserUpdateForm
    template_name = 'users/profile_edit.html'
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Профиль успешно обновлён!')
        return super().form_valid(form)
