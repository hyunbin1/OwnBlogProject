from django.shortcuts import render, redirect, get_object_or_404
from .forms import ObForm
from .models import Ob
from django.http import Http404
# 로그인 데코레이터


# index - 모든 글
def index(request):
    all_Ob = Ob.objects.all()
    return render(request, 'index.html', {'all_Ob':all_Ob})


# create - 게시물 작성
def create(request):
    if(request.method == 'POST'):
        post = Ob()
        post.title = request.POST['title']
        post.image = request.POST['image']
        post.content = request.POST['content']
        post.save()
    return redirect('index')


# detail - 상세 페이지
def detail(request, Ob_id):
    my_Ob = get_object_or_404(Ob, pk=Ob_id)
    return render(request, 'detail.html', {'my_Ob':my_Ob})
    
def delete(request, Ob_id):
    my_Ob = Ob.objects.get(pk=Ob_id)
    my_Ob.delete()
    return redirect('index')
    

def update(request, Ob_id):
    my_Ob = Ob.objects.get(pk=Ob_id)
    Ob_form = ObForm(instance=my_Ob)
    if request.method == "POST":
        update_form = ObForm(request.POST, instance=my_Ob)
        if update_form.is_valid():
            update_form.save()
            return redirect('index')

    return render(request, 'create.html', {'Ob_form':Ob_form})