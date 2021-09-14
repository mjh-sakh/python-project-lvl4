from django.shortcuts import render
from task_manager.settings import DEBUG
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.urls import reverse_lazy


def index(request):
    return render(request, 'index.html', context={
        'who': _('World'),
        'env_type': 'dev' if DEBUG else 'prod',
    })


class CustomAuthonticationForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus': True,
        'class': 'form-control',
        'maxlength': 150,
        'placeholder': _("username"),
        'title': _("Required field. Max length is 150 symbols. Letter, numbers only."),

    }))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'class': 'form-control',
            'placeholder': _("Password"),
            'title': _("Password min length is 8 symbols."),
        }),
    )

class UserLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    form_class = CustomAuthonticationForm

    def get_success_url(self):
        return reverse_lazy('users_list')


class UsersView(ListView):
    model = get_user_model()
    context_object_name = 'users'
    template_name = 'users_list.html'


def user_update_view(request, user_id):
    users = get_user_model()
    user = users.objects.all().filter(id=user_id)[0]
    return render(request, 'base_user.html', context={
        'page_header': _("Update user information"),
        'user': user,
        'form_action': _('Update'),
    })


def user_registration_view(request):
    users = get_user_model()
    return render(request, 'base_user.html', context={
        'page_header': _('Registration'),
        'user': None,
        'form_action': _('Register'),
    })
