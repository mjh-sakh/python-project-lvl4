from django.shortcuts import render
from task_manager.settings import DEBUG
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.views.generic.list import ListView

def index(request):
    return render(request, 'index.html', context={
        'who': _('World'),
        'env_type': 'dev' if DEBUG else 'prod',
    })

class UsersView(ListView):
    model = get_user_model()
    context_object_name = 'users'
    template_name = 'users_list.html'