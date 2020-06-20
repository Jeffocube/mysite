from django.urls import path, include
from django.contrib import admin
admin.autodiscover()
import hello.views
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("admin/", admin.site.urls),
    path("reg/", hello.views.reg, name="reg"),
    path("getPosts/", hello.views.getPosts, name="getPosts"),
    path("forum/", hello.views.forum, name="forum"),
    path("addforum/", hello.views.addforum, name="addforum"),
    path("login/", auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
]
