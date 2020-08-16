from django.shortcuts import render, redirect, get_object_or_404
from .models import Ob
# 로그인 데코레이터


# index - 모든 글


def index(request):
    all_Ob = Ob.objects.all()
    return render(request, 'index.html', {'all_Ob':all_Ob})


# new page - 게시물 작성하는페이지
def create(request):
    return render(request, 'create.html')

# new - 게시물 작성하는 함수
def new(request):
    if request.method == 'POST':
            post = Ob()
            if 'image' in request.FILES:
                post.image = request.FILES['image']
            post.title = request.POST['name']
            post.content = request.POST['content']
            post.update_at = request.POST['update_at']

            post.save()
            
            return redirect('detail', post.id)


# detail - 상세 페이지
def detail(request, Ob_id):
    my_Ob = get_object_or_404(Ob, pk=Ob_id)
    return render(request, 'detail.html', {'my_Ob':my_Ob})
    

def update(request, Ob_id):
    post = get_object_or_404(Ob, pk = Ob_id)

    if request.method == 'POST':
        if 'image' in request.FILES:
            post.image = request.FILES['image']
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.update_at = request.POST['update_at']

        post.save()

        return redirect('detail', post.id)
    
    else:
        return render(request, 'update.html', {'Ob':post})


def delete(request, Ob_id):
    my_Ob = Ob.objects.get(pk=Ob_id)
    my_Ob.delete()
    return redirect('index')

def main2(request):
    return render(request, 'main2.html')