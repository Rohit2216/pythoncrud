from django.shortcuts import render
from myapp.models import Dish

def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, 'dish_list.html', {'dishes': dishes})
