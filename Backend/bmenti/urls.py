from django_nextjs.views import nextjs_page
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="nextjs_page"),
    path('sign-in', nextjs_page(), name='sign_in'),
    path('sign-in/<str:name>', nextjs_page(), name='sign_in all'),
    path('sign-up', views.signup, name='sign_up'),
    path('sign-up/<name>', views.signup, name='sign_up all'),
    
]