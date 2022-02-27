# 현재 앱 폴더에 대한 라우팅만 진행함
from django.urls import path
from . import views

urlpatterns = [   # path(경로, view의 기능, 참조할 이름)
    path('', views.home, name='home'),
    path('room/', views.room, name='room')
]