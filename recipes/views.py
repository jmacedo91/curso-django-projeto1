from django.shortcuts import render

# Create your views here.


def home(request):
    """ Home View """
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Jonathan'
    })


def recipe(request, id):
    """ Recipe View """
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Jonathan'
    })
