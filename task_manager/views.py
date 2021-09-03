from django.shortcuts import render
from task_manager.settings import DEBUG


def index(request):
    return render(request, 'index.html', context={
        'who': 'World',
        'env_type': 'dev' if DEBUG else 'prod',
    })
