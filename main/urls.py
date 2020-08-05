from django.urls import path
from .views import index, create, detail, delete, update


urlpatterns = [
    path('', index, name="index"),
    path('create/', create, name="create"),
    path('detail/<int:Ob_id>', detail, name="detail"),
    path('delete/<int:Ob_id>', delete, name="delete"),
    path('update/<int:Ob_id>', update, name="update"),



]