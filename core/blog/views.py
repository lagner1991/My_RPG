from django.shortcuts import render


def index(request):
    context_dict = {'one': 'первый', 'two': 'второй', 'three': 'третий'}
    return render(request, template_name='blog/index.html', context=context_dict)
