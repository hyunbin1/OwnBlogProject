from django.urls import path
from .views import index, create, detail, delete, update
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="index"),
    path('create/', create, name="create"),
    path('new/', new, name = 'new'),
    path('detail/<int:Ob_id>', detail, name="detail"),
    path('delete/<int:Ob_id>', delete, name="delete"),
    path('update/<int:Ob_id>', update, name="update"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)