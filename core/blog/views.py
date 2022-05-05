from django.shortcuts import render


def index(request):
    context_dict = {'my_name': 'LAGNER_1991', 'names': ['Eva', 'Olga', 'Tata']}
    return render(request, template_name='blog/index.html', context=context_dict)
