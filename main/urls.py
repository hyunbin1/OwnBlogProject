from django.urls import path
from .views import index, create, detail, delete, update


urlpatterns = [
    path('', index, name="index"),
    path('create/', create, name="create"),
    path('detail/', detail, name="detail"),
    path('delete/', delete, name="delete"),
    path('update/', update, name="update"),



]