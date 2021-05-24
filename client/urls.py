from django.urls import path

from client.views import ClientView

urlpatterns = [
    # path('create_user/',CreateUser.as_view(),name='create'),
    path('token_user/',ClientView.as_view(),name='token'),



]