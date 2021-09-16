from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import UpdateView
from django.views.generic.list import ListView

from task_manager.forms import CustomAuthenticationForm, CustomUserForm
from task_manager.settings import DEBUG


def index(request):
    return render(request, 'index.html', context={
        'who': _('World'),
        'env_type': 'dev' if DEBUG else 'prod',
        })


class UserLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    form_class = CustomAuthenticationForm

    def get_success_url(self):
        return reverse_lazy('users_list')


class UsersView(ListView):
    model = get_user_model()
    context_object_name = 'users'
    template_name = 'users_list.html'


def user_registration_view(request):
    users = get_user_model()
    return render(request, 'base_user.html', context={
        'page_header': _('Registration'),
        'user': None,
        'form_action': _('Register'),
        })


class UserUpdateView(UpdateView):
    model = get_user_model()
    template_name = 'base_user.html'
    success_url = reverse_lazy('users_list')
    form_class = CustomUserForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_header'] = _('Update user information')
        context['form_action'] = _('Update')
        return context

    def get_form(self):
        form_kwargs = self.get_form_kwargs()
        user = form_kwargs['instance']
        form_kwargs['user'] = user
        del form_kwargs['instance']
        if user is not None:
            form_kwargs['initial'] = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'username': user.username,
                }
        return self.form_class(**form_kwargs)


class UserCreateView(UserUpdateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_header'] = _('Registration')
        context['form_action'] = _('Register')
        return context

    def get_object(self, queryset=None):
        return self.model()
