from django.urls import path

from . import views
app_name = 'userInfo'
urlpatterns = [
    path('datetime', views.current_datetime, name='datetime'),
]