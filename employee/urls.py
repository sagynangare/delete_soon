from django.urls import path
from . import views

app_name='employee'
urlpatterns = [
    path('', views.home),
    path('insert/',views.insert,name='insert'),
    path('display/',views.display,name='display'),
    path('update/',views.update,name='update'),
    path('delete/',views.delete,name="delete"),
]