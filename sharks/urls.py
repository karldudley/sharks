from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sharks-home'),
    path('about/', views.about, name='sharks-about'),
    path('list/', views.list, name='sharks-list'),
    path('<int:id>/', views.show, name='sharks-show')
]
