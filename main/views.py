from django.shortcuts import render
from .forms import OB
from .models import OB
from django.http import Http404
# 로그인 데코레이터


# index - 모든 글
def index(request):
    all_OB = OB.objects.all()
    return render(request, 'index.html', {'all_OB':all_OB})

# create - 게시물 작성
def create(request):
    if request.method == "POST":
        filled_form = OBForm(request.POST)
        if filled_form.is_valid():
            return redirect('index')
    
    OB_form = OBForm()
    return render(request, ' create.html', {'OB_form':OB_form})


# detail - 상세 페이지
def detail(request, OB_id):
    my_OB = get_object_or_404(OB, pk=OB_id)
    return render(request, 'detail.html', {'my_OB':my_OB})
    
def delete(request, OB_id):
    my_OB = OB.objects.get(pk=jss_id)
    my_OB.delete()
    return redirect('index')
    

def update(request, OB_id):
    my_OB = OB.objects.get(pk=OB_id)
    OB_form = OBFrom(instance=my_OB)
    if request.method == "POST":
        update_form = OBForm(request.POST, instance=my_OB)
        if update_form.is_valid():
            update_form.save()
            return redirect('index')

    return render(request, 'create.html', {'OB_form':OB_form})