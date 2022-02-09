from django.http import HttpResponse
from django.shortcuts import render

from django101.demo.models import Task


# def home(request):
#     items = Task.objects.all()
#     item_strings = (f'<li>{t.title}</li>' for t in items)
#     items_string = ''.join(item_strings)
#     html = f'''
# <h1>It works!</h1>
# <ul>
#     {items_string}
# </ul>
#     '''
#     return HttpResponse(html)

def home(request):
    context = {
        'title': 'It works from view!',
        'tasks': Task.objects.all(),
    }
    return render(request, "home.html", context)
