from django.shortcuts import render
from webapp.cat_db import CatDB
from django.http import HttpResponseRedirect


def index_view(request):
    if request.method == 'GET':
        print(request.GET)
        print(request.GET.get('cat_name'))
        return render(request, 'index.html')
    elif request.method == 'POST':
        CatDB.name = request.POST.get('cat_name')
        return HttpResponseRedirect('/cat_stats/')


def cat_states_view(request):
    if request.method == 'GET':
        context = {'name': CatDB.name,
                   'age': CatDB.age,
                   'satiety': CatDB.get_satiety,
                   'happiness': CatDB.get_happiness,
                   'photo': CatDB.photo}
        return render(request, 'cat_stats.html', context)
    elif request.method == 'POST':
        action = request.POST.get('action')
        if action == 'feed':
            CatDB.feed()
        elif action == 'play':
            CatDB.play()
        elif action == 'sleep':
            CatDB.sleep()
        print(CatDB.get_info())
        return HttpResponseRedirect('/cat_stats/')

