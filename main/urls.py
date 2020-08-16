from django.urls import path
from .views import index, create, detail, delete, update, main2


urlpatterns = [
    path('', index, name="index"),
    path('create/', create, name="create"),
    path('detail/<int:Ob_id>', detail, name="detail"),
    path('delete/<int:Ob_id>', delete, name="delete"),
    path('update/<int:Ob_id>', update, name="update"),
    path('main2/<int:Ob_id>', main2, name="main2"),
]