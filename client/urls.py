from django.urls import path

from client.views import CreateUser,ClientView

urlpatterns = [
    path('create_user/',CreateUser.as_view(),name='create'),
    path('toke_user/',ClientView.as_view(),name='token'),



]