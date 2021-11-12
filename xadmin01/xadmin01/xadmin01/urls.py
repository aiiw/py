from django.contrib import admin
from django.urls import path,include
import xadmin
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', xadmin.site.urls),
    path('my01/', views.r1),
    path('my02/', views.r2),
    path('my03/',views.mssql),
    path('test1',views.test1),
    path('cache/',views.testcatche),
    path('student/',views.student),
    path('love/',include('user.urls')),
    path('user/',include('user.urls'))
]