from django.shortcuts import render
from task_manager.settings import DEBUG
from django.utils.translation import gettext as _


def index(request):
    return render(request, 'index.html', context={
        'who': _('World'),
        'env_type': 'dev' if DEBUG else 'prod',
    })
