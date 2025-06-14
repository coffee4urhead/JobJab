from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('user/', include([
        path('register/', views.register, name='register'),
        path('login/', views.login, name='login'),
        path('logout/', views.logout, name='logout'),
    ])),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('privacyPolicy/', views.privacy_policy, name='privacy_policy'),
    path('user/<str:username>/', views.account_view, name='account_view'),
    path('user/<str:username>/connections/', views.followers_following_view, name='user_connections'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)