from django.urls import path
from django.urls import path
from .views import login, signup, logout

urlpatterns = [
    path('login/', login, name="login"),
    path('signup/', login, name="signup"),
    path('logout/', login, name="logout"),