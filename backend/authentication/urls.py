from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('login', views.LoginView.as_view(), name ="login"),
    path('logout', views.LogoutView.as_view() , name ="logout"),
    path('', include(router.urls)),



]