from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# Create a dictionary to simulate data storage
data = {}

# Create view function
def create(request):
    if request.method == "POST":
        key = request.POST.get("key")
        value = request.POST.get("value")
        data[key] = value
    return render(request, "create.html")

# Update view function
def update(request):
    if request.method == "POST":
        key = request.POST.get("key")
        value = request.POST.get("value")
        if key in data:
            data[key] = value
    return render(request, "update.html", {"data": data})

# Delete view function
def delete(request):
    if request.method == "POST":
        key = request.POST.get("key")
        if key in data:
            del data[key]
    return render(request, "delete.html", {"data": data})

# Read view function
def read(request):
    return render(request, "read.html", {"data": data})
