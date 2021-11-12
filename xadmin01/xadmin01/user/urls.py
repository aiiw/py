from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('val/', views.getsqlval),
    path('tag', views.tag),
    path('updatadb', views.updatadb),
    path('deldb', views.deldb),
    path('upsql', views.upsql),
    path('delsql', views.delsql),
    path('val2/', views.getsqlval2),
    path('resql', views.resql),
    path('sendoa',views.sendoa)
]
