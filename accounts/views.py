from django.shortcuts import render, redirect
# 장고의 유저관련 모델 가져오기
from django.contrib.auth.forms import UserCreationForm
# 로그인 기능 커스텀 하는법
from django.contrib.auth.views import LoginView
 
def signup(request):
    #UserCreationForm - 장고의 유저 폼 사용
    register_form = UserCreationForm()
    if request.method == "POST":
        filled_form = UserCreationForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('index')
            
    return render(request, 'signup.html', {'register_form':register_form})


#로그인 기능 커스텀
class MyLoginView(LoginView):
    template_name = "login.html"

