from django.urls import path
<<<<<<< HEAD
from .views import login, signup, logout
=======
# from django.contrib.auth.views import LoginView, LogoutView - 로그인 커스텀 안할때 
# 로그인 커스텀 할때 LoginView 삭제해줌
from .views import signup, MyLoginView, main
from django.contrib.auth.views import LogoutView
>>>>>>> 58ee025c406dbb60fd1d34478ea30bf70226f854

urlpatterns = [
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
<<<<<<< HEAD
    path('logout/', logout, name="logout"),
=======

   # path('login/' ,LoginView.as_view(), name="login"), - 기존 장고에 있는 폼 가져오는 법
   # 커스텀 해준 로그인 뷰 가져오는법
    path('login/',MyLoginView.as_view(), name="login"),
    path('logout/',LogoutView.as_view(), name="logout"),
    path('main/',main, name="main"),
>>>>>>> 58ee025c406dbb60fd1d34478ea30bf70226f854
]