from django.urls import path
from . import views

app_name = 'note'

urlpatterns = [
    path('home/',views.home,name='home'),
    path('create/',views.create,name='create'),
    path('card1/',views.card1,name='card1'),
    path('card2/',views.card2,name='card2'),
    path('',views.index,name='index'),
]