from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
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
        return reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, _('Welcome back'))
        return super().form_valid(form)


class UsersView(ListView):
    model = get_user_model()
    context_object_name = 'users'
    template_name = 'users_list.html'


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
        form_kwargs.pop('instance')
        if user is not None:
            form_kwargs['initial'] = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'username': user.username,
            }
        return self.form_class(**form_kwargs)

    def form_valid(self, form):
        messages.success(self.request, _('User information successfully updated.'))
        return super().form_valid(form)


class UserCreateView(UserUpdateView):
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_header'] = _('Registration')
        context['form_action'] = _('Register')
        return context

    def get_object(self, queryset=None):
        return self.model()

    def form_valid(self, form):
        messages.success(self.request, _('User created. Please log-in.'))
        return super(UserUpdateView, self).form_valid(form)


def delete_user(request, pk: int):
    users = get_user_model()
    user = users.objects.get(pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, _('User deleted 😢'))
        return HttpResponseRedirect(reverse_lazy('home'))
    return render(request, 'user_delete.html', context={'user': user})
