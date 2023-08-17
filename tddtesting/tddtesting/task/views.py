import json
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render  # Import the render function
from .models import Task


# from django.http import HttpResponse

# def test_view(request):
#     return HttpResponse("This is a test view.")
# Create your views here.

def index(request):
    tasks=Task.objects.all()
    return render(request, 'task/index.html',{'tasks':tasks})

def detail(request,pk):
    tasks=Task.objects.get(pk=pk)
    return render(request, 'task/detail.html',{'task':tasks})    



weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

def get_weather(request, city):
    weather = weather_data.get(city)
    if weather:
        return JsonResponse(weather)
    return HttpResponseNotFound()


def add_weather(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            city = data['city']
            temperature = data['temperature']
            weather = data['weather']

            if city and temperature and weather:
                weather_data[city] = {
                    'temperature': temperature,
                    'weather': weather,
                }
                return JsonResponse(weather_data[city], status=201)
            else:
                return HttpResponseBadRequest("Invalid data")
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON format")
    else:
        return HttpResponseBadRequest("Invalid request method")


# views.py

@csrf_exempt
def update_weather(request, city):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            updated_weather = weather_data.get(city)

            if updated_weather:
                updated_weather.update(data)
                return JsonResponse(updated_weather)
            else:
                return HttpResponseNotFound()
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON format")
    else:
        return HttpResponseBadRequest("Invalid request method")


def delete_weather(request, city):
    if city in weather_data:
        del weather_data[city]
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=404)