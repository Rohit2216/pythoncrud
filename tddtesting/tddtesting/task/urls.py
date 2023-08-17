from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('test/', views.test_view, name='test_view'),
    path('weather/<str:city>/', views.get_weather, name='get_weather'),
    path('weather/', views.add_weather, name='add_weather'),
    path('weather/<str:city>/update/', views.update_weather, name='update_weather'),
     path('weather/<str:city>/delete/', views.delete_weather, name='delete_weather'),
    path('<int:pk>/',views.detail,name='details'),
]
