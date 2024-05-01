from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('blog.urls'))
    path("", views.index, name="index"),
    path("student_form", views.student_form, name="student_form"),
    path("about", views.about, name="about"),
    path("stu_manage", views.stu_manage, name="stu_manage"),
    path("service", views.Serives, name="servives"),
    path('account', views.account, name='account'),
]
