from django.urls import path
from AppTwo import views


# interapp routing
urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.users, name='users')
]