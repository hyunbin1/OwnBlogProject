from django.urls import path
# from django.contrib.auth.views import LoginView, LogoutView - 로그인 커스텀 안할때 
# 로그인 커스텀 할때 LoginView 삭제해줌
from .views import signup, MyLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', signup, name="signup")

   # path('login/' ,LoginView.as_view(), name="login"), - 기존 장고에 있는 폼 가져오는 법
   # 커스텀 해준 로그인 뷰 가져오는법
    path('login/' ,MyLoginView.as_view(), name="login"),
    path('logout/',LogoutView.as_view(), name="logout"),

]