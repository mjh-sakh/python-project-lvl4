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


def user_update_view(request, user_id):
    users = get_user_model()
    user = users.objects.all().filter(id=user_id)[0]
    return render(request, 'base_user.html', context={
        'user': user,
        'form_action': _('Update'),
    })
